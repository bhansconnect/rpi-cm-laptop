# SPDX-FileCopyrightText: 2021 The RPI CM Laptop Contributors
#
# SPDX-License-Identifier: Apache-2.0

import os
from skidl import *  # pylint: disable=unused-wildcard-import
erc_logger.stop_file_output()
logger.stop_file_output()

dirname = os.path.dirname(__file__)
kbd_sym_lib_path = os.path.join(dirname, 'kbd/kicad-symbols')
lib_search_paths[KICAD].append(kbd_sym_lib_path)

# Everything is essententially 0805 or larger for convenience.
# Probably could lower the cost some with 0603 or other optimizations.
C_FP = 'Capacitor_SMD:C_0805_2012Metric'
LED_FP = 'LED_SMD:LED_0805_2012Metric'
R_FP = 'Resistor_SMD:R_0805_2012Metric'
LCSC = 'LCSC'


@subcircuit
def key_matrx(row_pins, col_pins, vcc, gnd, led_din=None):
    current_din = led_din
    row_nets = []
    for i, r in enumerate(row_pins):
        rn = Net(f'ROW{i}')
        rn += r
        row_nets.append(rn)
    col_nets = []
    for i, c in enumerate(col_pins):
        cn = Net(f'COL{i}')
        cn += c
        col_nets.append(cn)
    for r in row_nets:
        for c in col_nets:
            key = Part('kbd', 'SW_PUSH', footprint='kbd:CherryMX_Hotswap')
            diode = Part('Device', 'D', footprint='Diode_SMD:D_SOD-123')
            diode.fields[LCSC] = 'C2099'
            key[1] += c
            key[2] += diode[2]
            diode[1] += r
            if led_din is not None:
                led = Part('kbd', 'YS-SK6812MINI-E')
                led.footprint = 'kbd:YS-SK6812MINI-E'
                led['VDD'] += vcc
                led['VSS'] += gnd
                led['DIN'] += current_din
                current_din = led['DOUT']
    current_din += NC


