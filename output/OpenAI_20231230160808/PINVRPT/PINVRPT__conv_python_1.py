import datetime
import pandas as pd


def read_file(file_name, columns, widths):
    return pd.read_fwf(file_name, widths=widths, header=None, names=columns)


def write_report(df, file_name, header):
    with open(file_name, "w") as f:
        f.write(header)
        df.to_string(f, index=False)


def main():
    columns = ["SERIAL", "STATUS", "TYPE", "FORMULA", "QA", "WEIGHT"]
    widths = [12, 1, 10, 15, 4, 10]
    status_dict = {0: "ACTIVE", 1: "SPENT", 3: "DESTROYED"}

    for file_type in ["ALL", "ACT", "SPN", "DES"]:
        df = read_file(f"P{file_type}", columns, widths)
        df["STATUS"] = df["STATUS"].map(status_dict).fillna("OTHER")
        header = (
            f"HAYNIE RESEARCH & DEVELOPMENT\n"
            f"PROPELLANT GRAIN INVENTORY REPORT - {file_type}\n"
            f'REPORT DATE: {datetime.datetime.now().strftime("%Y/%m/%d")}\n'
            f'{"SERIAL":<12} {"STATUS":<10} {"TYPE":<10} {"FORMULA":<15} {"QA":<4} {"WEIGHT":<10}\n'
            f'{"-"*12} {"-"*10} {"-"*10} {"-"*15} {"-"*4} {"-"*10}\n'
        )
        write_report(df, f"RPT{file_type}", header)


if __name__ == "__main__":
    main()
