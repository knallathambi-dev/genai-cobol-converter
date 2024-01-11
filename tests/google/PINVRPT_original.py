import datetime
import os


# Define the input and output files
inall_file = "./tmp/INALL.dat"
inact_file = "./tmp/INACT.dat"
inspn_file = "./tmp/INSPN.dat"
indes_file = "./tmp/INDES.dat"
rptall_file = "./tmp/RPTALL.dat"
rptact_file = "./tmp/RPTACT.dat"
rptspn_file = "./tmp/RPTSPN.dat"
rptdes_file = "./tmp/RPTDES.dat"

# Define the record layouts
inall_record_layout = [
    ("grain_serial_all", 12),
    ("grain_type_all", 10),
    ("grain_formula_all", 15),
    ("grain_status_all", 1),
    ("grain_qa_all", 4),
    ("grain_quality_all", 2),
    ("filler1", 10),
    ("filler2", 10),
    ("grain_weight_all", 10),
    ("filler3", 375),
]

inact_record_layout = [
    ("grain_serial_act", 12),
    ("grain_type_act", 10),
    ("grain_formula_act", 15),
    ("grain_status_act", 1),
    ("grain_qa_act", 4),
    ("grain_quality_act", 2),
    ("filler1", 10),
    ("filler2", 10),
    ("grain_weight_act", 10),
    ("filler3", 375),
]

inspn_record_layout = [
    ("grain_serial_spn", 12),
    ("grain_type_spn", 10),
    ("grain_formula_spn", 15),
    ("grain_status_spn", 1),
    ("grain_qa_spn", 4),
    ("grain_quality_spn", 2),
    ("filler1", 10),
    ("filler2", 10),
    ("grain_weight_spn", 10),
    ("filler3", 375),
]

indes_record_layout = [
    ("grain_serial_des", 12),
    ("grain_type_des", 10),
    ("grain_formula_des", 15),
    ("grain_status_des", 1),
    ("grain_qa_des", 4),
    ("grain_quality_des", 2),
    ("filler1", 10),
    ("filler2", 10),
    ("grain_weight_des", 10),
    ("filler3", 375),
]

# Define the output record layout
out_record_layout = [
    ("serial_out", 12),
    ("filler1", 2),
    ("status_out", 10),
    ("filler2", 2),
    ("type_out", 10),
    ("filler3", 2),
    ("formula_out", 15),
    ("filler4", 2),
    ("qa_out", 4),
    ("filler5", 2),
    ("weight_out", 10),
    ("filler6", 1),
]

# Define the header and footer records
header_1 = "HAYNIE RESEARCH & DEVELOPMENT"
header_all = "PROPELLANT GRAIN INVENTORY REPORT - ALL"
header_active = "PROPELLANT GRAIN INVENTORY REPORT - ACTIVE"
header_spent = "PROPELLANT GRAIN INVENTORY REPORT - SPENT"
header_destroyed = "PROPELLANT GRAIN INVENTORY REPORT - DESTROYED"
header_3 = (
    "SERIAL".ljust(14)
    + "STATUS".ljust(12)
    + "TYPE".ljust(12)
    + "FORMULA".ljust(17)
    + "QA".ljust(6)
    + "WEIGHT".ljust(11)
)
header_4 = (
    "------------".ljust(12)
    + "----------".ljust(10)
    + "----------".ljust(10)
    + "---------------".ljust(15)
    + "----".ljust(4)
    + "-----------".ljust(11)
)
date_line = "REPORT DATE:".ljust(12) + datetime.datetime.now().strftime("%Y/%m/%d")

