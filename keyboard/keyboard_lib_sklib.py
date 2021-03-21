from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

keyboard_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'USB_C_Receptacle_USB2.0', 'dest':TEMPLATE, 'tool':SKIDL, 'F2':'', 'datasheet':'https://www.usb.org/sites/default/files/documents/usb_type-c.zip', 'keywords':'usb universal serial bus type-C USB2.0', 'F0':'J', 'LCSC':'C165948', 'match_pin_substring':False, 'F1':'USB_C_Receptacle_USB2.0', 'description':'USB 2.0-only Type-C Receptacle connector', 'F3':'', 'ref_prefix':'J', 'num_units':1, 'fplist':['USB*C*Receptacle*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'USB_C_Receptacle_HRO_TYPE-C-31-M-12', 'pins':[
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
        Part(**{ 'name':'R', 'dest':TEMPLATE, 'tool':SKIDL, 'F2':'', 'datasheet':'~', 'keywords':'R res resistor', 'F0':'R', 'LCSC':'C27834', 'match_pin_substring':False, 'F1':'R', 'description':'Resistor', 'F3':'', 'ref_prefix':'R', 'num_units':1, 'fplist':['R_*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'Resistor_SMD:R_0805_2012Metric', 'pins':[
            Pin(num='1',name='~',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'Fuse', 'dest':TEMPLATE, 'tool':SKIDL, 'F2':'', 'datasheet':'~', 'keywords':'fuse', 'F0':'F', 'LCSC':'C369159', 'match_pin_substring':False, 'F1':'Fuse', 'description':'Fuse', 'F3':'', 'ref_prefix':'F', 'num_units':1, 'fplist':['*Fuse*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'Fuse:Fuse_1206_3216Metric', 'pins':[
            Pin(num='1',name='~',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'ATmega16U4-AU', 'dest':TEMPLATE, 'tool':SKIDL, 'F2':'Package_QFP:TQFP-44_10x10mm_P0.8mm', 'datasheet':'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7766-8-bit-AVR-ATmega16U4-32U4_Datasheet.pdf', 'keywords':'AVR 8bit Microcontroller MegaAVR USB', 'F0':'U', '_aliases':Alias({'ATmega32U4RC-AU', 'ATmega16U4RC-AU', 'ATmega32U4-AU'}), 'LCSC':'C44854', 'match_pin_substring':False, 'F1':'ATmega16U4-AU', 'description':'16MHz, 32kB Flash, 2.5kB SRAM, 1kB EEPROM, USB 2.0, RC Osc, TQFP-44', 'F3':'', 'ref_prefix':'U', 'num_units':1, 'fplist':['TQFP*10x10mm*P0.8mm*'], 'do_erc':True, 'aliases':Alias({'ATmega32U4RC-AU', 'ATmega16U4RC-AU', 'ATmega32U4-AU'}), 'pin':None, 'footprint':'Package_QFP:TQFP-44_10x10mm_P0.8mm', 'pins':[
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
        Part(**{ 'name':'LED_Small', 'dest':TEMPLATE, 'tool':SKIDL, 'F2':'', 'datasheet':'~', 'keywords':'LED diode light-emitting-diode', 'F0':'D', 'LCSC':'C2296', 'match_pin_substring':False, 'F1':'LED_Small', 'description':'Light emitting diode, small symbol', 'F3':'', 'ref_prefix':'D', 'num_units':1, 'fplist':['LED*', 'LED_SMD:*', 'LED_THT:*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'LED_SMD:LED_0805_2012Metric', 'pins':[
            Pin(num='1',name='K',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='A',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'C', 'dest':TEMPLATE, 'tool':SKIDL, 'F2':'', 'datasheet':'~', 'keywords':'cap capacitor', 'F0':'C', 'LCSC':'C28323', 'match_pin_substring':False, 'F1':'C', 'description':'Unpolarized capacitor', 'F3':'', 'ref_prefix':'C', 'num_units':1, 'fplist':['C_*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'Capacitor_SMD:C_0805_2012Metric', 'pins':[
            Pin(num='1',name='~',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'Crystal_GND24_Small', 'dest':TEMPLATE, 'tool':SKIDL, 'F2':'', 'datasheet':'~', 'keywords':'quartz ceramic resonator oscillator', 'F0':'Y', 'LCSC':'C13738', 'match_pin_substring':False, 'F1':'Crystal_GND24_Small', 'description':'Four pin crystal, GND on pins 2 and 4, small symbol', 'F3':'', 'ref_prefix':'Y', 'num_units':1, 'fplist':['Crystal*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm', 'pins':[
            Pin(num='1',name='1',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='2',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='3',name='3',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='4',name='4',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'SW_PUSH', 'dest':TEMPLATE, 'tool':SKIDL, 'F2':'', 'datasheet':'', 'keywords':'', 'F0':'SW', 'match_pin_substring':False, 'F1':'SW_PUSH', 'description':'', 'F3':'', 'ref_prefix':'SW', 'num_units':1, 'fplist':[], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'kbd:CherryMX_Hotswap', 'pins':[
            Pin(num='1',name='1',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='2',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'D', 'dest':TEMPLATE, 'tool':SKIDL, 'F2':'', 'datasheet':'~', 'keywords':'diode', 'F0':'D', 'LCSC':'C2099', 'match_pin_substring':False, 'F1':'D', 'description':'Diode', 'F3':'', 'ref_prefix':'D', 'num_units':1, 'fplist':['TO-???*', '*_Diode_*', '*SingleDiode*', 'D_*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'Diode_SMD:D_SOD-123', 'pins':[
            Pin(num='1',name='K',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='A',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'YS-SK6812MINI-E', 'dest':TEMPLATE, 'tool':SKIDL, 'F2':'', 'datasheet':'', 'keywords':'', 'F0':'LED', 'match_pin_substring':False, 'F1':'YS-SK6812MINI-E', 'description':'', 'F3':'', 'ref_prefix':'LED', 'num_units':1, 'fplist':[], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'kbd:YS-SK6812MINI-E', 'pins':[
            Pin(num='1',name='VDD',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='2',name='DOUT',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='3',name='VSS',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='4',name='DIN',func=Pin.types.INPUT,do_erc=True)] })])