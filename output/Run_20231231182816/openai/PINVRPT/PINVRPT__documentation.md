# COBOL Code Documentation

## Identification Division
This section identifies the program. The `PROGRAM-ID` is `PINVRPT`.

## Environment Division
This section describes the environment in which the program will execute. It includes the `INPUT-OUTPUT SECTION` and `FILE-CONTROL` where the input and output files are defined. The `SELECT` statement assigns a file name to a file identifier. The `ASSIGN TO` clause specifies the physical file name. The `ORGANIZATION` clause specifies the organization of the file as `LINE SEQUENTIAL`.

## Data Division
This section describes the data structures used in the program. It includes the `FILE SECTION` and `WORKING-STORAGE SECTION`.

### File Section
This section describes the structure of the files used in the program. Each file has a `FD` entry that describes the structure of the records in the file. The `01` level numbers define the record structure. The `05` level numbers define the fields within the record.

### Working-Storage Section
This section defines the variables used in the program. It includes variables for the current date, output record, date line, headers, switches, and counters.

## Procedure Division
This section contains the logic of the program. It includes the `MAIN-PROGRAM` and several sub-programs.

### Main-Program
This sub-program gets the current date, performs the `REPORT-ALL`, `REPORT-ACTIVE`, `REPORT-SPENT`, `REPORT-DESTROYED`, and `DISPLAY-STATS` sub-programs, and then stops the run.

### Report-All, Report-Active, Report-Spent, Report-Destroyed
These sub-programs generate reports for all, active, spent, and destroyed grains respectively. They open the input and output files, read the first record from the input file, write the headers to the output file, and then perform a loop until the end of file switch is 'Y'. In the loop, they move the fields from the input record to the output record, write the output record to the output file, and read the next record from the input file. After the loop, they close the input and output files.

### All-Loop, Active-Loop, Spent-Loop, Destroyed-Loop
These sub-programs are performed in the `REPORT-ALL`, `REPORT-ACTIVE`, `REPORT-SPENT`, and `REPORT-DESTROYED` sub-programs respectively. They add 1 to the count of input records, move the fields from the input record to the output record, write the output record to the output file, add 1 to the count of output records, and read the next record from the input file.

### Display-Stats
This sub-program displays the counts of rows in the input and output files.

## End of Program
The `STOP RUN` statement ends the program.