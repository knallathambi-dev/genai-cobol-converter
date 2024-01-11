```
=== COBOL START ===

IDENTIFICATION DIVISION.
PROGRAM-ID.  PINVRPT.

* This program generates four reports:
* 1. A report of all propellant grain inventory items
* 2. A report of all active propellant grain inventory items
* 3. A report of all spent propellant grain inventory items
* 4. A report of all destroyed propellant grain inventory items

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
    * Define the input and output files.

    SELECT INALL ASSIGN TO PINV.
    * Input file containing all propellant grain inventory items

    SELECT INACT ASSIGN TO PACT.
    * Input file containing all active propellant grain inventory items

    SELECT INSPN ASSIGN TO PSPN.
    * Input file containing all spent propellant grain inventory items

    SELECT INDES ASSIGN TO PDES.
    * Input file containing all destroyed propellant grain inventory items

    SELECT RPTALL ASSIGN TO RPTALL.
    * Output file for the all propellant grain inventory report

    SELECT RPTACT ASSIGN TO RPTACT.
    * Output file for the active propellant grain inventory report

    SELECT RPTSPN ASSIGN TO RPTSPN.
    * Output file for the spent propellant grain inventory report

    SELECT RPTDES ASSIGN TO RPTDES.
    * Output file for the destroyed propellant grain inventory report

DATA DIVISION.
FILE SECTION.

    * Define the record layouts for the input and output files.

    FD INALL
        RECORDING MODE F.
    01  INALL-RECORD-ALL.
        05  GRAIN-SERIAL-ALL             PIC 9(12).
        * Grain serial number
        05  GRAIN-TYPE-ALL               PIC X(10).
        * Grain type
        05  GRAIN-FORMULA-ALL            PIC X(15).
        * Grain formula
        05  GRAIN-STATUS-ALL             PIC X(1).
        * Grain status (0=Active, 1=Spent, 3=Destroyed)
        05  GRAIN-QA-ALL                 PIC X(4).
        * Grain QA code
        05  GRAIN-QUALITY-ALL            PIC 9(2).
        * Grain quality rating
        05  FILLER                       PIC 9(10).
        05  FILLER                       PIC 9(10).
        05  GRAIN-WEIGHT-ALL             PIC 9(10).
        * Grain weight in grams
        05  FILLER                       PIC X(375).

    FD INACT
        RECORDING MODE F.
    01  INALL-RECORD-ACT.
        05  GRAIN-SERIAL-ACT             PIC 9(12).
        * Grain serial number
        05  GRAIN-TYPE-ACT               PIC X(10).
        * Grain type
        05  GRAIN-FORMULA-ACT            PIC X(15).
        * Grain formula
        05  GRAIN-STATUS-ACT             PIC X(1).
        * Grain status (0=Active, 1=Spent, 3=Destroyed)
        05  GRAIN-QA-ACT                 PIC X(4).
        * Grain QA code
        05  GRAIN-QUALITY-ACT            PIC 9(2).
        * Grain quality rating
        05  FILLER                       PIC 9(10).
        05  FILLER                       PIC 9(10).
        05  GRAIN-WEIGHT-ACT             PIC 9(10).
        * Grain weight in grams
        05  FILLER                       PIC X(375).

    FD INSPN
        RECORDING MODE F.
    01  INALL-RECORD-SPN.
        05  GRAIN-SERIAL-SPN             PIC 9(12).
        * Grain serial number
        05  GRAIN-TYPE-SPN               PIC X(10).
        * Grain type
        05  GRAIN-FORMULA-SPN            PIC X(15).
        * Grain formula
        05  GRAIN-STATUS-SPN             PIC X(1).
        * Grain status (0=Active, 1=Spent, 3=Destroyed)
        05  GRAIN-QA-SPN                 PIC X(4).
        * Grain QA code
        05  GRAIN-QUALITY-SPN            PIC 9(2).
        * Grain quality rating
        05  FILLER                       PIC 9(10).
        05  FILLER                       PIC 9(10).
        05  GRAIN-WEIGHT-SPN             PIC 9(10).
        * Grain weight in grams
        05  FILLER                       PIC X(375).

    FD INDES
        RECORDING MODE F.
    01  INALL-RECORD-DES.
        05  GRAIN-SERIAL-DES             PIC 9(12).
        * Grain serial number
        05  GRAIN-TYPE-DES               PIC X(10).
        * Grain type
        05  GRAIN-FORMULA-DES            PIC X(15).
        * Grain formula
        05  GRAIN-STATUS-DES             PIC X(1).
        * Grain status (0=Active, 1=Spent, 3=Destroyed)
        05  GRAIN-QA-DES                 PIC X(4).
        * Grain QA code
        05  GRAIN-QUALITY-DES            PIC 9(2).
        * Grain quality rating
        05  FILLER                       PIC 9(10).
        05  FILLER                       PIC 9(10).
        05  GRAIN-WEIGHT-DES             PIC 9(10).
        * Grain weight in grams
        05  FILLER                       PIC X(375).

    FD RPTALL
        RECORDING MODE V.
    01  OUTFILE-ALL                 PIC X(200).
    * Output record for the all propellant grain inventory report

    FD RPTACT
        RECORDING MODE V.
    01  OUTFILE-ACTIVE              PIC X(200).
    * Output record for the active propellant grain inventory report

    FD RPTSPN
        RECORDING MODE V.
    01  OUTFILE-SPENT               PIC X(200).
    * Output record for the spent propellant grain inventory report

    FD RPTDES
        RECORDING MODE V.
    01  OUTFILE-DESTROYED           PIC X(200).
    * Output record for the destroyed propellant grain inventory report

WORKING-STORAGE SECTION.

    * Declare working-storage variables.

    01  WS-CURRENT-DATE.
        05  WS-YEAR                 PIC 9(4).
        * Current year
        05  WS-MONTH                PIC 9(2).
        * Current month
        05  WS-DAY                  PIC 9(2).
        * Current day
        05  WS-HOURS                PIC 9(2).
        * Current hour
        05  WS-MINUTES              PIC 9(2).
        * Current minute
        05  WS-SECONDS              PIC 9(2).
        * Current second
        05  WS-HUND-SECOND          PIC 9(2).
        * Current hundredth of a second
        05  WS-GMT                  PIC X(5).
        * Current GMT offset

    01  OUT-RECORD.
        05  SERIAL-OUT              PIC X(12).
        * Grain serial number
        05  FILLER                  PIC X(2)
            VALUE  SPACES.
        05  STATUS-OUT              PIC X(10).
        * Grain status
        05  FILLER                  PIC X(2)
            VALUE SPACES.
        05  TYPE-OUT                PIC X(10).
        * Grain type
        05  FILLER                  PIC X(2)
            VALUE  SPACES.
        05  FORMULA-OUT             PIC X(15).
        * Grain formula
        05  FILLER                  PIC X(2)
            VALUE  SPACES.
        05  QA-OUT                  PIC X(4).
        * Grain QA code
        05  FILLER                  PIC X(2)
            VALUE  SPACES.
        05  WEIGHT-OUT              PIC X(10).
        * Grain weight in grams
        05  FILLER                  PIC X
            VALUE 'G'.

    01  DATE-LINE.
        05  FILLER                  PIC X(12)
            VALUE 'REPORT DATE:'.
        05  FILLER                  PIC X(1)
            VALUE SPACES.
        05  DT-YEAR                 PIC 9(4).
        * Year of the report date
        05  FILLER                  PIC X
            VALUE '/'.
        05  DT-MONTH                PIC 9(2).
        * Month of the report date
        05  FILLER                  PIC X
            VALUE '/'.
        05  DT-DAY                  PIC 9(2).
        * Day of the report date

    01  HEADER-1.
        05  FILLER                  PIC X(100)
            VALUE  'HAYNIE RESEARCH & DEVELOPMENT'.

    01  HEADER-ALL.
        05  FILLER                  PIC X(100)
            VALUE  'PROPELLANT GRAIN INVENTORY REPORT - ALL'.

    01  HEADER-ACTIVE.
        05  FILLER                  PIC X(100)
            VALUE  'PROPELLANT GRAIN INVENTORY REPORT - ACTIVE'.

    01  HEADER-SPENT.
        05  FILLER                  PIC X(100)
            VALUE  'PROPELLANT GRAIN INVENTORY REPORT - SPENT'.

    01  HEADER-DESTROYED.
        05  FILLER                  PIC X(100)
            VALUE  'PROPELLANT GRAIN INVENTORY REPORT - DESTROYED'.

    01  HEADER-3.
        05  FILLER                  PIC X(14)
            VALUE  'SERIAL'.
        05  FILLER                  PIC X(12)
            VALUE  'STATUS'.
        05  FILLER                  PIC X(12)
            VALUE  'TYPE'.
        05  FILLER                  PIC X(17)
            VALUE  'FORMULA'.
        05  FILLER                  PIC X(6)
            VALUE  'QA'.
        05  FILLER                  PIC X(11)
            VALUE  'WEIGHT'.

    01  HEADER-4.
        05  FILLER                  PIC X(12)
            VALUE  '------------'.
        05  FILLER                  PIC X(2)
            VALUE SPACES.
        05  FILLER                  PIC X(10)
            VALUE  '----------'.
        05  FILLER                  PIC X(2)
            VALUE SPACES.
        05  FILLER                  PIC X(10)
            VALUE '----------'.
        05  FILLER                  PIC X(2)
            VALUE SPACES.
        05  FILLER                  PIC X(15)
            VALUE '---------------'.
        05  FILLER                  PIC X(2)
            VALUE SPACES.
        05  FILLER                  PIC X(4)
            VALUE '----'.
        05  FILLER                  PIC X(2)
            VALUE SPACES.
        05  FILLER                  PIC X(11)
            VALUE '-----------'.

    01  SWITCHES.
        05  INALL-EOF-SWITCH         PIC X(1) VALUE 'N'.
        * End-of-file switch for INALL file
        05  INACT-EOF-SWITCH         PIC X(1) VALUE 'N'.
        * End-of-file switch for INACT file
        05  INSPN-EOF-SWITCH         PIC X(1) VALUE 'N'.
        * End-of-file switch for INSPN file
        05  INDES-EOF-SWITCH         PIC X(1) VALUE 'N'.
        * End-of-file switch for INDES file

PROCEDURE DIVISION.

    * Main program

    MAIN-PROGRAM.
        MOVE FUNCTION CURRENT-DATE TO WS-CURRENT-DATE.
        * Get the current date and time
        MOVE WS-YEAR TO DT-YEAR.
        * Move the year to the date line
        MOVE WS-MONTH TO DT-MONTH.
        * Move the month to the date line
        MOVE WS-DAY TO DT-DAY.
        * Move the day to the date line
        PERFORM REPORT-ALL.
        * Perform the report-all procedure
        PERFORM REPORT-ACTIVE.
        * Perform the report-active procedure
        PERFORM REPORT-SPENT.
        * Perform the report-spent procedure
        PERFORM REPORT-DESTROYED.
        * Perform the report-destroyed procedure
        STOP RUN.
        * Stop the program

    * Report-all procedure

    REPORT-ALL.
        OPEN INPUT INALL
             OUTPUT RPTALL.
        * Open the INALL and RPTALL files
        READ INALL
            AT END
                MOVE 'Y' TO INALL-EOF-SWITCH
        END-READ.
        * Read the first record from INALL
        MOVE HEADER-1 TO OUTFILE-ALL.
        * Move the header-1 line to the output file
        WRITE OUTFILE-ALL.
        * Write the header-1 line to the output file
        MOVE HEADER-ALL TO OUTFILE-ALL.
        * Move the header-all line to the output file
        WRITE OUTFILE-ALL.
        * Write the header-all line to the output file
        MOVE DATE-LINE TO OUTFILE-ALL.
        * Move the date-line line to the output file
        WRITE OUTFILE-ALL.
        * Write the date-line line to the output file
        MOVE SPACES TO OUTFILE-ALL.
        * Move spaces to the output file
        WRITE OUTFILE-ALL.
        * Write spaces to the output file
        MOVE HEADER-3 TO OUTFILE-ALL.
        * Move the header-3 line to the output file
        WRITE OUTFILE-ALL.
        * Write the header-3 line to the output file
        MOVE HEADER-4 TO OUTFILE-ALL.
        * Move the header-4 line to the output file
        WRITE OUTFILE-ALL.
        * Write the header-4 line to the output file
        PERFORM ALL-LOOP
            UNTIL INALL-EOF-SWITCH = 'Y'.
        * Perform the all-loop procedure until the end-of-file switch is 'Y'
        CLOSE INALL
              RPTALL.
        * Close the INALL and RPTALL files

    * Report-active procedure

    REPORT-ACTIVE.
        OPEN INPUT INACT
             OUTPUT RPTACT.
        * Open the INACT and RPTACT files
        READ INACT
            AT END
                MOVE 'Y' TO INACT-EOF-SWITCH
        END-READ.
        * Read the first record from INACT
        MOVE HEADER-1 TO OUTFILE-ACTIVE.
        * Move the header-1 line to the output file
        WRITE OUTFILE-ACTIVE.
        * Write the header-1 line to the output file
        MOVE HEADER-ACTIVE TO OUTFILE-ACTIVE.
        * Move the header-active line to the output file
        WRITE OUTFILE-ACTIVE.
        * Write the header-active line to the output file
        MOVE DATE-LINE TO OUTFILE-ACTIVE.
        * Move the date-line line to the output file
        WRITE OUTFILE-ACTIVE.
        * Write the date-line line to the output file
        MOVE SPACES TO OUTFILE-ACTIVE.
        * Move spaces to the output file
        WRITE OUTFILE-ACTIVE.
        * Write spaces to the output file
        MOVE HEADER-3 TO OUTFILE-ACTIVE.
        * Move the header-3 line to the output file
        WRITE OUTFILE-ACTIVE.
        * Write the header-3 line to the output file
        MOVE HEADER-4 TO OUTFILE-ACTIVE.
        * Move the header-4 line to the output file
        WRITE OUTFILE-ACTIVE.
        * Write the header-4 line to the output file
        PERFORM ACTIVE-LOOP
            UNTIL INACT-EOF-SWITCH = 'Y'.
        * Perform the active-loop procedure until the end-of-file switch is 'Y'
        CLOSE INACT
              RPTACT.
        * Close the INACT and RPTACT files

    * Report-spent procedure

    REPORT-SPENT.
        OPEN INPUT INSPN
             OUTPUT RPTSPN.
        * Open the INSPN and RPTSPN files
        READ INSPN
            AT END
                MOVE 'Y' TO INSPN-EOF-SWITCH
        END-READ.
        * Read the first record from INSPN
        MOVE HEADER-1 TO OUTFILE-SPENT.
        * Move the header-1 line to the output file
        WRITE OUTFILE-SPENT.
        * Write the header-1 line to the output file
        MOVE HEADER-SPENT TO OUTFILE-SPENT.
        * Move the header-spent line to the output file
        WRITE OUTFILE-SPENT.
        * Write the header-spent line to the output file
        MOVE DATE-LINE TO OUTFILE-SPENT.
        * Move the date-line line to the output file
        WRITE OUTFILE-SPENT.
        * Write the date-line line to the output file
        MOVE SPACES TO OUTFILE-SPENT.
        * Move spaces to the output file
        WRITE OUTFILE-SPENT.
        * Write spaces to the output file
        MOVE HEADER-3 TO OUTFILE-SPENT