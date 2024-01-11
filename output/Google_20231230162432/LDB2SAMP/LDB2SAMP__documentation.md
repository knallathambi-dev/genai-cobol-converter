=== COBOL START ===

## IDENTIFICATION DIVISION.

### PROGRAM-ID. LDB2SAMP.

This line specifies the program name as LDB2SAMP.

## DATA DIVISION.

### WORKING-STORAGE SECTION.

#### EXEC SQL INCLUDE SQLCA END-EXEC.

This line includes the SQL Communication Area (SQLCA) in the program. The SQLCA is a special area that is used to communicate between a COBOL program and a database management system (DBMS).

#### 01 EMPLOYEE.

This line defines a group of data items that represent an employee record.

##### 05 EMPNO PIC X(6).

This line defines a 6-character field named EMPNO to store the employee number.

##### 05 FIRSTNME.

This line defines a group of data items that represent the employee's first name.

###### 49 LEN PIC S9(4) COMP-5.

This line defines a 4-character field named LEN to store the length of the first name.

###### 49 DAT PIC X(12).

This line defines a 12-character field named DAT to store the first name.

##### 05 MIDINIT PIC X(1).

This line defines a 1-character field named MIDINIT to store the employee's middle initial.

##### 05 LASTNAME.

This line defines a group of data items that represent the employee's last name.

###### 49 LEN PIC S9(4) COMP-5.

This line defines a 4-character field named LEN to store the length of the last name.

###### 49 DAT PIC X(15).

This line defines a 15-character field named DAT to store the last name.

##### 05 WORKDEPT PIC X(3).

This line defines a 3-character field named WORKDEPT to store the employee's department.

##### 05 PHONENO PIC X(4).

This line defines a 4-character field named PHONENO to store the employee's phone number.

##### 05 HIREDATE PIC X(10).

This line defines a 10-character field named HIREDATE to store the employee's hire date.

##### 05 JOB PIC X(8).

This line defines an 8-character field named JOB to store the employee's job title.

##### 05 EDLEVEL PIC S9(4) COMP-5.

This line defines a 4-character field named EDLEVEL to store the employee's education level.

##### 05 SEX PIC X(1).

This line defines a 1-character field named SEX to store the employee's sex.

##### 05 BIRTHDATE PIC X(10).

This line defines a 10-character field named BIRTHDATE to store the employee's birth date.

##### 05 SALARY PIC S9(7)V9(2) COMP-3.

This line defines a 7-character field named SALARY to store the employee's salary.

##### 05 BONUS PIC S9(7)V9(2) COMP-3.

This line defines a 7-character field named BONUS to store the employee's bonus.

##### 05 COMM PIC S9(7)V9(2) COMP-3.

This line defines a 7-character field named COMM to store the employee's commission.

#### 01 VARIABLES.

This line defines a group of data items that are used to store various values during the execution of the program.

##### 02 RECORDCOUNT PIC S9(8) USAGE COMP-3.

This line defines an 8-character field named RECORDCOUNT to store the number of records in the EMPLOYEE table.

##### 02 DISPLAYRC PIC S9(4) USAGE DISPLAY.

This line defines a 4-character field named DISPLAYRC to store the number of records in the EMPLOYEE table in a display format.

##### 02 OUT PIC X(200).

This line defines a 200-character field named OUT to store various messages.

##### 02 NEXTEMP PIC X(6).

This line defines a 6-character field named NEXTEMP to store the next employee number.

##### 02 NEXTEMPNO PIC 9(6).

This line defines a 6-character field named NEXTEMPNO to store the next employee number in a numeric format.

##### 02 FIRSTNMEP PIC X(12).

This line defines a 12-character field named FIRSTNMEP to store the first name of the new employee.

##### 02 LASTNAMEP PIC X(15).

This line defines a 15-character field named LASTNAMEP to store the last name of the new employee.

## LINKAGE SECTION.

This section is not used in this program.

## PROCEDURE DIVISION.

### MOVE LOW-VALUES TO VARIABLES.

This line initializes all the data items in the VARIABLES group to their lowest possible values.

### EXEC SQL SELECT COUNT (*)
###                     INTO :RECORDCOUNT
###                     FROM EMPLOYEE
###                     END-EXEC.

This line executes an SQL SELECT statement to count the number of records in the EMPLOYEE table. The result of the SELECT statement is stored in the RECORDCOUNT data item.

