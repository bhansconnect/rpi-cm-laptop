from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

keyboard_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'USB_C_Receptacle_USB2.0', 'dest':TEMPLATE, 'tool':SKIDL, 'keywords':'usb universal serial bus type-C USB2.0', 'description':'USB 2.0-only Type-C Receptacle connector', 'F1':'USB_C_Receptacle_USB2.0', 'match_pin_substring':False, 'F2':'', 'datasheet':'https://www.usb.org/sites/default/files/documents/usb_type-c.zip', 'F3':'', 'F0':'J', 'manf#':'TYPE-C-31-M-12', 'ref_prefix':'J', 'num_units':1, 'fplist':['USB*C*Receptacle*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'USB_C_Receptacle_HRO_TYPE-C-31-M-12', 'pins':[
            Pin(num='A1',name='GND',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='A12',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='A4',name='VBUS',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='A5',name='CC1',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='A6',name='D+',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='A7',name='D-',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='A8',name='SBU1',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='A9',name='VBUS',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='B1',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='B12',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='B4',name='VBUS',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='B5',name='CC2',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='B6',name='D+',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='B7',name='D-',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='B8',name='SBU2',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='B9',name='VBUS',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='S1',name='SHIELD',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'R', 'dest':TEMPLATE, 'tool':SKIDL, 'keywords':'R res resistor', 'description':'Resistor', 'F1':'R', 'match_pin_substring':False, 'F2':'', 'datasheet':'~', 'F3':'', 'F0':'R', 'ref_prefix':'R', 'num_units':1, 'fplist':['R_*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'Resistor_SMD:R_0805_2012Metric', 'pins':[
            Pin(num='1',name='~',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'Fuse', 'dest':TEMPLATE, 'tool':SKIDL, 'keywords':'fuse', 'description':'Fuse', 'F1':'Fuse', 'match_pin_substring':False, 'F2':'', 'datasheet':'~', 'F3':'', 'F0':'F', 'manf#':'JK-MSMD050', 'ref_prefix':'F', 'num_units':1, 'fplist':['*Fuse*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'Fuse:Fuse_1812_4532Metric', 'pins':[
            Pin(num='1',name='~',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'ATmega16U4-AU', 'dest':TEMPLATE, 'tool':SKIDL, 'keywords':'AVR 8bit Microcontroller MegaAVR USB', 'description':'16MHz, 32kB Flash, 2.5kB SRAM, 1kB EEPROM, USB 2.0, RC Osc, TQFP-44', 'F1':'ATmega16U4-AU', 'match_pin_substring':False, 'F2':'Package_QFP:TQFP-44_10x10mm_P0.8mm', 'datasheet':'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7766-8-bit-AVR-ATmega16U4-32U4_Datasheet.pdf', 'F3':'', 'F0':'U', '_aliases':Alias({'ATmega32U4RC-AU', 'ATmega16U4RC-AU', 'ATmega32U4-AU'}), 'manf#':'ATMEGA32U4-AU', 'ref_prefix':'U', 'num_units':1, 'fplist':['TQFP*10x10mm*P0.8mm*'], 'do_erc':True, 'aliases':Alias({'ATmega32U4RC-AU', 'ATmega16U4RC-AU', 'ATmega32U4-AU'}), 'pin':None, 'footprint':'Package_QFP:TQFP-44_10x10mm_P0.8mm', 'pins':[
            Pin(num='1',name='PE6',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='10',name='PB2',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='11',name='PB3',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='12',name='PB7',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='13',name='~RESET',func=Pin.types.INPUT,do_erc=True),
            Pin(num='14',name='VCC',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='15',name='GND',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='16',name='XTAL2',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='17',name='XTAL1',func=Pin.types.INPUT,do_erc=True),
            Pin(num='18',name='PD0',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='19',name='PD1',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='2',name='UVCC',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='20',name='PD2',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='21',name='PD3',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='22',name='PD5',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='23',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='24',name='AVCC',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='25',name='PD4',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='26',name='PD6',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='27',name='PD7',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='28',name='PB4',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='29',name='PB5',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='3',name='D-',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='30',name='PB6',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='31',name='PC6',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='32',name='PC7',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='33',name='~HWB~/PE2',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='34',name='VCC',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='35',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='36',name='PF7',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='37',name='PF6',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='38',name='PF5',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='39',name='PF4',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='4',name='D+',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='40',name='PF1',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='41',name='PF0',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='42',name='AREF',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='43',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='44',name='AVCC',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='5',name='UGND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='6',name='UCAP',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='7',name='VBUS',func=Pin.types.INPUT,do_erc=True),
            Pin(num='8',name='PB0',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='9',name='PB1',func=Pin.types.BIDIR,do_erc=True)] }),
        Part(**{ 'name':'LED_Small', 'dest':TEMPLATE, 'tool':SKIDL, 'keywords':'LED diode light-emitting-diode', 'description':'Light emitting diode, small symbol', 'F1':'LED_Small', 'match_pin_substring':False, 'F2':'', 'datasheet':'~', 'F3':'', 'F0':'D', 'ref_prefix':'D', 'num_units':1, 'fplist':['LED*', 'LED_SMD:*', 'LED_THT:*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'LED_SMD:LED_0805_2012Metric', 'pins':[
            Pin(num='1',name='K',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='A',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'C', 'dest':TEMPLATE, 'tool':SKIDL, 'keywords':'cap capacitor', 'description':'Unpolarized capacitor', 'F1':'C', 'match_pin_substring':False, 'F2':'', 'datasheet':'~', 'F3':'', 'F0':'C', 'ref_prefix':'C', 'num_units':1, 'fplist':['C_*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'Capacitor_SMD:C_0805_2012Metric', 'pins':[
            Pin(num='1',name='~',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'Crystal_Small', 'dest':TEMPLATE, 'tool':SKIDL, 'keywords':'quartz ceramic resonator oscillator', 'description':'Two pin crystal, small symbol', 'F1':'Crystal_Small', 'match_pin_substring':False, 'F2':'', 'datasheet':'~', 'F3':'', 'F0':'Y', 'manf#':'X503216MSB2GI', 'ref_prefix':'Y', 'num_units':1, 'fplist':['Crystal*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'Crystal:Crystal_SMD_5032-2Pin_5.0x3.2mm', 'pins':[
            Pin(num='1',name='1',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='2',func=Pin.types.PASSIVE,do_erc=True)] })])