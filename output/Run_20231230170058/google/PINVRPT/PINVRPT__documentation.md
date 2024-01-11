## IDENTIFICATION DIVISION.

### PROGRAM-ID.
This line specifies the program name as PINVRPT.

## ENVIRONMENT DIVISION.

### INPUT-OUTPUT SECTION.

### FILE-CONTROL.
This section defines the files used in the program.

- **INALL:** This file contains the records for all grain inventory items.
- **INACT:** This file contains the records for active grain inventory items.
- **INSPN:** This file contains the records for spent grain inventory items.
- **INDES:** This file contains the records for destroyed grain inventory items.
- **RPTALL:** This file is used to generate the report for all grain inventory items.
- **RPTACT:** This file is used to generate the report for active grain inventory items.
- **RPTSPN:** This file is used to generate the report for spent grain inventory items.
- **RPTDES:** This file is used to generate the report for destroyed grain inventory items.

## DATA DIVISION.

### FILE SECTION.

This section defines the structure of the files used in the program.

- **FD INALL:** This file contains fixed-length records, each of which is 400 bytes long.
  - **GRAIN-SERIAL-ALL:** This field contains the serial number of the grain inventory item.
  - **GRAIN-TYPE-ALL:** This field contains the type of grain inventory item.
  - **GRAIN-FORMULA-ALL:** This field contains the formula of the grain inventory item.
  - **GRAIN-STATUS-ALL:** This field contains the status of the grain inventory item.
  - **GRAIN-QA-ALL:** This field contains the QA status of the grain inventory item.
  - **GRAIN-QUALITY-ALL:** This field contains the quality of the grain inventory item.
  - **FILLER:** This field is used for padding.
  - **GRAIN-WEIGHT-ALL:** This field contains the weight of the grain inventory item.
  - **FILLER:** This field is used for padding.

- **FD INACT:** This file contains fixed-length records, each of which is 400 bytes long.
  - **GRAIN-SERIAL-ACT:** This field contains the serial number of the grain inventory item.
  - **GRAIN-TYPE-ACT:** This field contains the type of grain inventory item.
  - **GRAIN-FORMULA-ACT:** This field contains the formula of the grain inventory item.
  - **GRAIN-STATUS-ACT:** This field contains the status of the grain inventory item.
  - **GRAIN-QA-ACT:** This field contains the QA status of the grain inventory item.
  - **GRAIN-QUALITY-ACT:** This field contains the quality of the grain inventory item.
  - **FILLER:** This field is used for padding.
  - **GRAIN-WEIGHT-ACT:** This field contains the weight of the grain inventory item.
  - **FILLER:** This field is used for padding.

- **FD INSPN:** This file contains fixed-length records, each of which is 400 bytes long.
  - **GRAIN-SERIAL-SPN:** This field contains the serial number of the grain inventory item.
  - **GRAIN-TYPE-SPN:** This field contains the type of grain inventory item.
  - **GRAIN-FORMULA-SPN:** This field contains the formula of the grain inventory item.
  - **GRAIN-STATUS-SPN:** This field contains the status of the grain inventory item.
  - **GRAIN-QA-SPN:** This field contains the QA status of the grain inventory item.
  - **GRAIN-QUALITY-SPN:** This field contains the quality of the grain inventory item.
  - **FILLER:** This field is used for padding.
  - **GRAIN-WEIGHT-SPN:** This field contains the weight of the grain inventory item.
  - **FILLER:** This field is used for padding.

- **FD INDES:** This file contains fixed-length records, each of which is 400 bytes long.
  - **GRAIN-SERIAL-DES:** This field contains the serial number of the grain inventory item.
  - **GRAIN-TYPE-DES:** This field contains the type of grain inventory item.
  - **GRAIN-FORMULA-DES:** This field contains the formula of the grain inventory item.
  - **GRAIN-STATUS-DES:** This field contains the status of the grain inventory item.
  - **GRAIN-QA-DES:** This field contains the QA status of the grain inventory item.
  - **GRAIN-QUALITY-DES:** This field contains the quality of the grain inventory item.
  - **FILLER:** This field is used for padding.
  - **GRAIN-WEIGHT-DES:** This field contains the weight of the grain inventory item.
  - **FILLER:** This field is used for padding.

