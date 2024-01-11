       IDENTIFICATION DIVISION.
       PROGRAM-ID.  PINVRPT.
      **************************************************************************
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT INALL ASSIGN TO 
           '/home/knallathambi/workspace/cobol_apps/tmp/INALL.dat'
           ORGANIZATION LINE SEQUENTIAL.
           SELECT INACT ASSIGN TO 
           '/home/knallathambi/workspace/cobol_apps/tmp/INACT.dat'
           ORGANIZATION LINE SEQUENTIAL.
           SELECT INSPN ASSIGN TO 
           '/home/knallathambi/workspace/cobol_apps/tmp/INSPN.dat'
           ORGANIZATION LINE SEQUENTIAL.
           SELECT INDES ASSIGN TO 
           '/home/knallathambi/workspace/cobol_apps/tmp/INDES.dat'
           ORGANIZATION LINE SEQUENTIAL.
           SELECT RPTALL ASSIGN TO 
           '/home/knallathambi/workspace/cobol_apps/tmp/RPTALL.dat'
           ORGANIZATION LINE SEQUENTIAL.
           SELECT RPTACT ASSIGN TO 
           '/home/knallathambi/workspace/cobol_apps/tmp/RPTACT.dat'
           ORGANIZATION LINE SEQUENTIAL.
           SELECT RPTSPN ASSIGN TO 
           '/home/knallathambi/workspace/cobol_apps/tmp/RPTSPN.dat'
           ORGANIZATION LINE SEQUENTIAL.
           SELECT RPTDES ASSIGN TO 
           '/home/knallathambi/workspace/cobol_apps/tmp/RPTDES.dat'
           ORGANIZATION LINE SEQUENTIAL.
      **************************************************************************
       DATA DIVISION.
       FILE SECTION.
       FD INALL.
       01  INALL-RECORD-ALL.
           05  GRAIN-SERIAL-ALL             PIC 9(12).
           05  GRAIN-TYPE-ALL               PIC X(10).
           05  GRAIN-FORMULA-ALL            PIC X(15).
           05  GRAIN-STATUS-ALL             PIC X(1).
           05  GRAIN-QA-ALL                 PIC X(4).
           05  GRAIN-QUALITY-ALL            PIC 9(2).
           05  FILLER                       PIC 9(10).
           05  FILLER                       PIC 9(10).
           05  GRAIN-WEIGHT-ALL             PIC 9(10).
           05  FILLER                       PIC X(375).
       FD INACT.
       01  INALL-RECORD-ACT.
           05  GRAIN-SERIAL-ACT             PIC 9(12).
           05  GRAIN-TYPE-ACT               PIC X(10).
           05  GRAIN-FORMULA-ACT            PIC X(15).
           05  GRAIN-STATUS-ACT             PIC X(1).
           05  GRAIN-QA-ACT                 PIC X(4).
           05  GRAIN-QUALITY-ACT            PIC 9(2).
           05  FILLER                       PIC 9(10).
           05  FILLER                       PIC 9(10).
           05  GRAIN-WEIGHT-ACT             PIC 9(10).
           05  FILLER                       PIC X(375).
       FD INSPN.
       01  INALL-RECORD-SPN.
           05  GRAIN-SERIAL-SPN             PIC 9(12).
           05  GRAIN-TYPE-SPN               PIC X(10).
           05  GRAIN-FORMULA-SPN            PIC X(15).
           05  GRAIN-STATUS-SPN             PIC X(1).
           05  GRAIN-QA-SPN                 PIC X(4).
           05  GRAIN-QUALITY-SPN            PIC 9(2).
           05  FILLER                       PIC 9(10).
           05  FILLER                       PIC 9(10).
           05  GRAIN-WEIGHT-SPN             PIC 9(10).
           05  FILLER                       PIC X(375).
       FD INDES.
       01  INALL-RECORD-DES.
           05  GRAIN-SERIAL-DES             PIC 9(12).
           05  GRAIN-TYPE-DES               PIC X(10).
           05  GRAIN-FORMULA-DES            PIC X(15).
           05  GRAIN-STATUS-DES             PIC X(1).
           05  GRAIN-QA-DES                 PIC X(4).
           05  GRAIN-QUALITY-DES            PIC 9(2).
           05  FILLER                       PIC 9(10).
           05  FILLER                       PIC 9(10).
           05  GRAIN-WEIGHT-DES             PIC 9(10).
           05  FILLER                       PIC X(375).
       FD RPTALL.
       01  OUTFILE-ALL                 PIC X(200).
       FD RPTACT.
       01  OUTFILE-ACTIVE              PIC X(200).
       FD RPTSPN.
       01  OUTFILE-SPENT               PIC X(200).
       FD RPTDES.
       01  OUTFILE-DESTROYED           PIC X(200).
      **************************************************************************
       WORKING-STORAGE SECTION.
       01  WS-CURRENT-DATE.
           05  WS-YEAR                 PIC 9(4).
           05  WS-MONTH                PIC 9(2).
           05  WS-DAY                  PIC 9(2).
           05  WS-HOURS                PIC 9(2).
           05  WS-MINUTES              PIC 9(2).
           05  WS-SECONDS              PIC 9(2).
           05  WS-HUND-SECOND          PIC 9(2).
           05  WS-GMT                  PIC X(5).
       01  OUT-RECORD.
           05  SERIAL-OUT              PIC X(12).
           05  FILLER                  PIC X(2)
               VALUE  SPACES.
           05  STATUS-OUT              PIC X(10).
           05  FILLER                  PIC X(2)
               VALUE SPACES.
           05  TYPE-OUT                PIC X(10).
           05  FILLER                  PIC X(2)
               VALUE  SPACES.
           05  FORMULA-OUT             PIC X(15).
           05  FILLER                  PIC X(2)
               VALUE SPACES.
           05  QA-OUT                  PIC X(4).
           05  FILLER                  PIC X(2)
               VALUE SPACES.
           05  WEIGHT-OUT              PIC X(10).
           05  FILLER                  PIC X
               VALUE 'G'.
       01  DATE-LINE.
           05  FILLER                  PIC X(12)
               VALUE 'REPORT DATE:'.
           05  FILLER                  PIC X(1)
               VALUE SPACES.
           05  DT-YEAR                 PIC 9(4).
           05  FILLER                  PIC X
               VALUE '/'.
           05  DT-MONTH                PIC 9(2).
           05  FILLER                  PIC X
               VALUE '/'.
           05  DT-DAY                  PIC 9(2).
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
           05  INACT-EOF-SWITCH         PIC X(1) VALUE 'N'.
           05  INSPN-EOF-SWITCH         PIC X(1) VALUE 'N'.
           05  INDES-EOF-SWITCH         PIC X(1) VALUE 'N'.

       01  WS-COUNTERS.
           05  WS-INACT-COUNT           PIC S9(4) COMP VALUE 0.
           05  WS-INALL-COUNT           PIC S9(4) COMP VALUE 0.
           05  WS-INSPN-COUNT           PIC S9(4) COMP VALUE 0.
           05  WS-INDES-COUNT           PIC S9(4) COMP VALUE 0.
           05  WS-RPTACT-COUNT           PIC S9(4) COMP VALUE 0.
           05  WS-RPTALL-COUNT           PIC S9(4) COMP VALUE 0.
           05  WS-RPTSPN-COUNT           PIC S9(4) COMP VALUE 0.
           05  WS-RPTDES-COUNT           PIC S9(4) COMP VALUE 0.
      **************************************************************************
       PROCEDURE DIVISION.
       MAIN-PROGRAM.
           MOVE FUNCTION CURRENT-DATE TO WS-CURRENT-DATE.
           MOVE WS-YEAR TO DT-YEAR.
           MOVE WS-MONTH TO DT-MONTH.
           MOVE WS-DAY TO DT-DAY.
           PERFORM REPORT-ALL.
           PERFORM REPORT-ACTIVE.
           PERFORM REPORT-SPENT.
           PERFORM REPORT-DESTROYED.
           PERFORM DISPLAY-STATS.
           STOP RUN.
      **************************************************************************
       REPORT-ALL.
           OPEN INPUT INALL
                OUTPUT RPTALL.
           READ INALL
               AT END
                   MOVE 'Y' TO INALL-EOF-SWITCH
           END-READ.
           MOVE HEADER-1 TO OUTFILE-ALL.
           WRITE OUTFILE-ALL.
           MOVE HEADER-ALL TO OUTFILE-ALL.
           WRITE OUTFILE-ALL.
           MOVE DATE-LINE TO OUTFILE-ALL.
           WRITE OUTFILE-ALL.
           MOVE SPACES TO OUTFILE-ALL.
           WRITE OUTFILE-ALL.
           MOVE HEADER-3 TO OUTFILE-ALL.
           WRITE OUTFILE-ALL.
           MOVE HEADER-4 TO OUTFILE-ALL.
           WRITE OUTFILE-ALL.
           PERFORM ALL-LOOP
               UNTIL INALL-EOF-SWITCH = 'Y'.
           CLOSE INALL
                 RPTALL.
      **************************************************************************
       REPORT-ACTIVE.
           OPEN INPUT INACT
                OUTPUT RPTACT.
           READ INACT
               AT END
                   MOVE 'Y' TO INACT-EOF-SWITCH
           END-READ.
           MOVE HEADER-1 TO OUTFILE-ACTIVE.
           WRITE OUTFILE-ACTIVE.
           MOVE HEADER-ACTIVE TO OUTFILE-ACTIVE.
           WRITE OUTFILE-ACTIVE.
           MOVE DATE-LINE TO OUTFILE-ACTIVE.
           WRITE OUTFILE-ACTIVE.
           MOVE SPACES TO OUTFILE-ACTIVE.
           WRITE OUTFILE-ACTIVE.
           MOVE HEADER-3 TO OUTFILE-ACTIVE.
           WRITE OUTFILE-ACTIVE.
           MOVE HEADER-4 TO OUTFILE-ACTIVE.
           WRITE OUTFILE-ACTIVE.
           PERFORM ACTIVE-LOOP
               UNTIL INACT-EOF-SWITCH = 'Y'.
           CLOSE INACT
                 RPTACT.
      **************************************************************************
       REPORT-SPENT.
           OPEN INPUT INSPN
                OUTPUT RPTSPN.
           READ INSPN
               AT END
                   MOVE 'Y' TO INSPN-EOF-SWITCH
           END-READ.
           MOVE HEADER-1 TO OUTFILE-SPENT.
           WRITE OUTFILE-SPENT.
           MOVE HEADER-SPENT TO OUTFILE-SPENT.
           WRITE OUTFILE-SPENT.
           MOVE DATE-LINE TO OUTFILE-SPENT.
           WRITE OUTFILE-SPENT.
           MOVE SPACES TO OUTFILE-SPENT.
           WRITE OUTFILE-SPENT.
           MOVE HEADER-3 TO OUTFILE-SPENT.
           WRITE OUTFILE-SPENT.
           MOVE HEADER-4 TO OUTFILE-SPENT.
           WRITE OUTFILE-SPENT.
           PERFORM SPENT-LOOP
               UNTIL INSPN-EOF-SWITCH = 'Y'.
           CLOSE INSPN
                 RPTSPN.
      **************************************************************************
       REPORT-DESTROYED.
           OPEN INPUT INDES
                OUTPUT RPTDES.
           READ INDES
               AT END
                   MOVE 'Y' TO INDES-EOF-SWITCH
           END-READ.
           MOVE HEADER-1 TO OUTFILE-DESTROYED.
           WRITE OUTFILE-DESTROYED.
           MOVE HEADER-DESTROYED TO OUTFILE-DESTROYED.
           WRITE OUTFILE-DESTROYED.
           MOVE DATE-LINE TO OUTFILE-DESTROYED.
           WRITE OUTFILE-DESTROYED.
           MOVE SPACES TO OUTFILE-DESTROYED.
           WRITE OUTFILE-DESTROYED.
           MOVE HEADER-3 TO OUTFILE-DESTROYED.
           WRITE OUTFILE-DESTROYED.
           MOVE HEADER-4 TO OUTFILE-DESTROYED.
           WRITE OUTFILE-DESTROYED.
           PERFORM DESTROYED-LOOP
               UNTIL INDES-EOF-SWITCH = 'Y'.
           CLOSE INDES
                 RPTDES.
      **************************************************************************
       ALL-LOOP.
           ADD 1 TO WS-INALL-COUNT.
           MOVE GRAIN-SERIAL-ALL TO SERIAL-OUT.           
           IF GRAIN-STATUS-ALL = 0
               MOVE "ACTIVE" TO STATUS-OUT
           ELSE IF GRAIN-STATUS-ALL = 1
               MOVE "SPENT" TO STATUS-OUT
           ELSE IF GRAIN-STATUS-ALL = 3
               MOVE "DESTROYED" TO STATUS-OUT
           ELSE
               MOVE "OTHER" TO STATUS-OUT
           END-IF.
           MOVE GRAIN-TYPE-ALL TO TYPE-OUT.
           MOVE GRAIN-FORMULA-ALL TO FORMULA-OUT.
           MOVE GRAIN-QA-ALL TO QA-OUT.
           MOVE GRAIN-WEIGHT-ALL TO WEIGHT-OUT.
           MOVE OUT-RECORD TO OUTFILE-ALL.
           WRITE OUTFILE-ALL.
           ADD 1 TO WS-RPTALL-COUNT.
           READ INALL
               AT END
                   MOVE 'Y' TO INALL-EOF-SWITCH
           END-READ.
      **************************************************************************
       ACTIVE-LOOP.
           ADD 1 TO WS-INACT-COUNT.
           MOVE GRAIN-SERIAL-ACT TO SERIAL-OUT.
           IF GRAIN-STATUS-ACT = 0
               MOVE "ACTIVE" TO STATUS-OUT
           ELSE IF GRAIN-STATUS-ACT = 1
               MOVE "SPENT" TO STATUS-OUT
           ELSE IF GRAIN-STATUS-ACT = 3
               MOVE "DESTROYED" TO STATUS-OUT
           ELSE
               MOVE "OTHER" TO STATUS-OUT
           END-IF.
           MOVE GRAIN-TYPE-ACT TO TYPE-OUT.
           MOVE GRAIN-FORMULA-ACT TO FORMULA-OUT.
           MOVE GRAIN-QA-ACT TO QA-OUT.
           MOVE GRAIN-WEIGHT-ACT TO WEIGHT-OUT.
           MOVE OUT-RECORD TO OUTFILE-ACTIVE.
           WRITE OUTFILE-ACTIVE.
           ADD 1 TO WS-RPTACT-COUNT.
           READ INACT
               AT END
                   MOVE 'Y' TO INACT-EOF-SWITCH
           END-READ.
      **************************************************************************
       SPENT-LOOP.
           ADD 1 TO WS-INSPN-COUNT.
           MOVE GRAIN-SERIAL-SPN TO SERIAL-OUT.
           IF GRAIN-STATUS-SPN = 0
               MOVE "ACTIVE" TO STATUS-OUT
           ELSE IF GRAIN-STATUS-SPN = 1
               MOVE "SPENT" TO STATUS-OUT
           ELSE IF GRAIN-STATUS-SPN = 3
               MOVE "DESTROYED" TO STATUS-OUT
           ELSE
               MOVE "OTHER" TO STATUS-OUT
           END-IF.
           MOVE GRAIN-TYPE-SPN TO TYPE-OUT.
           MOVE GRAIN-FORMULA-SPN TO FORMULA-OUT.
           MOVE GRAIN-QA-SPN TO QA-OUT.
           MOVE GRAIN-WEIGHT-SPN TO WEIGHT-OUT.
           MOVE OUT-RECORD TO OUTFILE-SPENT.
           WRITE OUTFILE-SPENT.
           ADD 1 TO WS-RPTSPN-COUNT.
           READ INSPN
               AT END
                   MOVE 'Y' TO INSPN-EOF-SWITCH
           END-READ.
      **************************************************************************
       DESTROYED-LOOP.
           ADD 1 TO WS-INDES-COUNT.
           MOVE GRAIN-SERIAL-DES TO SERIAL-OUT.
           IF GRAIN-STATUS-DES = 0
               MOVE "ACTIVE" TO STATUS-OUT
           ELSE IF GRAIN-STATUS-DES = 1
               MOVE "SPENT" TO STATUS-OUT
           ELSE IF GRAIN-STATUS-DES = 3
               MOVE "DESTROYED" TO STATUS-OUT
           ELSE
               MOVE "OTHER" TO STATUS-OUT
           END-IF.
           MOVE GRAIN-TYPE-DES TO TYPE-OUT.
           MOVE GRAIN-FORMULA-DES TO FORMULA-OUT.
           MOVE GRAIN-QA-DES TO QA-OUT.
           MOVE GRAIN-WEIGHT-DES TO WEIGHT-OUT.
           MOVE OUT-RECORD TO OUTFILE-DESTROYED.
           WRITE OUTFILE-DESTROYED.
           ADD 1 TO WS-RPTDES-COUNT.
           READ INDES
               AT END
                   MOVE 'Y' TO INDES-EOF-SWITCH
           END-READ.
      **************************************************************************
       DISPLAY-STATS.
           DISPLAY '********************************************'.
           DISPLAY '**** INPUT FILES ***************************'.
           DISPLAY '*** FILE INALL ROWS = ' WS-INALL-COUNT.
           DISPLAY '*** FILE INACT ROWS = ' WS-INACT-COUNT.
           DISPLAY '*** FILE INSPN ROWS = ' WS-INSPN-COUNT.
           DISPLAY '*** FILE INDES ROWS = ' WS-INDES-COUNT.
           DISPLAY '**** OUTPUT FILES ***************************'.
           DISPLAY '*** FILE RPTALL ROWS = ' WS-RPTALL-COUNT.
           DISPLAY '*** FILE RPTACT ROWS = ' WS-RPTACT-COUNT.
           DISPLAY '*** FILE RPTSPN ROWS = ' WS-RPTSPN-COUNT.
           DISPLAY '*** FILE RPTDES ROWS = ' WS-RPTDES-COUNT.
           DISPLAY '********************************************'.