import datetime

# File paths
INALL = "./tmp/INALL.dat"
INACT = "./tmp/INACT.dat"
INSPN = "./tmp/INSPN.dat"
INDES = "./tmp/INDES.dat"
RPTALL = "./tmp/RPTALL.dat"
RPTACT = "./tmp/RPTACT.dat"
RPTSPN = "./tmp/RPTSPN.dat"
RPTDES = "./tmp/RPTDES.dat"

# Headers
HEADER_1 = "HAYNIE RESEARCH & DEVELOPMENT"
HEADER_ALL = "PROPELLANT GRAIN INVENTORY REPORT - ALL"
HEADER_ACTIVE = "PROPELLANT GRAIN INVENTORY REPORT - ACTIVE"
HEADER_SPENT = "PROPELLANT GRAIN INVENTORY REPORT - SPENT"
HEADER_DESTROYED = "PROPELLANT GRAIN INVENTORY REPORT - DESTROYED"
HEADER_3 = "SERIAL          STATUS        TYPE          FORMULA         QA    WEIGHT"
HEADER_4 = "------------  ----------  ----------  ---------------  ----  -----------"

# Counters
INALL_COUNT = 0
INACT_COUNT = 0
INSPN_COUNT = 0
INDES_COUNT = 0
RPTALL_COUNT = 0
RPTACT_COUNT = 0
RPTSPN_COUNT = 0
RPTDES_COUNT = 0


def main():
    global current_date
    current_date = datetime.datetime.now()
    report_all()
    report_active()
    report_spent()
    report_destroyed()
    display_stats()


def report_all():
    global INALL_COUNT, RPTALL_COUNT
    with open(INALL, "r") as inall, open(RPTALL, "w") as rptall:
        rptall.write(HEADER_1 + "\n")
        rptall.write(HEADER_ALL + "\n")
        rptall.write(f"REPORT DATE: {current_date.strftime('%Y-%m-%d')}" + "\n")
        rptall.write("\n")
        rptall.write(HEADER_3 + "\n")
        rptall.write(HEADER_4 + "\n")
        for line in inall:
            INALL_COUNT += 1
            serial = line[0:12].strip()
            status = line[37:38].strip()
            if status == "0":
                status = "ACTIVE"
            elif status == "1":
                status = "SPENT"
            elif status == "3":
                status = "DESTROYED"
            else:
                status = "OTHER"
            type = line[12:22].strip()
            formula = line[22:37].strip()
            qa = line[38:42].strip()
            weight = line[72:82].strip()
            out_record = f"{serial}  {status}  {type}  {formula}  {qa}  {weight}"
            rptall.write(out_record + "\n")
            RPTALL_COUNT += 1

def report_active():
    global INACT_COUNT, RPTACT_COUNT
    with open(INACT, "r") as inall, open(RPTACT, "w") as rptall:
        rptall.write(HEADER_1 + "\n")
        rptall.write(HEADER_ACTIVE + "\n")
        rptall.write(f"REPORT DATE: {current_date.strftime('%Y-%m-%d')}" + "\n")
        rptall.write("\n")
        rptall.write(HEADER_3 + "\n")
        rptall.write(HEADER_4 + "\n")
        for line in inall:
            INACT_COUNT += 1
            serial = line[0:12].strip()
            status = line[37:38].strip()
            if status == "0":
                status = "ACTIVE"
            elif status == "1":
                status = "SPENT"
            elif status == "3":
                status = "DESTROYED"
            else:
                status = "OTHER"
            type = line[12:22].strip()
            formula = line[22:37].strip()
            qa = line[38:42].strip()
            weight = line[72:82].strip()
            out_record = f"{serial}  {status}  {type}  {formula}  {qa}  {weight}"
            rptall.write(out_record + "\n")
            RPTACT_COUNT += 1

def report_spent():
    global INSPN_COUNT, RPTSPN_COUNT
    with open(INSPN, "r") as inall, open(RPTSPN, "w") as rptall:
        rptall.write(HEADER_1 + "\n")
        rptall.write(HEADER_SPENT + "\n")
        rptall.write(f"REPORT DATE: {current_date.strftime('%Y-%m-%d')}" + "\n")
        rptall.write("\n")
        rptall.write(HEADER_3 + "\n")
        rptall.write(HEADER_4 + "\n")
        for line in inall:
            INSPN_COUNT += 1
            serial = line[0:12].strip()
            status = line[37:38].strip()
            if status == "0":
                status = "ACTIVE"
            elif status == "1":
                status = "SPENT"
            elif status == "3":
                status = "DESTROYED"
            else:
                status = "OTHER"
            type = line[12:22].strip()
            formula = line[22:37].strip()
            qa = line[38:42].strip()
            weight = line[72:82].strip()
            out_record = f"{serial}  {status}  {type}  {formula}  {qa}  {weight}"
            rptall.write(out_record + "\n")
            RPTSPN_COUNT += 1

def report_destroyed():
    global INDES_COUNT, RPTDES_COUNT
    with open(INDES, "r") as inall, open(RPTDES, "w") as rptall:
        rptall.write(HEADER_1 + "\n")
        rptall.write(HEADER_DESTROYED + "\n")
        rptall.write(f"REPORT DATE: {current_date.strftime('%Y-%m-%d')}" + "\n")
        rptall.write("\n")
        rptall.write(HEADER_3 + "\n")
        rptall.write(HEADER_4 + "\n")

        for line in inall:
            INDES_COUNT += 1
            serial = line[0:12].strip()
            status = line[37:38].strip()
            if status == "0":
                status = "ACTIVE"
            elif status == "1":
                status = "SPENT"
            elif status == "3":
                status = "DESTROYED"
            else:
                status = "OTHER"
            type = line[12:22].strip()
            formula = line[22:37].strip()
            qa = line[38:42].strip()
            weight = line[72:82].strip()
            out_record = f"{serial}  {status}  {type}  {formula}  {qa}  {weight}"
            rptall.write(out_record + "\n")
            RPTDES_COUNT += 1

def display_stats():
    print("********************************************")
    print("**** INPUT FILES ***************************")
    print(f"*** FILE INALL ROWS = {INALL_COUNT}")
    print(f"*** FILE INACT ROWS = {INACT_COUNT}")
    print(f"*** FILE INSPN ROWS = {INSPN_COUNT}")
    print(f"*** FILE INDES ROWS = {INDES_COUNT}")
    print("**** OUTPUT FILES ***************************")
    print(f"*** FILE RPTALL ROWS = {RPTALL_COUNT}")
    print(f"*** FILE RPTACT ROWS = {RPTACT_COUNT}")
    print(f"*** FILE RPTSPN ROWS = {RPTSPN_COUNT}")
    print(f"*** FILE RPTDES ROWS = {RPTDES_COUNT}")
    print("********************************************")


if __name__ == "__main__":
    main()
