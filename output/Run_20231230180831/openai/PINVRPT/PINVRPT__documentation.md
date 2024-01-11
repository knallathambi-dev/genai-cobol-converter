This COBOL program, identified as `PINVRPT`, is designed to read data from multiple input files, process the data, and write the processed data to multiple output files. The data represents an inventory of propellant grains, with each grain having attributes such as serial number, type, formula, status, QA, and weight.

**IDENTIFICATION DIVISION and ENVIRONMENT DIVISION**

The `IDENTIFICATION DIVISION` and `ENVIRONMENT DIVISION` are standard sections of a COBOL program. The `PROGRAM-ID` is `PINVRPT`. The `ENVIRONMENT DIVISION` specifies the input and output files used by the program.

**INPUT-OUTPUT SECTION and FILE-CONTROL**

The `INPUT-OUTPUT SECTION` and `FILE-CONTROL` paragraphs define the files used by the program. The `SELECT` statements associate logical file names used in the program with physical file names. The logical file names are `INALL`, `INACT`, `INSPN`, `INDES`, `RPTALL`, `RPTACT`, `RPTSPN`, and `RPTDES`.

**DATA DIVISION and FILE SECTION**

The `DATA DIVISION` and `FILE SECTION` define the structure of the input and output files. Each input file has a similar structure, with fields for the grain's serial number, type, formula, status, QA, quality, and weight. The output files are defined with a single field of 200 characters.

**WORKING-STORAGE SECTION**

The `WORKING-STORAGE SECTION` defines variables used by the program. These include variables for the current date, output records, headers for the reports, and switches to indicate when the end of a file has been reached.

**PROCEDURE DIVISION**

The `PROCEDURE DIVISION` contains the logic of the program. The `MAIN-PROGRAM` paragraph gets the current date and calls the `REPORT-ALL`, `REPORT-ACTIVE`, `REPORT-SPENT`, and `REPORT-DESTROYED` paragraphs.

Each `REPORT` paragraph opens the corresponding input and output files, reads the first record from the input file, writes headers to the output file, and then enters a loop. In the loop, the program processes each record from the input file, writes the processed record to the output file, and reads the next record from the input file. The loop continues until the end of the input file is reached, at which point the input and output files are closed.

The `ALL-LOOP`, `ACTIVE-LOOP`, `SPENT-LOOP`, and `DESTROYED-LOOP` paragraphs process the records from the input files. Each paragraph moves the fields from the input record to the output record, translates the status code to a status description, and writes the output record to the output file.

The program stops running after the `REPORT-DESTROYED` paragraph is performed.