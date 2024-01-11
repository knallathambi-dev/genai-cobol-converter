import datetime
import pandas as pd

def main():
    current_date = datetime.datetime.now()
    dt_year = current_date.year
    dt_month = current_date.month
    dt_day = current_date.day

    report_all(dt_year, dt_month, dt_day)
    report_active(dt_year, dt_month, dt_day)
    report_spent(dt_year, dt_month, dt_day)
    report_destroyed(dt_year, dt_month, dt_day)

def report_all(dt_year, dt_month, dt_day):
    df = pd.read_fwf('INALL', widths=[12, 10, 15, 1, 4, 2, 10, 10, 10, 375], header=None)
    df.to_csv('RPTALL', index=False, header=False)

def report_active(dt_year, dt_month, dt_day):
    df = pd.read_fwf('INACT', widths=[12, 10, 15, 1, 4, 2, 10, 10, 10, 375], header=None)
    df.to_csv('RPTACT', index=False, header=False)

def report_spent(dt_year, dt_month, dt_day):
    df = pd.read_fwf('INSPN', widths=[12, 10, 15, 1, 4, 2, 10, 10, 10, 375], header=None)
    df.to_csv('RPTSPN', index=False, header=False)

def report_destroyed(dt_year, dt_month, dt_day):
    df = pd.read_fwf('INDES', widths=[12, 10, 15, 1, 4, 2, 10, 10, 10, 375], header=None)
    df.to_csv('RPTDES', index=False, header=False)

if __name__ == "__main__":
    main()