@subcircuit
def keyboard(uvcc, udplus, udminus, gnd):
    vcc = Net('VCC')
    vcc.drive = POWER

    # Input fuse
    fuse = Part('Device', 'Fuse', value='500mA')
    fuse.footprint = 'Fuse:Fuse_1206_3216Metric'
    fuse.fields[LCSC] = 'C369159'
    uvcc & fuse & vcc

    # MCU with power
    atmega = Part('MCU_Microchip_ATmega', 'ATmega32U4-AU')
    atmega.footprint = 'Package_QFP:TQFP-44_10x10mm_P0.8mm'
    atmega.fields[LCSC] = 'C44854'
    vcc += atmega['VCC', 'AVCC']
    gnd += atmega['GND', 'UGND', '~HWB~/PE2']
    uvcc += atmega['UVCC', 'VBUS']

    # Indicator LEDs
    rx_led = Part('Device', 'LED_Small', value='Yellow', footprint=LED_FP)
    rx_led.fields[LCSC] = 'C2296'
    tx_led = Part('Device', 'LED_Small', value='Green', footprint=LED_FP)
    tx_led.fields[LCSC] = 'C2297'
    power_led = Part('Device', 'LED_Small', value='Red', footprint=LED_FP)
    power_led.fields[LCSC] = 'C84256'
    rx_resistor = Part('Device', 'R', value='330', footprint=R_FP)
    rx_resistor.fields[LCSC] = 'C17630'
    tx_resistor = rx_resistor.copy()
    power_resistor = Part('Device', 'R', value='1K', footprint=R_FP)
    power_resistor.fields[LCSC] = 'C17513'
    vcc & power_resistor & power_led & gnd
    atmega['PB0'] & rx_resistor & rx_led & gnd
    atmega['PD5'] & tx_resistor & tx_led & gnd

    reset_pullup = Part('Device', 'R', value='10K', footprint=R_FP)
    reset_pullup.fields[LCSC] = 'C17414'
    atmega['~RESET'] & reset_pullup & vcc

    # USB Data
    dplus_resistor = Part('Device', 'R', value='22', footprint=R_FP)
    dplus_resistor.fields[LCSC] = 'C17561'
    dminus_resistor = dplus_resistor.copy()
    # Add net to keep differential pair naming
    rdplus = Net("RD+")
    rdminus = Net("RD-")
    atmega['D+'] & rdplus & dplus_resistor & udplus
    atmega['D-'] & rdminus & dminus_resistor & udminus

    # Bypass caps
    uvcc_bypass = Part('Device', 'C', value='1uF', footprint=C_FP)
    uvcc_bypass.fields[LCSC] = 'C28323'
    vcc_bypass_10u = Part('Device', 'C', value='10uF', footprint=C_FP)
    vcc_bypass_10u.fields[LCSC] = 'C15850'
    vcc_bypass_1u = Part('Device', 'C', value='1uF', footprint=C_FP)
    vcc_bypass_1u.fields[LCSC] = 'C28323'
    vcc_bypass_100n = Part('Device', 'C', value='100nF', footprint=C_FP)
    vcc_bypass_100n.fields[LCSC] = 'C49678'
    uvcc & uvcc_bypass & gnd
    vcc & vcc_bypass_10u & gnd
    vcc & vcc_bypass_1u & gnd
    vcc & vcc_bypass_100n & gnd

    ucap = Part('Device', 'C', value='1uF', footprint=C_FP)
    ucap.fields[LCSC] = 'C28323'
    atmega['UCAP'] & ucap & gnd

    aref_cap = Part('Device', 'C', value='100nF', footprint=C_FP)
    aref_cap.fields[LCSC] = 'C49678'
    atmega['AREF'] & aref_cap & gnd

    # Crystal oscillator
    oscillator = Part('Device', 'Crystal_GND24_Small', value='16MHz')
    oscillator.footprint = 'Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm'
    oscillator.fields[LCSC] = 'C13738'
    oscillator_cap1 = Part('Device', 'C', value='22pF', footprint=C_FP)
    oscillator_cap1.fields[LCSC] = 'C1804'
    oscillator_cap2 = oscillator_cap1.copy()
    oscillator[2, 4] += gnd
    atmega['XTAL1'] += oscillator[1]
    atmega['XTAL2'] += oscillator[3]
    atmega['XTAL1'] & oscillator_cap1 & gnd
    atmega['XTAL2'] & oscillator_cap2 & gnd

    key_matrx([
        atmega['PD4'],
        atmega['PC6'],
        atmega['PD7'],
        atmega['PE6'],
        atmega['PB4'],
    ], [
        atmega['PF0'],
        atmega['PF1'],
        atmega['PF4'],
        atmega['PF5'],
        atmega['PF6'],
        atmega['PF7'],
        atmega['PB1'],
        atmega['PB2'],
        atmega['PB3'],
        atmega['PB5'],
        atmega['PB6'],
        atmega['PB7'],
    ], vcc, gnd, atmega['PD3'])

    # NC fix up
    atmega['PD0', 'PD1', 'PD2', 'PD6', 'PC7'] += NC


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--xml', action='store',
                        type=argparse.FileType('w'), dest='xml', help='File to output xml to')
    parser.add_argument('--net', action='store',
                        type=argparse.FileType('w'), dest='net', help='File to output netlist to')
    args = parser.parse_args()

    # Add usb connector if defining alone.
    vbus = Net('VBUS')
    vbus.drive = POWER
    dplus = Net('D+')
    dminus = Net('D-')
    gnd = Net('GND')
    gnd.drive = POWER

    usb_c = Part('Connector', 'USB_C_Receptacle_USB2.0')
    usb_c.footprint = 'USB_C_Receptacle_HRO_TYPE-C-31-M-12'
    usb_c.fields[LCSC] = 'C165948'
    cc1_resistor = Part('Device', 'R', value='5.1K', footprint=R_FP)
    cc1_resistor.fields[LCSC] = 'C27834'
    cc2_resistor = cc1_resistor.copy()
    usb_c['VBUS'] += vbus
    usb_c['D+'] += dplus
    usb_c['D-'] += dminus
    usb_c['GND'] += gnd
    usb_c['CC1'] & cc1_resistor & gnd
    usb_c['CC2'] & cc2_resistor & gnd
    usb_c['SBU1'] += NC
    usb_c['SBU2'] += NC
    usb_c['SHIELD'] += NC

    keyboard(vbus, dplus, dminus, gnd)
    ERC()

    if args.xml is not None:
        generate_xml(file_=args.xml)
    if args.net is not None:
        generate_netlist(file_=args.net)