- **FD RPTALL:** This file contains variable-length records.
  - **OUTFILE-ALL:** This field contains the output for the report for all grain inventory items.

- **FD RPTACT:** This file contains variable-length records.
  - **OUTFILE-ACTIVE:** This field contains the output for the report for active grain inventory items.

- **FD RPTSPN:** This file contains variable-length records.
  - **OUTFILE-SPENT:** This field contains the output for the report for spent grain inventory items.

- **FD RPTDES:** This file contains variable-length records.
  - **OUTFILE-DESTROYED:** This field contains the output for the report for destroyed grain inventory items.

### WORKING-STORAGE SECTION.

This section defines the working storage variables used in the program.

- **WS-CURRENT-DATE:** This variable contains the current date and time.
  - **WS-YEAR:** This field contains the year.
  - **WS-MONTH:** This field contains the month.
  - **WS-DAY:** This field contains the day.
  - **WS-HOURS:** This field contains the hours.
  - **WS-MINUTES:** This field contains the minutes.
  - **WS-SECONDS:** This field contains the seconds.
  - **WS-HUND-SECOND:** This field contains the hundredths of a second.
  - **WS-GMT:** This field contains the Greenwich Mean Time (GMT) offset.

- **OUT-RECORD:** This variable contains the output record for the reports.
  - **SERIAL-OUT:** This field contains the serial number of the grain inventory item.
  - **FILLER:** This field is used for padding.
  - **STATUS-OUT:** This field contains the status of the grain inventory item.
  - **FILLER:** This field is used for padding.
  - **TYPE-OUT:** This field contains the type of grain inventory item.
  - **FILLER:** This field is used for padding.
  - **FORMULA-OUT:** This field contains the formula of the grain inventory item.
  - **FILLER:** This field is used for padding.
  - **QA-OUT:** This field contains the QA status of the grain inventory item.
  - **FILLER:** This field is used for padding.
  - **WEIGHT-OUT:** This field contains the weight of the grain inventory item.
  - **FILLER:** This field is used for padding.

- **DATE-LINE:** This variable contains the date line for the reports.
  - **FILLER:** This field contains the text "REPORT DATE:".
  - **FILLER:** This field is used for padding.
  - **DT-YEAR:** This field contains the year.
  - **FILLER:** This field contains the slash character (/).
  - **DT-MONTH:** This field contains the month.
  - **FILLER:** This field contains the slash character (/).
  - **DT-DAY:** This field contains the day.

- **HEADER-1:** This variable contains the first header line for the reports.
  - **FILLER:** This field contains the text "HAYNIE RESEARCH & DEVELOPMENT".

- **HEADER-ALL:** This variable contains the header line for the report for all grain inventory items.
  - **FILLER:** This field contains the text "PROPELLANT GRAIN INVENTORY REPORT - ALL".

- **HEADER-ACTIVE:** This variable contains the header line for the report for active grain inventory items.
  - **FILLER:** This field contains the text "PROPELLANT GRAIN INVENTORY REPORT - ACTIVE".

- **HEADER-SPENT:** This variable contains the header line for the report for spent grain inventory items.
  - **FILLER:** This field contains the text "PROPELLANT GRAIN INVENTORY REPORT - SPENT".

- **HEADER-DESTROYED:** This variable contains the header line for the report for destroyed grain inventory items.
  - **FILLER:** This field contains the text "PROPELLANT GRAIN INVENTORY REPORT - DESTROYED".

