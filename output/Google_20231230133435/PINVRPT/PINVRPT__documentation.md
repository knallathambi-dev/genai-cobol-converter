```
IDENTIFICATION DIVISION.
```
This division identifies the program and provides information about the program's purpose and author.

```
PROGRAM-ID.  PINVRPT.
```
This line specifies the program name as PINVRPT.

```
ENVIRONMENT DIVISION.
```
This division defines the computer environment in which the program will run.

```
INPUT-OUTPUT SECTION.
```
This section defines the files that the program will use for input and output.

```
FILE-CONTROL.
```
This section contains the file control statements that define the files that the program will use.

```
SELECT INALL ASSIGN TO PINV.
```
This statement assigns the file named PINV to the file named INALL.

```
SELECT INACT ASSIGN TO PACT.
```
This statement assigns the file named PACT to the file named INACT.

```
SELECT INSPN ASSIGN TO PSPN.
```
This statement assigns the file named PSPN to the file named INSPN.

```
SELECT INDES ASSIGN TO PDES.
```
This statement assigns the file named PDES to the file named INDES.

```
SELECT RPTALL ASSIGN TO RPTALL.
```
This statement assigns the file named RPTALL to the file named RPTALL.

```
SELECT RPTACT ASSIGN TO RPTACT.
```
This statement assigns the file named RPTACT to the file named RPTACT.

```
SELECT RPTSPN ASSIGN TO RPTSPN.
```
This statement assigns the file named RPTSPN to the file named RPTSPN.

```
SELECT RPTDES ASSIGN TO RPTDES.
```
This statement assigns the file named RPTDES to the file named RPTDES.

```
DATA DIVISION.
```
This division defines the data that the program will use.

```
FILE SECTION.
```
This section defines the files that the program will use.

```
FD INALL
```
This statement defines the file named INALL.

```
RECORDING MODE F.
```
This statement specifies that the file is a fixed-length file.

```
01  INALL-RECORD-ALL.
```
This statement defines the record layout for the INALL file.

```
05  GRAIN-SERIAL-ALL             PIC 9(12).
```
This statement defines a field named GRAIN-SERIAL-ALL, which is a 12-digit numeric field.

```
05  GRAIN-TYPE-ALL               PIC X(10).
```
This statement defines a field named GRAIN-TYPE-ALL, which is a 10-character alphanumeric field.

```
05  GRAIN-FORMULA-ALL            PIC X(15).
```
This statement defines a field named GRAIN-FORMULA-ALL, which is a 15-character alphanumeric field.

```
05  GRAIN-STATUS-ALL             PIC X(1).
```
This statement defines a field named GRAIN-STATUS-ALL, which is a 1-character alphanumeric field.

```
05  GRAIN-QA-ALL                 PIC X(4).
```
This statement defines a field named GRAIN-QA-ALL, which is a 4-character alphanumeric field.

```
05  GRAIN-QUALITY-ALL            PIC 9(2).
```
This statement defines a field named GRAIN-QUALITY-ALL, which is a 2-digit numeric field.

```
05  FILLER                       PIC 9(10).
```
This statement defines a filler field that is 10 digits long.

```
05  FILLER                       PIC 9(10).
```
This statement defines a filler field that is 10 digits long.

```
05  GRAIN-WEIGHT-ALL             PIC 9(10).
```
This statement defines a field named GRAIN-WEIGHT-ALL, which is a 10-digit numeric field.

```
05  FILLER                       PIC X(375).
```
This statement defines a filler field that is 375 characters long.

```
FD INACT
```
This statement defines the file named INACT.

```
RECORDING MODE F.
```
This statement specifies that the file is a fixed-length file.

```
01  INALL-RECORD-ACT.
```
This statement defines the record layout for the INACT file.

```
05  GRAIN-SERIAL-ACT             PIC 9(12).
```
This statement defines a field named GRAIN-SERIAL-ACT, which is a 12-digit numeric field.

```
05  GRAIN-TYPE-ACT               PIC X(10).
```
This statement defines a field named GRAIN-TYPE-ACT, which is a 10-character alphanumeric field.

```
05  GRAIN-FORMULA-ACT            PIC X(15).
```
This statement defines a field named GRAIN-FORMULA-ACT, which is a 15-character alphanumeric field.

```
05  GRAIN-STATUS-ACT             PIC X(1).
```
This statement defines a field named GRAIN-STATUS-ACT, which is a 1-character alphanumeric field.

```
05  GRAIN-QA-ACT                 PIC X(4).
```
This statement defines a field named GRAIN-QA-ACT, which is a 4-character alphanumeric field.

```
05  GRAIN-QUALITY-ACT            PIC 9(2).
```
This statement defines a field named GRAIN-QUALITY-ACT, which is a 2-digit numeric field.

```
05  FILLER                       PIC 9(10).
```
This statement defines a filler field that is 10 digits long.