### IF SQLCODE = 0 THEN
###         MOVE RECORDCOUNT TO DISPLAYRC
###         MOVE "THE NUMBER OF EMPLOYEES IN THE DATABASE IS " TO OUT
###         MOVE DISPLAYRC TO OUT(44:4)
###     ELSE IF SQLCODE = 100 THEN
###         MOVE "NO EMPLOYEES FOUND IN DATABASE" TO OUT
###     ELSE
###         MOVE "SQL ERROR " TO OUT
###         MOVE SQLCODE TO OUT(11:10)
###     END-IF.

This IF statement checks the value of the SQLCODE special register. If SQLCODE is equal to 0, it means that the SQL statement executed successfully. In this case, the program moves the value of RECORDCOUNT to DISPLAYRC, moves a message to OUT, and moves the value of DISPLAYRC to the end of the message. If SQLCODE is equal to 100, it means that no records were found in the EMPLOYEE table. In this case, the program moves a message to OUT. Otherwise, the program moves an error message to OUT and moves the value of SQLCODE to the end of the message.

### DISPLAY OUT.

This line displays the contents of the OUT data item on the console.

### IF SQLCODE = 0 THEN
###         EXEC SQL SELECT MAX (EMPNO)
###                         INTO :NEXTEMP
###                         FROM EMPLOYEE
###                         END-EXEC

###         MOVE NEXTEMP TO NEXTEMPNO

###         COMPUTE NEXTEMPNO = NEXTEMPNO + 10

###         MOVE NEXTEMPNO TO EMPNO
###         MOVE "FRANK" TO FIRSTNMEP
###         MOVE "JONES" TO LASTNAMEP
###         MOVE "Y" TO MIDINIT
###         MOVE "A00" TO WORKDEPT
###         MOVE "1234" TO PHONENO
###         MOVE "04-30-1979" TO HIREDATE
###         MOVE "Clerk" TO JOB
###         MOVE 15 TO EDLEVEL
###         MOVE "M" TO SEX
###         MOVE "05-30-1954" TO BIRTHDATE
###         MOVE "36170" TO SALARY
###         MOVE "400" TO BONUS
###         MOVE "2387" TO COMM

###         EXEC SQL INSERT INTO EMPLOYEE
###                         VALUES(:EMPNO,
###                                :FIRSTNMEP,
###                                :MIDINIT,
###                                :LASTNAMEP,
###                                :WORKDEPT,
###                                :PHONENO,
###                                :HIREDATE,
###                                :JOB,
###                                :EDLEVEL,
###                                :SEX,
###                                :BIRTHDATE,
###                                :SALARY,
###                                :BONUS,
###                                :COMM)
###                         END-EXEC

###         IF SQLCODE = 0 THEN
###            EXEC SQL SELECT *
###                     INTO :EMPNO,
###                          :FIRSTNME,
###                          :MIDINIT,
###                          :LASTNAME,
###                          :WORKDEPT,
###                          :PHONENO,
###                          :HIREDATE,
###                          :JOB,
###                          :EDLEVEL,
###                          :SEX,
###                          :BIRTHDATE,
###                          :SALARY,
###                          :BONUS,
###                          :COMM
###                     FROM EMPLOYEE
###                     WHERE EMPNO = :EMPNO
###                     END-EXEC

###            EXEC SQL COMMIT END-EXEC

###            MOVE FIRSTNMEP TO OUT
###            MOVE LASTNAMEP TO OUT(14:15)
###            DISPLAY OUT
###            DISPLAY "ADDED TO THE DATABASE"

###         ELSE
###            MOVE "SQL ERROR" TO OUT
###            DISPLAY OUT
###         END-IF

###     END-IF.

This IF statement checks the value of the SQLCODE special register again. If SQLCODE is equal to 0, it means that the previous SQL statement executed successfully. In this case, the program retrieves the maximum value of the EMPNO column from the EMPLOYEE table, calculates the next employee number, and moves the next employee number to the EMPNO data item. The program then moves various values to other data items to create a new employee record. The program then executes an SQL INSERT statement to insert the new employee record into the EMPLOYEE table. If the INSERT statement executes successfully, the program retrieves the newly inserted employee record and displays it on the console. Otherwise, the program displays an error message.

### GOBACK.

This line is used to return control to the operating system.

=== COBOL END ===