- **HEADER-3:** This variable contains the third header line for the reports.
  - **FILLER:** This field contains the text "SERIAL".
  - **FILLER:** This field contains the text "STATUS".
  - **FILLER:** This field contains the text "TYPE".
  - **FILLER:** This field contains the text "FORMULA".
  - **FILLER:** This field contains the text "QA".
  - **FILLER:** This field contains the text "WEIGHT".

- **HEADER-4:** This variable contains the fourth header line for the reports.
  - **FILLER:** This field contains the text "------------".
  - **FILLER:** This field is used for padding.
  - **FILLER:** This field contains the text "----------".
  - **FILLER:** This field is used for padding.
  - **FILLER:** This field contains the text "----------".
  - **FILLER:** This field is used for padding.
  - **FILLER:** This field contains the text "---------------".
  - **FILLER:** This field is used for padding.
  - **FILLER:** This field contains the text "----".
  - **FILLER:** This field is used for padding.
  - **FILLER:** This field contains the text "-----------".

- **SWITCHES:** This variable contains the switches used to control the program flow.
  - **INALL-EOF-SWITCH:** This field contains the end-of-file switch for the INALL file.
  - **INACT-EOF-SWITCH:** This field contains the end-of-file switch for the INACT file.
  - **INSPN-EOF-SWITCH:** This field contains the end-of-file switch for the INSPN file.
  - **INDES-EOF-SWITCH:** This field contains the end-of-file switch for the INDES file.

### PROCEDURE DIVISION.

This section contains the procedure division of the program.

- **MAIN-PROGRAM:** This is the main program of the program.
  - It calls the REPORT-ALL, REPORT-ACTIVE, REPORT-SPENT, and REPORT-DESTROYED paragraphs to generate the reports.

- **REPORT-ALL:** This paragraph generates the report for all grain inventory items.
  - It opens the INALL and RPTALL files.
  - It reads the INALL file and writes the output to the RPTALL file.
  - It closes the INALL and RPTALL files.

- **REPORT-ACTIVE:** This paragraph generates the report for active grain inventory items.
  - It opens the INACT and RPTACT files.
  - It reads the INACT file and writes the output to the RPTACT file.
  - It closes the INACT and RPTACT files.

- **REPORT-SPENT:** This paragraph generates the report for spent grain inventory items.
  - It opens the INSPN and RPTSPN files.
  - It reads the INSPN file and writes the output to the RPTSPN file.
  - It closes the INSPN and RPTSPN files.

- **REPORT-DESTROYED:** This paragraph generates the report for destroyed grain inventory items.
  - It opens the INDES and RPTDES files.
  - It reads the INDES file and writes the output to the RPTDES file.
  - It closes the INDES and RPTDES files.

- **ALL-LOOP:** This paragraph is used to read the INALL file and write the output to the RPTALL file.
  - It moves the grain serial number, status, type, formula, QA status, and weight to the OUT-RECORD variable.
  - It writes the OUT-RECORD variable to the RPTALL file.
  - It reads the next record from the INALL file.

- **ACTIVE-LOOP:** This paragraph is used to read the INACT file and write the output to the RPTACT file.
  - It moves the grain serial number, status, type, formula, QA status, and weight to the OUT-RECORD variable.
  - It writes the OUT-RECORD variable to the RPTACT file.
  - It reads the next record from the INACT file.

- **SPENT-LOOP:** This paragraph is used to read the INSPN file and write the output to the RPTSPN file.
  - It moves the grain serial number, status, type, formula, QA status, and weight to the OUT-RECORD variable.
  - It writes the OUT-RECORD variable to the RPTSPN file.
  - It reads the next record from the INSPN file.

- **DESTROYED-LOOP:** This paragraph is used to read the INDES file and write the output to the RPTDES file.
  - It moves the grain serial number, status, type, formula, QA status, and weight to the OUT-RECORD variable.
  - It writes the OUT-RECORD variable to the RPTDES file.
  - It reads the next record from the INDES file.