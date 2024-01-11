import datetime

def read_file(file, length):
    with open(file, 'r') as f:
        while True:
            line = f.read(length)
            if not line:
                break
            yield line

def write_file(file, data):
    with open(file, 'a') as f:
        f.write(data)

def process_file(input_file, output_file, header):
    eof_switch = 'N'
    for record in read_file(input_file, 540):
        serial_out = record[0:12].strip()
        status_out = record[38:39].strip()
        if status_out == '0':
            status_out = 'ACTIVE'
        elif status_out == '1':
            status_out = 'SPENT'
        elif status_out == '3':
            status_out = 'DESTROYED'
        else:
            status_out = 'OTHER'
        type_out = record[12:22].strip()
        formula_out = record[22:37].strip()
        qa_out = record[39:43].strip()
        weight_out = record[73:83].strip()
        out_record = f"{serial_out}  {status_out}  {type_out}  {formula_out}  {qa_out}  {weight_out}G"
        write_file(output_file, out_record)
    eof_switch = 'Y'
    return eof_switch

def main():
    current_date = datetime.datetime.now()
    dt_year = current_date.year
    dt_month = current_date.month
    dt_day = current_date.day
    headers = ['HAYNIE RESEARCH & DEVELOPMENT', 'PROPELLANT GRAIN INVENTORY REPORT - ALL', 'PROPELLANT GRAIN INVENTORY REPORT - ACTIVE', 'PROPELLANT GRAIN INVENTORY REPORT - SPENT', 'PROPELLANT GRAIN INVENTORY REPORT - DESTROYED']
    files = ['INALL', 'INACT', 'INSPN', 'INDES']
    for i in range(4):
        write_file(f"RPT{files[i]}", headers[0])
        write_file(f"RPT{files[i]}", headers[i+1])
        write_file(f"RPT{files[i]}", f"REPORT DATE: {dt_year}/{dt_month}/{dt_day}")
        write_file(f"RPT{files[i]}", ' ')
        write_file(f"RPT{files[i]}", 'SERIAL  STATUS  TYPE  FORMULA  QA  WEIGHT')
        write_file(f"RPT{files[i]}", '------------  ----------  ----------  ---------------  ----  -----------')
        process_file(files[i], f"RPT{files[i]}", headers[i+1])

if __name__ == "__main__":
    main()
