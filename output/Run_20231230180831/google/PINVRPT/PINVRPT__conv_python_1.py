import datetime

# Define the input and output files
inall_file = "PINV"
inact_file = "PACT"
inspn_file = "PSPN"
indes_file = "PDES"
rptall_file = "RPTALL"
rptact_file = "RPTACT"
rptspn_file = "RPTSPN"
rptdes_file = "RPTDES"

# Define the record layouts
inall_record_layout = [
    ("GRAIN-SERIAL-ALL", 12, "9"),
    ("GRAIN-TYPE-ALL", 10, "X"),
    ("GRAIN-FORMULA-ALL", 15, "X"),
    ("GRAIN-STATUS-ALL", 1, "X"),
    ("GRAIN-QA-ALL", 4, "X"),
    ("GRAIN-QUALITY-ALL", 2, "9"),
    ("FILLER", 10, "9"),
    ("FILLER", 10, "9"),
    ("GRAIN-WEIGHT-ALL", 10, "9"),
    ("FILLER", 375, "X"),
]

inact_record_layout = [
    ("GRAIN-SERIAL-ACT", 12, "9"),
    ("GRAIN-TYPE-ACT", 10, "X"),
    ("GRAIN-FORMULA-ACT", 15, "X"),
    ("GRAIN-STATUS-ACT", 1, "X"),
    ("GRAIN-QA-ACT", 4, "X"),
    ("GRAIN-QUALITY-ACT", 2, "9"),
    ("FILLER", 10, "9"),
    ("FILLER", 10, "9"),
    ("GRAIN-WEIGHT-ACT", 10, "9"),
    ("FILLER", 375, "X"),
]

inspn_record_layout = [
    ("GRAIN-SERIAL-SPN", 12, "9"),
    ("GRAIN-TYPE-SPN", 10, "X"),
    ("GRAIN-FORMULA-SPN", 15, "X"),
    ("GRAIN-STATUS-SPN", 1, "X"),
    ("GRAIN-QA-SPN", 4, "X"),
    ("GRAIN-QUALITY-SPN", 2, "9"),
    ("FILLER", 10, "9"),
    ("FILLER", 10, "9"),
    ("GRAIN-WEIGHT-SPN", 10, "9"),
    ("FILLER", 375, "X"),
]

indes_record_layout = [
    ("GRAIN-SERIAL-DES", 12, "9"),
    ("GRAIN-TYPE-DES", 10, "X"),
    ("GRAIN-FORMULA-DES", 15, "X"),
    ("GRAIN-STATUS-DES", 1, "X"),
    ("GRAIN-QA-DES", 4, "X"),
    ("GRAIN-QUALITY-DES", 2, "9"),
    ("FILLER", 10, "9"),
    ("FILLER", 10, "9"),
    ("GRAIN-WEIGHT-DES", 10, "9"),
    ("FILLER", 375, "X"),
]

# Define the output record layouts
out_record_layout = [
    ("SERIAL-OUT", 12, "X"),
    ("FILLER", 2, "X", " "),
    ("STATUS-OUT", 10, "X"),
    ("FILLER", 2, "X", " "),
    ("TYPE-OUT", 10, "X"),
    ("FILLER", 2, "X", " "),
    ("FORMULA-OUT", 15, "X"),
    ("FILLER", 2, "X", " "),
    ("QA-OUT", 4, "X"),
    ("FILLER", 2, "X", " "),
    ("WEIGHT-OUT", 10, "X"),
    ("FILLER", 1, "X", "G"),
]

date_line_layout = [
    ("FILLER", 12, "X", "REPORT DATE:"),
    ("FILLER", 1, "X", " "),
    ("DT-YEAR", 4, "9"),
    ("FILLER", 1, "X", "/"),
    ("DT-MONTH", 2, "9"),
    ("FILLER", 1, "X", "/"),
    ("DT-DAY", 2, "9"),
]

header_1_layout = [("FILLER", 100, "X", "HAYNIE RESEARCH & DEVELOPMENT")]

header_all_layout = [("FILLER", 100, "X", "PROPELLANT GRAIN INVENTORY REPORT - ALL")]

header_active_layout = [
    ("FILLER", 100, "X", "PROPELLANT GRAIN INVENTORY REPORT - ACTIVE")
]

header_spent_layout = [
    ("FILLER", 100, "X", "PROPELLANT GRAIN INVENTORY REPORT - SPENT")
]

header_destroyed_layout = [
    ("FILLER", 100, "X", "PROPELLANT GRAIN INVENTORY REPORT - DESTROYED")
]

