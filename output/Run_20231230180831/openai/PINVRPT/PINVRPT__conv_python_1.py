import datetime
import os
import pandas as pd

FILE_PATH = './tmp'

def read_file(file_name, columns, column_lengths):
    file_path = os.path.join(FILE_PATH, f'{file_name}.dat')
    df = pd.read_fwf(file_path, widths=column_lengths, header=None)
    df.columns = columns
    return df


def write_report(df, file_name, header):
    file_path = os.path.join(FILE_PATH, f'{file_name}.dat')
    with open(file_path, "w") as file:
        file.write(header)
        df.to_string(file, index=False)


def main():
    columns = [
        "grain_serial",
        "grain_type",
        "grain_formula",
        "grain_status",
        "grain_qa",
        "grain_quality",
        "filler1",
        "filler2",
        "grain_weight",
        "filler3",
    ]
    column_lengths = [12, 10, 15, 1, 4, 2, 10, 10, 10, 375]

    df_all = read_file("INALL", columns, column_lengths)
    df_act = read_file("INACT", columns, column_lengths)
    df_spn = read_file("INSPN", columns, column_lengths)
    df_des = read_file("INDES", columns, column_lengths)

    header = f"REPORT DATE: {datetime.datetime.now().strftime('%Y/%m/%d')}\n"
    header += "SERIAL  STATUS  TYPE  FORMULA  QA  WEIGHT\n"
    header += (
        "------------  ----------  ----------  ---------------  ----  -----------\n"
    )

    write_report(
        df_all,
        "RPTALL",
        header
        + "HAYNIE RESEARCH & DEVELOPMENT\nPROPELLANT GRAIN INVENTORY REPORT - ALL\n",
    )
    write_report(
        df_act,
        "RPTACT",
        header
        + "HAYNIE RESEARCH & DEVELOPMENT\nPROPELLANT GRAIN INVENTORY REPORT - ACTIVE\n",
    )
    write_report(
        df_spn,
        "RPTSPN",
        header
        + "HAYNIE RESEARCH & DEVELOPMENT\nPROPELLANT GRAIN INVENTORY REPORT - SPENT\n",
    )
    write_report(
        df_des,
        "RPTDES",
        header
        + "HAYNIE RESEARCH & DEVELOPMENT\nPROPELLANT GRAIN INVENTORY REPORT - DESTROYED\n",
    )


if __name__ == "__main__":
    main()
