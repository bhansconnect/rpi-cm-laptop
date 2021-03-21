#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2021 The RPI CM Laptop Contributors
#
# SPDX-License-Identifier: Apache-2.0

# First generate the XML BOM using skidl.
# Then feed it into this script to create a BOM ready for upload to JLCPCB.
# This requires a LCSC field containing the LCSC part number.

if __name__ == '__main__':
    import argparse
    import xml.etree.ElementTree as ET
    import xlsxwriter

    parser = argparse.ArgumentParser()
    parser.add_argument('xml', action='store',
                        type=argparse.FileType('r'), help='SKIDL XML to be converted to BOM')
    parser.add_argument('-o', '--out', action='store',
                        dest='bom', help='File to output xlsx BOM to')
    args = parser.parse_args()

    if args.bom is None:
        args.bom = 'bom.xlsx'

    xml = ET.parse(args.xml)
    root = xml.getroot()
    components = None
    for child in root:
        if child.tag == 'components':
            components = child
            break
    if components is None:
        print('Could not find components')
        print('Are you sure this is a proper SKIDL XML file?')
        exit(-1)

    partmap = {}
    nolcscmap = {}
    for comp in components:
        ref = comp.attrib['ref']
        value = None
        footprint = None
        lcsc = None
        for child in comp:
            if child.tag == 'value':
                value = child.text
            if child.tag == 'footprint':
                footprint = child.text
            if child.tag == 'fields':
                for field in child.text.splitlines():
                    if 'LCSC' in field:
                        lcsc = field.split()[-1][:-1]
        if value is None:
            print(f'Component {ref} has no value')
        if footprint is None:
            print(f'Component {ref} has no footprint')
        if lcsc is None:
            print(f'Component {ref} has no lcsc number')
            # group by value and footprint if they don't have an lcsc number
            key = (value, footprint)
            if key not in nolcscmap:
                nolcscmap[key] = []

            nolcscmap[key].append(
                {'ref': ref, 'value': value, 'footprint': footprint})
            continue

        if lcsc not in partmap:
            partmap[lcsc] = []

        partmap[lcsc].append(
            {'ref': ref, 'value': value, 'footprint': footprint})

    workbook = xlsxwriter.Workbook(args.bom)
    worksheet = workbook.add_worksheet()

    max_widths = [0]*4
    row = 0
    worksheet.write(row, 0, 'Comment')
    worksheet.write(row, 1, 'Designator')
    worksheet.write(row, 2, 'Footprint')
    worksheet.write(row, 3, 'LCSC Part #（optional）')
    max_widths[0] = len('Comment')
    max_widths[1] = len('Designator')
    max_widths[2] = len('Footprint')
    max_widths[3] = len('LCSC Part #（optional）')
    row += 1

    for lcsc, parts in partmap.items():
        # verify part compatibility
        value = parts[0]['value']
        footprint = parts[0]['footprint']
        for part in parts:
            if part['value'] != value or part['footprint'] != footprint:
                print(
                    f'Parts sharing the lcsc component {lcsc} are not the same')
                print(parts)
                print(part)
                exit(0)

        # output parts
        refs = []
        for part in parts:
            refs.append(part['ref'])
        # Note, refs is already sorted due to SKIDL sorting it in the XML
        worksheet.write(row, 0, value)
        worksheet.write(row, 1, ', '.join(refs))
        worksheet.write(row, 2, footprint)
        worksheet.write(row, 3, lcsc)
        max_widths[0] = max(max_widths[0], len(value))
        max_widths[1] = max(max_widths[1], len(', '.join(refs)))
        max_widths[2] = max(max_widths[2], len(footprint))
        max_widths[3] = max(max_widths[3], len(lcsc))
        row += 1

    # output other parts without lcsc number
    for parts in nolcscmap.values():
        # output parts
        refs = []
        for part in parts:
            refs.append(part['ref'])
        # Note, refs is already sorted due to SKIDL sorting it in the XML
        worksheet.write(row, 0, parts[0]['value'])
        worksheet.write(row, 1, ', '.join(refs))
        worksheet.write(row, 2, parts[0]['footprint'])
        max_widths[0] = max(max_widths[0], len(value))
        max_widths[1] = max(max_widths[1], len(', '.join(refs)))
        max_widths[2] = max(max_widths[2], len(footprint))
        row += 1

    for i, width in enumerate(max_widths):
        worksheet.set_column(i, i, width)

    workbook.close()