header_3_layout = [
    ("FILLER", 14, "X", "SERIAL"),
    ("FILLER", 12, "X", "STATUS"),
    ("FILLER", 12, "X", "TYPE"),
    ("FILLER", 17, "X", "FORMULA"),
    ("FILLER", 6, "X", "QA"),
    ("FILLER", 11, "X", "WEIGHT"),
]

header_4_layout = [
    ("FILLER", 12, "X", "------------"),
    ("FILLER", 2, "X", " "),
    ("FILLER", 10, "X", "----------"),
    ("FILLER", 2, "X", " "),
    ("FILLER", 10, "X", "----------"),
    ("FILLER", 2, "X", " "),
    ("FILLER", 15, "X", "---------------"),
    ("FILLER", 2, "X", " "),
    ("FILLER", 4, "X", "----"),
    ("FILLER", 2, "X", " "),
    ("FILLER", 11, "X", "-----------"),
]

# Define the switches
switches = {
    "INALL-EOF-SWITCH": "N",
    "INACT-EOF-SWITCH": "N",
    "INSPN-EOF-SWITCH": "N",
    "INDES-EOF-SWITCH": "N",
}

# Get the current date
current_date = datetime.datetime.now()

# Format the date for the report
dt_year = current_date.strftime("%Y")
dt_month = current_date.strftime("%m")
dt_day = current_date.strftime("%d")

