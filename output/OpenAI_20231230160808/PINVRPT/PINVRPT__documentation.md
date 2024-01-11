# COBOL Code Documentation

This COBOL program is named `PINVRPT`. It reads data from four different files (`INALL`, `INACT`, `INSPN`, `INDES`), processes the data, and writes the output to four corresponding report files (`RPTALL`, `RPTACT`, `RPTSPN`, `RPTDES`). The data represents an inventory of propellant grains with different statuses (active, spent, destroyed, etc.).

## Identification Division

This section identifies the program. The `PROGRAM-ID` is `PINVRPT`.

## Environment Division

This section describes the environment in which the program will execute. It includes the `INPUT-OUTPUT SECTION` and `FILE-CONTROL` paragraph, which maps the logical files used in the program to the physical files in the operating system.

## Data Division

This section describes the data structures used in the program. It includes the `FILE SECTION` and `WORKING-STORAGE SECTION`.

### File Section

This section describes the structure of the files used in the program. Each file has a `FD` (File Description) entry, which includes the name of the file and the structure of the records in the file. For example, the `INALL` file has records with fields like `GRAIN-SERIAL-ALL`, `GRAIN-TYPE-ALL`, `GRAIN-FORMULA-ALL`, etc.

### Working-Storage Section

This section describes the data items that are used internally by the program. It includes items like `WS-CURRENT-DATE`, `OUT-RECORD`, `DATE-LINE`, `HEADER-1`, `HEADER-ALL`, `HEADER-ACTIVE`, `HEADER-SPENT`, `HEADER-DESTROYED`, `HEADER-3`, `HEADER-4`, and `SWITCHES`.

## Procedure Division

This section contains the logic of the program. It includes the `MAIN-PROGRAM` and several sub-programs (`REPORT-ALL`, `REPORT-ACTIVE`, `REPORT-SPENT`, `REPORT-DESTROYED`, `ALL-LOOP`, `ACTIVE-LOOP`, `SPENT-LOOP`, `DESTROYED-LOOP`).

### MAIN-PROGRAM

This is the main entry point of the program. It gets the current date, performs the four report procedures, and then stops the program.

### REPORT-ALL, REPORT-ACTIVE, REPORT-SPENT, REPORT-DESTROYED

These procedures generate the four reports. Each procedure opens the corresponding input and output files, reads the first record from the input file, writes the headers to the output file, performs a loop to process each record, and then closes the files.

### ALL-LOOP, ACTIVE-LOOP, SPENT-LOOP, DESTROYED-LOOP

These procedures process each record from the corresponding input file. They move the fields from the input record to the output record, write the output record to the output file, and then read the next record from the input file. The loop continues until the end of the input file is reached.