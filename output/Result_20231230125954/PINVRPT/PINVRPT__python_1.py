import datetime

def read_record(file, size):
    return [file.read(size) for _ in range(9)]

def write_report(file, header, records):
    file.write(header + '\n')
    file.write('REPORT DATE: ' + datetime.datetime.now().strftime('%Y/%m/%d') + '\n\n')
    file.write('SERIAL  STATUS  TYPE  FORMULA  QA  WEIGHT\n')
    file.write('------------  ----------  ----------  ---------------  ----  -----------\n')
    for record in records:
        file.write(' '.join(record) + '\n')

def main():
    with open('PINV', 'r') as inall, open('PACT', 'r') as inact, open('PSPN', 'r') as inspn, open('PDES', 'r') as indes, \
         open('RPTALL', 'w') as rptall, open('RPTACT', 'w') as rptact, open('RPTSPN', 'w') as rptspn, open('RPTDES', 'w') as rptdes:

        records_all = [read_record(inall, 12) for _ in range(9)]
        records_act = [read_record(inact, 12) for _ in range(9)]
        records_spn = [read_record(inspn, 12) for _ in range(9)]
        records_des = [read_record(indes, 12) for _ in range(9)]

        write_report(rptall, 'PROPELLANT GRAIN INVENTORY REPORT - ALL', records_all)
        write_report(rptact, 'PROPELLANT GRAIN INVENTORY REPORT - ACTIVE', records_act)
        write_report(rptspn, 'PROPELLANT GRAIN INVENTORY REPORT - SPENT', records_spn)
        write_report(rptdes, 'PROPELLANT GRAIN INVENTORY REPORT - DESTROYED', records_des)

if __name__ == "__main__":
    main()
