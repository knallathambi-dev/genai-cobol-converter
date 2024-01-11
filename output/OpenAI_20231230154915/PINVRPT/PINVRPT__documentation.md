# COBOL Code Documentation

## IDENTIFICATION DIVISION
This section is used to specify the name and type of the program. The `PROGRAM-ID` is `PINVRPT`.

## ENVIRONMENT DIVISION
This section describes the environment in which the program will execute. It includes the `INPUT-OUTPUT SECTION` and `FILE-CONTROL` where the files used in the program are defined.

- `INALL`, `INACT`, `INSPN`, `INDES` are input files.
- `RPTALL`, `RPTACT`, `RPTSPN`, `RPTDES` are output files.

## DATA DIVISION
This section describes the data items processed by the program.

### FILE SECTION
This section describes the format of the files used in the program. Each file has a `FD` (File Description) entry that describes the structure of the records in the file.

- `INALL`, `INACT`, `INSPN`, `INDES` are input files with fixed-length records. Each record contains information about a grain, including its serial number, type, formula, status, QA, quality, and weight.
- `RPTALL`, `RPTACT`, `RPTSPN`, `RPTDES` are output files with variable-length records. Each record is a string of 200 characters.

### WORKING-STORAGE SECTION
This section describes the data items that are used internally by the program. It includes the current date, output record, date line, headers, and switches.

## PROCEDURE DIVISION
This section contains the executable instructions of the program.

### MAIN-PROGRAM
This section gets the current date and performs the four report procedures (`REPORT-ALL`, `REPORT-ACTIVE`, `REPORT-SPENT`, `REPORT-DESTROYED`).

### REPORT-ALL, REPORT-ACTIVE, REPORT-SPENT, REPORT-DESTROYED
These sections generate the four reports. Each section opens the corresponding input and output files, reads the first record from the input file, writes the headers to the output file, and performs a loop until it reaches the end of the input file. In each iteration of the loop, it formats a record and writes it to the output file, then reads the next record from the input file. After the loop, it closes the input and output files.

### ALL-LOOP, ACTIVE-LOOP, SPENT-LOOP, DESTROYED-LOOP
These sections format a record and write it to the corresponding output file. They move the fields from the input record to the output record, translate the status code to a status string, and write the output record to the output file. They then read the next record from the input file.

The code is well-structured and follows good COBOL programming practices. It uses meaningful names for data items and procedures, and it uses indentation to make the structure of the code clear. It also uses comments to explain the purpose of each section and procedure.