# Open the input and output files
with open(inall_file, "r") as inall, open(inact_file, "r") as inact, open(
    inspn_file, "r"
) as inspn, open(indes_file, "r") as indes, open(rptall_file, "w") as rptall, open(
    rptact_file, "w"
) as rptact, open(
    rptspn_file, "w"
) as rptspn, open(
    rptdes_file, "w"
) as rptdes:
    # Write the header information to the report files
    rptall.write(header_1_layout[0][1] + "\n")
    rptall.write(header_all_layout[0][1] + "\n")
    rptall.write(
        date_line_layout[0][1] + " " + dt_year + "/" + dt_month + "/" + dt_day + "\n"
    )
    rptall.write("\n")
    rptall.write(header_3_layout[0][1] + "\n")
    rptall.write(header_4_layout[0][1] + "\n")

    rptact.write(header_1_layout[0][1] + "\n")
    rptact.write(header_active_layout[0][1] + "\n")
    rptact.write(
        date_line_layout[0][1] + " " + dt_year + "/" + dt_month + "/" + dt_day + "\n"
    )
    rptact.write("\n")
    rptact.write(header_3_layout[0][1] + "\n")
    rptact.write(header_4_layout[0][1] + "\n")

    rptspn.write(header_1_layout[0][1] + "\n")
    rptspn.write(header_spent_layout[0][1] + "\n")
    rptspn.write(
        date_line_layout[0][1] + " " + dt_year + "/" + dt_month + "/" + dt_day + "\n"
    )
    rptspn.write("\n")
    rptspn.write(header_3_layout[0][1] + "\n")
    rptspn.write(header_4_layout[0][1] + "\n")

    rptdes.write(header_1_layout[0][1] + "\n")
    rptdes.write(header_destroyed_layout[0][1] + "\n")
    rptdes.write(
        date_line_layout[0][1] + " " + dt_year + "/" + dt_month + "/" + dt_day + "\n"
    )
    rptdes.write("\n")
    rptdes.write(header_3_layout[0][1] + "\n")
    rptdes.write(header_4_layout[0][1] + "\n")

    # Read the first record from each input file
    inall_record = inall.readline()
    inact_record = inact.readline()
    inspn_record = inspn.readline()
    indes_record = indes.readline()

    # Loop through the input files until all records have been processed
    while True:
        # Parse the input records
        inall_record_parsed = dict(
            zip(
                [field[0] for field in inall_record_layout],
                [
                    inall_record[field[2] : field[2] + field[3]]
                    for field in inall_record_layout
                ],
            )
        )
        inact_record_parsed = dict(
            zip(
                [field[0] for field in inact_record_layout],
                [
                    inact_record[field[2] : field[2] + field[3]]
                    for field in inact_record_layout
                ],
            )
        )
        inspn_record_parsed = dict(
            zip(
                [field[0] for field in inspn_record_layout],
                [
                    inspn_record[field[2] : field[2] + field[3]]
                    for field in inspn_record_layout
                ],
            )
        )
        indes_record_parsed = dict(
            zip(
                [field[0] for field in indes_record_layout],
                [
                    indes_record[field[2] : field[2] + field[3]]
                    for field in indes_record_layout
                ],
            )
        )

        # Determine the status of the grain
        if inall_record_parsed["GRAIN-STATUS-ALL"] == "0":
            status_out = "ACTIVE"
        elif inall_record_parsed["GRAIN-STATUS-ALL"] == "1":
            status_out = "SPENT"
        elif inall_record_parsed["GRAIN-STATUS-ALL"] == "3":
            status_out = "DESTROYED"
        else:
            status_out = "OTHER"

        if inact_record_parsed["GRAIN-STATUS-ACT"] == "0":
            status_out = "ACTIVE"
        elif inact_record_parsed["GRAIN-STATUS-ACT"] == "1":
            status_out = "SPENT"
        elif inact_record_parsed["GRAIN-STATUS-ACT"] == "3":
            status_out = "DESTROYED"
        else:
            status_out = "OTHER"

        if inspn_record_parsed["GRAIN-STATUS-SPN"] == "0":
            status_out = "ACTIVE"
        elif inspn_record_parsed["GRAIN-STATUS-SPN"] == "1":
            status_out = "SPENT"
        elif inspn_record_parsed["GRAIN-STATUS-SPN"] == "3":
            status_out = "DESTROYED"
        else:
            status_out = "OTHER"

        if indes_record_parsed["GRAIN-STATUS-DES"] == "0":
            status_out = "ACTIVE"
        elif indes_record_parsed["GRAIN-STATUS-DES"] == "1":
            status_out = "SPENT"
        elif indes_record_parsed["GRAIN-STATUS-DES"] == "3":
            status_out = "DESTROYED"
        else:
            status_out = "OTHER"

        # Create the output record
        out_record = {
            "SERIAL-OUT": inall_record_parsed["GRAIN-SERIAL-ALL"],
            "STATUS-OUT": status_out,
            "TYPE-OUT": inall_record_parsed["GRAIN-TYPE-ALL"],
            "FORMULA-OUT": inall_record_parsed["GRAIN-FORMULA-ALL"],
            "QA-OUT": inall_record_parsed["GRAIN-QA-ALL"],
            "WEIGHT-OUT": inall_record_parsed["GRAIN-WEIGHT-ALL"],
        }

        # Write the output record to the report files
        rptall.write(
            out_record["SERIAL-OUT"]
            + "  "
            + out_record["STATUS-OUT"]
            + "  "
            + out_record["TYPE-OUT"]
            + "  "
            + out_record["FORMULA-OUT"]
            + "  "
            + out_record["QA-OUT"]
            + "  "
            + out_record["WEIGHT-OUT"]
            + "\n"
        )

        if out_record["STATUS-OUT"] == "ACTIVE":
            rptact.write(
                out_record["SERIAL-OUT"]
                + "  "
                + out_record["STATUS-OUT"]
                + "  "
                + out_record["TYPE-OUT"]
                + "  "
                + out_record["FORMULA-OUT"]
                + "  "
                + out_record["QA-OUT"]
                + "  "
                + out_record["WEIGHT-OUT"]
                + "\n"
            )
        elif out_record["STATUS-OUT"] == "SPENT":
            rptspn.write(
                out_record["SERIAL-OUT"]
                + "  "
                + out_record["STATUS-OUT"]
                + "  "
                + out_record["TYPE-OUT"]
                + "  "
                + out_record["FORMULA-OUT"]
                + "  "
                + out_record["QA-OUT"]
                + "  "
                + out_record["WEIGHT-OUT"]
                + "\n"
            )
        elif out_record["STATUS-OUT"] == "DESTROYED":
            rptdes.write(
                out_record["SERIAL-OUT"]
                + "  "
                + out_record["STATUS-OUT"]
                + "  "
                + out_record["TYPE-OUT"]
                + "  "
                + out_record["FORMULA-OUT"]
                + "  "
                + out_record["QA-OUT"]
                + "  "
                + out_record["WEIGHT-OUT"]
                + "\n"
            )

        # Read the next record from each input file
        inall_record = inall.readline()
        inact_record = inact.readline()
        inspn_record = inspn.readline()
        indes_record = indes.readline()

        # Check if all input files have been processed
        if (
            inall_record == ""
            and inact_record == ""
            and inspn_record == ""
            and indes_record == ""
        ):
            break

    # Close the input and output files
    inall.close()
    inact.close()
    inspn.close()
    indes.close()
    rptall.close()
    rptact.close()
    rptspn.close()
    rptdes.close()


def main():
    PINVRPT()


if __name__ == "__main__":
    main()