# Open the input and output files
with open(inall_file, "rb") as inall, open(inact_file, "rb") as inact, open(
    inspn_file, "rb"
) as inspn, open(indes_file, "rb") as indes, open(rptall_file, "wb") as rptall, open(
    rptact_file, "wb"
) as rptact, open(
    rptspn_file, "wb"
) as rptspn, open(
    rptdes_file, "wb"
) as rptdes:
    # Initialize the counters
    inall_count = 0
    inact_count = 0
    inspn_count = 0
    indes_count = 0
    rptall_count = 0
    rptact_count = 0
    rptspn_count = 0
    rptdes_count = 0

    # Read the first record from each input file
    inall_record = inall.read(sum(length for _, length in inall_record_layout))
    inact_record = inact.read(sum(length for _, length in inact_record_layout))
    inspn_record = inspn.read(sum(length for _, length in inspn_record_layout))
    indes_record = indes.read(sum(length for _, length in indes_record_layout))

    # Write the header records to the output files
    rptall.write(header_1.encode("ascii") + b"\n")
    rptall.write(header_all.encode("ascii") + b"\n")
    rptall.write(date_line.encode("ascii") + b"\n")
    rptall.write(b"\n")
    rptall.write(header_3.encode("ascii") + b"\n")
    rptall.write(header_4.encode("ascii") + b"\n")

    rptact.write(header_1.encode("ascii") + b"\n")
    rptact.write(header_active.encode("ascii") + b"\n")
    rptact.write(date_line.encode("ascii") + b"\n")
    rptact.write(b"\n")
    rptact.write(header_3.encode("ascii") + b"\n")
    rptact.write(header_4.encode("ascii") + b"\n")

    rptspn.write(header_1.encode("ascii") + b"\n")
    rptspn.write(header_spent.encode("ascii") + b"\n")
    rptspn.write(date_line.encode("ascii") + b"\n")
    rptspn.write(b"\n")
    rptspn.write(header_3.encode("ascii") + b"\n")
    rptspn.write(header_4.encode("ascii") + b"\n")

    rptdes.write(header_1.encode("ascii") + b"\n")
    rptdes.write(header_destroyed.encode("ascii") + b"\n")
    rptdes.write(date_line.encode("ascii") + b"\n")
    rptdes.write(b"\n")
    rptdes.write(header_3.encode("ascii") + b"\n")
    rptdes.write(header_4.encode("ascii") + b"\n")

    # Process the input records
    while inall_record or inact_record or inspn_record or indes_record:
        # Process the INALL record
        if inall_record:
            inall_count += 1
            (
                grain_serial_all,
                grain_type_all,
                grain_formula_all,
                grain_status_all,
                grain_qa_all,
                grain_quality_all,
                _,
                _,
                grain_weight_all,
                _,
            ) = inall_record
            status_out = (
                "ACTIVE"
                if grain_status_all == b"0"
                else "SPENT"
                if grain_status_all == b"1"
                else "DESTROYED"
                if grain_status_all == b"3"
                else "OTHER"
            )
            out_record = (
                grain_serial_all,
                " ",
                status_out,
                " ",
                grain_type_all,
                " ",
                grain_formula_all,
                " ",
                grain_qa_all,
                " ",
                grain_weight_all,
                "G",
            )
            rptall.write("".join(out_record).encode("ascii") + b"\n")
            rptall_count += 1
            inall_record = inall.read(sum(length for _, length in inall_record_layout))

        # Process the INACT record
        if inact_record:
            inact_count += 1
            (
                grain_serial_act,
                grain_type_act,
                grain_formula_act,
                grain_status_act,
                grain_qa_act,
                grain_quality_act,
                _,
                _,
                grain_weight_act,
                _,
            ) = inact_record
            status_out = (
                "ACTIVE"
                if grain_status_act == b"0"
                else "SPENT"
                if grain_status_act == b"1"
                else "DESTROYED"
                if grain_status_act == b"3"
                else "OTHER"
            )
            out_record = (
                grain_serial_act,
                " ",
                status_out,
                " ",
                grain_type_act,
                " ",
                grain_formula_act,
                " ",
                grain_qa_act,
                " ",
                grain_weight_act,
                "G",
            )
            rptact.write("".join(out_record).encode("ascii") + b"\n")
            rptact_count += 1
            inact_record = inact.read(sum(length for _, length in inact_record_layout))

        # Process the INSPN record
        if inspn_record:
            inspn_count += 1
            (
                grain_serial_spn,
                grain_type_spn,
                grain_formula_spn,
                grain_status_spn,
                grain_qa_spn,
                grain_quality_spn,
                _,
                _,
                grain_weight_spn,
                _,
            ) = inspn_record
            status_out = (
                "ACTIVE"
                if grain_status_spn == b"0"
                else "SPENT"
                if grain_status_spn == b"1"
                else "DESTROYED"
                if grain_status_spn == b"3"
                else "OTHER"
            )
            out_record = (
                grain_serial_spn,
                " ",
                status_out,
                " ",
                grain_type_spn,
                " ",
                grain_formula_spn,
                " ",
                grain_qa_spn,
                " ",
                grain_weight_spn,
                "G",
            )
            rptspn.write("".join(out_record).encode("ascii") + b"\n")
            rptspn_count += 1
            inspn_record = inspn.read(sum(length for _, length in inspn_record_layout))

        # Process the INDES record
        if indes_record:
            indes_count += 1
            (
                grain_serial_des,
                grain_type_des,
                grain_formula_des,
                grain_status_des,
                grain_qa_des,
                grain_quality_des,
                _,
                _,
                grain_weight_des,
                _,
            ) = indes_record
            status_out = (
                "ACTIVE"
                if grain_status_des == b"0"
                else "SPENT"
                if grain_status_des == b"1"
                else "DESTROYED"
                if grain_status_des == b"3"
                else "OTHER"
            )
            out_record = (
                grain_serial_des,
                " ",
                status_out,
                " ",
                grain_type_des,
                " ",
                grain_formula_des,
                " ",
                grain_qa_des,
                " ",
                grain_weight_des,
                "G",
            )
            rptdes.write("".join(out_record).encode("ascii") + b"\n")
            rptdes_count += 1
            indes_record = indes.read(sum(length for _, length in indes_record_layout))

    # Display the statistics
    print("********************************************")
    print("**** INPUT FILES ***************************")
    print("*** FILE INALL ROWS =", inall_count)
    print("*** FILE INACT ROWS =", inact_count)
    print("*** FILE INSPN ROWS =", inspn_count)
    print("*** FILE INDES ROWS =", indes_count)
    print("**** OUTPUT FILES ***************************")
    print("*** FILE RPTALL ROWS =", rptall_count)
    print("*** FILE RPTACT ROWS =", rptact_count)
    print("*** FILE RPTSPN ROWS =", rptspn_count)
    print("*** FILE RPTDES ROWS =", rptdes_count)
    print("********************************************")