```
05  FILLER                       PIC 9(10).
```
This statement defines a filler field that is 10 digits long.

```
05  GRAIN-WEIGHT-ACT             PIC 9(10).
```
This statement defines a field named GRAIN-WEIGHT-ACT, which is a 10-digit numeric field.

```
05  FILLER                       PIC X(375).
```
This statement defines a filler field that is 375 characters long.

```
FD INSPN
```
This statement defines the file named INSPN.

```
RECORDING MODE F.
```
This statement specifies that the file is a fixed-length file.

```
01  INALL-RECORD-SPN.
```
This statement defines the record layout for the INSPN file.

```
05  GRAIN-SERIAL-SPN             PIC 9(12).
```
This statement defines a field named GRAIN-SERIAL-SPN, which is a 12-digit numeric field.

```
05  GRAIN-TYPE-SPN               PIC X(10).
```
This statement defines a field named GRAIN-TYPE-SPN, which is a 10-character alphanumeric field.

```
05  GRAIN-FORMULA-SPN            PIC X(15).
```
This statement defines a field named GRAIN-FORMULA-SPN, which is a 15-character alphanumeric field.

```
05  GRAIN-STATUS-SPN             PIC X(1).
```
This statement defines a field named GRAIN-STATUS-SPN, which is a 1-character alphanumeric field.

```
05  GRAIN-QA-SPN                 PIC X(4).
```
This statement defines a field named GRAIN-QA-SPN, which is a 4-character alphanumeric field.

```
05  GRAIN-QUALITY-SPN            PIC 9(2).
```
This statement defines a field named GRAIN-QUALITY-SPN, which is a 2-digit numeric field.

```
05  FILLER                       PIC 9(10).
```
This statement defines a filler field that is 10 digits long.

```
05  FILLER                       PIC 9(10).
```
This statement defines a filler field that is 10 digits long.

```
05  GRAIN-WEIGHT-SPN             PIC 9(10).
```
This statement defines a field named GRAIN-WEIGHT-SPN, which is a 10-digit numeric field.

```
05  FILLER                       PIC X(375).
```
This statement defines a filler field that is 375 characters long.

```
FD INDES
```
This statement defines the file named INDES.

```
RECORDING MODE F.
```
This statement specifies that the file is a fixed-length file.

```
01  INALL-RECORD-DES.
```
This statement defines the record layout for the INDES file.

```
05  GRAIN-SERIAL-DES             PIC 9(12).
```
This statement defines a field named GRAIN-SERIAL-DES, which is a 12-digit numeric field.

```
05  GRAIN-TYPE-DES               PIC X(10).
```
This statement defines a field named GRAIN-TYPE-DES, which is a 10-character alphanumeric field.

```
05  GRAIN-FORMULA-DES            PIC X(15).
```
This statement defines a field named GRAIN-FORMULA-DES, which is a 15-character alphanumeric field.

```
05  GRAIN-STATUS-DES             PIC X(1).
```
This statement defines a field named GRAIN-STATUS-DES, which is a 1-character alphanumeric field.

```
05  GRAIN-QA-DES                 PIC X(4).
```
This statement defines a field named GRAIN-QA-DES, which is a 4-character alphanumeric field.

```
05  GRAIN-QUALITY-DES            PIC 9(2).
```
This statement defines a field named GRAIN-QUALITY-DES, which is a 2-digit numeric field.

```
05  FILLER                       PIC 9(10).
```
This statement defines a filler field that is 10 digits long.

```
05  FILLER                       PIC 9(10).
```
This statement defines a filler field that is 10 digits long.

```
05  GRAIN-WEIGHT-DES             PIC 9(10).
```
This statement defines a field named GRAIN-WEIGHT-DES, which is a 10-digit numeric field.

```
05  FILLER                       PIC X(375).
```
This statement defines a filler field that is 375 characters long.

```
FD RPTALL
```
This statement defines the file named RPTALL.

```
RECORDING MODE V.
```
This statement specifies that the file is a variable-length file.

```
01  OUTFILE-ALL                 PIC X(200).
```
This statement defines the record layout for the RPTALL file.

```
FD RPTACT
```
This statement defines the file named RPTACT.

```
RECORDING MODE V.
```
This statement specifies that the file is a variable-length file.

```
01  OUTFILE-ACTIVE              PIC X(200).
```
This statement defines the record layout for the RPTACT file.

```
FD RPTSPN
```
This statement defines the file named RPTSPN.

```
RECORDING MODE V.
```
This statement specifies that the file is a variable-length file.

```
01  OUTFILE-SPENT               PIC X(200).
```
This statement defines the record layout for the RPTSPN file.

```
FD RPTDES
```
This statement defines the file named RPTDES.

```
RECORDING MODE V.
```
This statement specifies that the file is a variable-length file.

```
01  OUTFILE-DESTROYED           PIC X(200).
```
This statement defines the record layout for the RPTDES file.

```
WORKING-STORAGE SECTION.
```
This section contains the working-storage variables.

