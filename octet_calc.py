#!/usr/bin/python3
# Author: David Chidell (dchidell)

from openpyxl import load_workbook
import subnet_toolkit as st

def main():
    wb = load_workbook('subnets.xlsx')
    ws = wb.get_active_sheet()
    for row in ws.rows:
        row_list = list(map(lambda field: field.value if field.value is not None else 'None', row))
        if row_list[0] is None: continue
        if row_list[1] is None: continue
        ip = row_list[0]

        cidr = int(str(row_list[1]).strip('/'))
        int_ip = st.ip_to_int(ip)
        int_cidr = st.cidr_to_int(cidr)
        first_addr = (int_ip & int_cidr)+1
        print('{}'.format(st.int_to_ip(first_addr)))

if __name__ == "__main__":
    main()