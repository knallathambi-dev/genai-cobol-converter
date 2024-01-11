## IDENTIFICATION DIVISION.

### PROGRAM-ID.

- This line specifies the program name as PINVRPT.

## ENVIRONMENT DIVISION.

### INPUT-OUTPUT SECTION.

### FILE-CONTROL.

- This section defines the files used in the program.

- **INALL** is an input file containing records of all grain inventory items.
- **INACT** is an input file containing records of active grain inventory items.
- **INSPN** is an input file containing records of spent grain inventory items.
- **INDES** is an input file containing records of destroyed grain inventory items.
- **RPTALL** is an output file containing a report of all grain inventory items.
- **RPTACT** is an output file containing a report of active grain inventory items.
- **RPTSPN** is an output file containing a report of spent grain inventory items.
- **RPTDES** is an output file containing a report of destroyed grain inventory items.

## DATA DIVISION.

### FILE SECTION.

- This section defines the structure of the files used in the program.

### FD INALL

- This section defines the input file INALL.
- The file is recorded in fixed-length format (RECORDING MODE F).
- The record structure is as follows:

```
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
```

### FD INACT

- This section defines the input file INACT.
- The file is recorded in fixed-length format (RECORDING MODE F).
- The record structure is as follows:

```
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
```

### FD INSPN

- This section defines the input file INSPN.
- The file is recorded in fixed-length format (RECORDING MODE F).
- The record structure is as follows:

```
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
```

### FD INDES

- This section defines the input file INDES.
- The file is recorded in fixed-length format (RECORDING MODE F).
- The record structure is as follows:

```
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
```

### FD RPTALL

- This section defines the output file RPTALL.
- The file is recorded in variable-length format (RECORDING MODE V).
- The record structure is as follows:

```
01  OUTFILE-ALL                 PIC X(200).
```

### FD RPTACT

- This section defines the output file RPTACT.
- The file is recorded in variable-length format (RECORDING MODE V).
- The record structure is as follows:

```
01  OUTFILE-ACTIVE              PIC X(200).
```

### FD RPTSPN

- This section defines the output file RPTSPN.
- The file is recorded in variable-length format (RECORDING MODE V).
- The record structure is as follows:

```
01  OUTFILE-SPENT               PIC X(200).
```

### FD RPTDES

- This section defines the output file RPTDES.
- The file is recorded in variable-length format (RECORDING MODE V).
- The record structure is as follows:

```
01  OUTFILE-DESTROYED           PIC X(200).
```

### WORKING-STORAGE SECTION.

- This section defines the working storage variables used in the program.

### 01  WS-CURRENT-DATE.

- This variable is used to store the current date and time.
- The variable is subdivided as follows:

```
     05  WS-YEAR                 PIC 9(4).
     05  WS-MONTH                PIC 9(2).
     05  WS-DAY                  PIC 9(2).
     05  WS-HOURS                PIC 9(2).
     05  WS-MINUTES              PIC 9(2).
     05  WS-SECONDS              PIC 9(2).
     05  WS-HUND-SECOND          PIC 9(2).
     05  WS-GMT                  PIC X(5).
```

### 01  OUT-RECORD.

- This variable is used to store the output record for the report files.
- The variable is subdivided as follows:

```
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
```

### 01  DATE-LINE.

- This variable is used to store the date line for the report files.
- The variable is subdivided as follows:

```
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
```

### 01  HEADER-1.

- This variable is used to store the first header line for the report files.
- The variable is subdivided as follows:

```
     05  FILLER                  PIC X(100)
         VALUE  'HAYNIE RESEARCH & DEVELOPMENT'.
```

### 01  HEADER-ALL.

- This variable is used to store the header line for the all grain inventory report.
- The variable is subdivided as follows:

```
     05  FILLER                  PIC X(100)
         VALUE  'PROPELLANT GRAIN INVENTORY REPORT - ALL'.
```

### 01  HEADER-ACTIVE.

- This variable is used to store the header line for the active grain inventory report.
- The variable is subdivided as follows:

```
     05  FILLER                  PIC X(100)
         VALUE  'PROPELLANT GRAIN INVENTORY REPORT - ACTIVE'.
```

### 01  HEADER-SPENT.

- This variable is used to store the header line for the spent grain inventory report.
- The variable is subdivided as follows:

```
     05  FILLER                  PIC X(100)
         VALUE  'PROPELLANT GRAIN INVENTORY REPORT - SPENT'.
```

### 01  HEADER-DESTROYED.

- This variable is used to store the header line for the destroyed grain inventory report.
- The variable is subdivided as follows:

```
     05  FILLER                  PIC X(100)
         VALUE  'PROPELLANT GRAIN INVENTORY REPORT - DESTROYED'.
```

### 01  HEADER-3.

- This variable is used to store the third header line for the report files.
- The variable is subdivided as follows:

```
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
```

### 01  HEADER-4.

- This variable is used to store the fourth header line for the report files.
- The variable is subdivided as follows:

```
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
```

### 01  SWITCHES.

- This variable is used to store the end-of-file switches for the input files.
- The variable is subdivided as follows:

```
     05  INALL-EOF-SWITCH         PIC X(1) VALUE 'N'.
     05  INACT-EOF-SWITCH         PIC X(1) VALUE 'N'.
     05  INSPN-EOF-SWITCH         PIC X(1) VALUE 'N'.
     05  INDES-EOF-SWITCH         PIC X(1) VALUE 'N'.
```

### PROCEDURE DIVISION.

- This section contains the executable statements of the program.

### MAIN-PROGRAM.

- This is the main program of the program.
- It calls the report-generating procedures and then stops the program.

### REPORT-ALL.

- This procedure generates the all grain inventory report.
- It opens the input and output files, reads the input file, and writes the output file.

### REPORT-ACTIVE.

- This procedure generates the active grain inventory report.
- It opens the input and output files, reads the input file, and writes the output file.

### REPORT-SPENT.

- This procedure generates the spent grain inventory report.
- It opens the input and output files, reads the input file, and writes the output file.

### REPORT-DESTROYED.

- This procedure generates the destroyed grain inventory report.
- It opens the input and output files, reads the input file, and writes the output file.

### ALL-LOOP.

- This loop is used to read the input file and write the output file for the all grain inventory report.

### ACTIVE-LOOP.

- This loop is used to read the input file and write the output file for the active grain inventory report.

### SPENT-LOOP.

- This loop is used to read the input file and write the output file for the spent grain inventory report.

### DESTROYED-LOOP.

- This loop is used to read the input file and write the output file for the destroyed grain inventory report.