```
01  WS-CURRENT-DATE.
```
This variable contains the current date and time.

```
05  WS-YEAR                 PIC 9(4).
```
This field contains the year.

```
05  WS-MONTH                PIC 9(2).
```
This field contains the month.

```
05  WS-DAY                  PIC 9(2).
```
This field contains the day.

```
05  WS-HOURS                PIC 9(2).
```
This field contains the hours.

```
05  WS-MINUTES              PIC 9(2).
```
This field contains the minutes.

```
05  WS-SECONDS              PIC 9(2).
```
This field contains the seconds.

```
05  WS-HUND-SECOND          PIC 9(2).
```
This field contains the hundredths of a second.

```
05  WS-GMT                  PIC X(5).
```
This field contains the Greenwich Mean Time (GMT) offset.

```
01  OUT-RECORD.
```
This variable contains the output record.

```
05  SERIAL-OUT              PIC X(12).
```
This field contains the grain serial number.

```
05  FILLER                  PIC X(2)
         VALUE  SPACES.
```
This filler field contains two spaces.

```
05  STATUS-OUT              PIC X(10).
```
This field contains the grain status.

```
05  FILLER                  PIC X(2)
         VALUE SPACES.
```
This filler field contains two spaces.

```
05  TYPE-OUT                PIC X(10).
```
This field contains the grain type.

```
05  FILLER                  PIC X(2)
         VALUE  SPACES.
```
This filler field contains two spaces.

```
05  FORMULA-OUT             PIC X(15).
```
This field contains the grain formula.

```
05  FILLER                  PIC X(2)
         VALUE SPACES.
```
This filler field contains two spaces.

```
05  QA-OUT                  PIC X(4).
```
This field contains the grain QA code.

```
05  FILLER                  PIC X(2)
         VALUE SPACES.
```
This filler field contains two spaces.

```
05  WEIGHT-OUT              PIC X(10).
```
This field contains the grain weight.

```
05  FILLER                  PIC X
         VALUE 'G'.
```
This filler field contains the letter 'G'.

```
01  DATE-LINE.
```
This variable contains the date line.

```
05  FILLER                  PIC X(12)
         VALUE 'REPORT DATE:'.
```
This filler field contains the text 'REPORT DATE:'.

```
05  FILLER                  PIC X(1)
         VALUE SPACES.
```
This filler field contains a space.

```
05  DT-YEAR                 PIC 9(4).
```
This field contains the year.

```
05  FILLER                  PIC X
         VALUE '/'.
```
This filler field contains a slash (/).

```
05  DT-MONTH                PIC 9(2).
```
This field contains the month.

```
05  FILLER                  PIC X
         VALUE '/'.
```
This filler field contains a slash (/).

```
05  DT-DAY                  PIC 9(2).
```
This field contains the day.

```
01  HEADER-1.
```
This variable contains the first header line.

```
05  FILLER                  PIC X(100)
         VALUE  'HAYNIE RESEARCH & DEVELOPMENT'.
```
This filler field contains the text 'HAYNIE RESEARCH & DEVELOPMENT'.

```
01  HEADER-ALL.
```
This variable contains the header line for the all grain report.

```
05  FILLER                  PIC X(100)
         VALUE  'PROPELLANT GRAIN INVENTORY REPORT - ALL'.
```
This filler field contains the text 'PROPELLANT GRAIN INVENTORY REPORT - ALL'.

```
01  HEADER-ACTIVE.
```
This variable contains the header line for the active grain report.

```
05  FILLER                  PIC X(100)
         VALUE  'PROPELLANT GRAIN INVENTORY REPORT - ACTIVE'.
```
This filler field contains the text 'PROPELLANT GRAIN INVENTORY REPORT - ACTIVE'.

```
01  HEADER-SPENT.
```
This variable contains the header line for the spent grain report.

```
05  FILLER                  PIC X(100)
         VALUE  'PROPELLANT GRAIN INVENTORY REPORT - SPENT'.
```
This filler field contains the text 'PROPELLANT GRAIN INVENTORY REPORT - SPENT'.

```
01  HEADER-DESTROYED.
```
This variable contains the header line for the destroyed grain report.

```
05  FILLER                  PIC X(100)
         VALUE  'PROPELLANT GRAIN INVENTORY REPORT - DESTROYED'.
```
This filler field contains the text 'PROPELLANT GRAIN INVENTORY REPORT - DESTROYED'.

```
01  HEADER-3.
```
This variable contains the third header line.

```
05  FILLER                  PIC X(14)
         VALUE  'SERIAL'.
```
This filler field contains the text 'SERIAL'.

```
05  FILLER                  PIC X(12)
         VALUE  'STATUS'.
```
This filler field contains the text 'STATUS'.

```
05  FILLER                  PIC X(12)
         VALUE  'TYPE'.
```
This filler field contains the text 'TYPE'.

```
05  FILLER                  PIC X(17