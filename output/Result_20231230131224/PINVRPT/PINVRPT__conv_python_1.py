import datetime

def read_record(file, size):
    return file.read(size)

def write_record(file, record):
    file.write(record)

def main():
    current_date = datetime.datetime.now()
    dt_year = current_date.year
    dt_month = current_date.month
    dt_day = current_date.day

    report_all()
    report_active()
    report_spent()
    report_destroyed()

def report_all():
    with open('INALL', 'r') as inall, open('RPTALL', 'w') as rptall:
        eof_switch = 'N'
        while eof_switch != 'Y':
            record = read_record(inall, 200)
            if record == '':
                eof_switch = 'Y'
            else:
                write_record(rptall, record)

def report_active():
    with open('INACT', 'r') as inact, open('RPTACT', 'w') as rptact:
        eof_switch = 'N'
        while eof_switch != 'Y':
            record = read_record(inact, 200)
            if record == '':
                eof_switch = 'Y'
            else:
                write_record(rptact, record)

def report_spent():
    with open('INSPN', 'r') as inspn, open('RPTSPN', 'w') as rptspn:
        eof_switch = 'N'
        while eof_switch != 'Y':
            record = read_record(inspn, 200)
            if record == '':
                eof_switch = 'Y'
            else:
                write_record(rptspn, record)

def report_destroyed():
    with open('INDES', 'r') as indes, open('RPTDES', 'w') as rptdes:
        eof_switch = 'N'
        while eof_switch != 'Y':
            record = read_record(indes, 200)
            if record == '':
                eof_switch = 'Y'
            else:
                write_record(rptdes, record)

if __name__ == "__main__":
    main()
