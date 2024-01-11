# COBOL Code Documentation

This COBOL program, identified as `PINVRPT`, is designed to read data from multiple files, process it, and write the processed data to multiple output files. The data represents an inventory of propellant grain, with each record containing information about the grain's serial number, type, formula, status, QA, quality, and weight.

## Environment Division

The `ENVIRONMENT DIVISION` specifies the input and output files used in the program. The `FILE-CONTROL` section maps logical file names used in the program to the physical files in the operating system.

## Data Division

The `DATA DIVISION` describes the structure of the data in the files and the working storage variables used in the program.

### File Section

The `FILE SECTION` describes the structure of the records in each file. Each input file (`INALL`, `INACT`, `INSPN`, `INDES`) has a similar structure, with fields for the grain's serial number, type, formula, status, QA, quality, and weight. The output files (`RPTALL`, `RPTACT`, `RPTSPN`, `RPTDES`) each contain a single field for a string of 200 characters.

### Working-Storage Section

The `WORKING-STORAGE SECTION` defines variables used in the program. These include variables for the current date and time, output records, headers for the reports, and switches to indicate when the end of a file has been reached.

## Procedure Division

The `PROCEDURE DIVISION` contains the logic of the program. It begins with the `MAIN-PROGRAM` section, which gets the current date and time and then calls the `REPORT-ALL`, `REPORT-ACTIVE`, `REPORT-SPENT`, and `REPORT-DESTROYED` sections to generate the four reports.

Each `REPORT` section opens the appropriate input and output files, reads the first record from the input file, writes the headers to the output file, and then enters a loop to process each record in the input file. The loop continues until the end of the file is reached, as indicated by the appropriate EOF switch.

In the loop, the program moves the fields from the input record to the output record, translates the status code to a string, and writes the output record to the output file. It then reads the next record from the input file.

After all records have been processed, the program closes the input and output files and returns to the `MAIN-PROGRAM` section. When all reports have been generated, the program stops.

## Note

This is a high-level overview of the program. Each section and variable in the program would be documented in more detail in a complete code documentation.