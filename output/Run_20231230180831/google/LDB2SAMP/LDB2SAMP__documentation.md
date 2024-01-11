=== COBOL START ===

## IDENTIFICATION DIVISION.

### PROGRAM-ID. LDB2SAMP.

This line specifies the program identifier, which is LDB2SAMP in this case.

## DATA DIVISION.

### WORKING-STORAGE SECTION.

This section defines the working storage area, which is used to store data that is used during the execution of the program.

#### EXEC SQL INCLUDE SQLCA END-EXEC.

This line includes the SQL Communication Area (SQLCA) in the working storage section. The SQLCA is a special area that is used to communicate between the COBOL program and the database management system (DBMS).

#### 01 EMPLOYEE.

This line defines a group item named EMPLOYEE, which is used to store data about an employee.

##### 05 EMPNO PIC X(6).

This line defines an elementary item named EMPNO, which is used to store the employee number. It is a 6-character alphanumeric field.

##### 05 FIRSTNME.

This line defines a group item named FIRSTNME, which is used to store the employee's first name.

###### 49 LEN PIC S9(4) COMP-5.

This line defines an elementary item named LEN, which is used to store the length of the first name. It is a 4-digit packed decimal field.

###### 49 DAT PIC X(12).

This line defines an elementary item named DAT, which is used to store the first name. It is a 12-character alphanumeric field.

##### 05 MIDINIT PIC X(1).

This line defines an elementary item named MIDINIT, which is used to store the employee's middle initial. It is a 1-character alphanumeric field.

##### 05 LASTNAME.

This line defines a group item named LASTNAME, which is used to store the employee's last name.

###### 49 LEN PIC S9(4) COMP-5.

This line defines an elementary item named LEN, which is used to store the length of the last name. It is a 4-digit packed decimal field.

###### 49 DAT PIC X(15).

This line defines an elementary item named DAT, which is used to store the last name. It is a 15-character alphanumeric field.

##### 05 WORKDEPT PIC X(3).

This line defines an elementary item named WORKDEPT, which is used to store the employee's work department. It is a 3-character alphanumeric field.

##### 05 PHONENO PIC X(4).

This line defines an elementary item named PHONENO, which is used to store the employee's phone number. It is a 4-character alphanumeric field.

##### 05 HIREDATE PIC X(10).

This line defines an elementary item named HIREDATE, which is used to store the employee's hire date. It is a 10-character alphanumeric field.

##### 05 JOB PIC X(8).

This line defines an elementary item named JOB, which is used to store the employee's job title. It is an 8-character alphanumeric field.

##### 05 EDLEVEL PIC S9(4) COMP-5.

This line defines an elementary item named EDLEVEL, which is used to store the employee's education level. It is a 4-digit packed decimal field.

##### 05 SEX PIC X(1).

This line defines an elementary item named SEX, which is used to store the employee's sex. It is a 1-character alphanumeric field.

##### 05 BIRTHDATE PIC X(10).

This line defines an elementary item named BIRTHDATE, which is used to store the employee's birth date. It is a 10-character alphanumeric field.

##### 05 SALARY PIC S9(7)V9(2) COMP-3.

This line defines an elementary item named SALARY, which is used to store the employee's salary. It is a 7-digit packed decimal field with 2 decimal places.

##### 05 BONUS PIC S9(7)V9(2) COMP-3.

This line defines an elementary item named BONUS, which is used to store the employee's bonus. It is a 7-digit packed decimal field with 2 decimal places.

##### 05 COMM PIC S9(7)V9(2) COMP-3.

This line defines an elementary item named COMM, which is used to store the employee's commission. It is a 7-digit packed decimal field with 2 decimal places.

#### 01 VARIABLES.

This line defines a group item named VARIABLES, which is used to store various variables that are used during the execution of the program.

##### 02 RECORDCOUNT PIC S9(8) USAGE COMP-3.

This line defines an elementary item named RECORDCOUNT, which is used to store the number of records in the EMPLOYEE table. It is an 8-digit packed decimal field.

##### 02 DISPLAYRC PIC S9(4) USAGE DISPLAY.

This line defines an elementary item named DISPLAYRC, which is used to store the number of records in the EMPLOYEE table in a display format. It is a 4-digit display field.

##### 02 OUT PIC X(200).

This line defines an elementary item named OUT, which is used to store various messages that are displayed to the user. It is a 200-character alphanumeric field.

##### 02 NEXTEMP PIC X(6).

This line defines an elementary item named NEXTEMP, which is used to store the next employee number. It is a 6-character alphanumeric field.

##### 02 NEXTEMPNO PIC 9(6).

This line defines an elementary item named NEXTEMPNO, which is used to store the next employee number in a numeric format. It is a 6-digit numeric field.

##### 02 FIRSTNMEP PIC X(12).

This line defines an elementary item named FIRSTNMEP, which is used to store the first name of the new employee. It is a 12-character alphanumeric field.

##### 02 LASTNAMEP PIC X(15).

This line defines an elementary item named LASTNAMEP, which is used to store the last name of the new employee. It is a 15-character alphanumeric field.

## LINKAGE SECTION.

This section is not used in this program.

## PROCEDURE DIVISION.

This section contains the executable statements of the program.

### MOVE LOW-VALUES TO VARIABLES.

This statement moves low values to all the variables in the VARIABLES group item. This initializes the variables to their default values.

### EXEC SQL SELECT COUNT (*)
###                     INTO :RECORDCOUNT
###                     FROM EMPLOYEE
###                     END-EXEC.

This statement executes an SQL SELECT statement to count the number of records in the EMPLOYEE table. The result of the SELECT statement is stored in the RECORDCOUNT variable.

### IF SQLCODE = 0 THEN
###     MOVE RECORDCOUNT TO DISPLAYRC
###     MOVE "THE NUMBER OF EMPLOYEES IN THE DATABASE IS " TO OUT
###     MOVE DISPLAYRC TO OUT(44:4)
### ELSE IF SQLCODE = 100 THEN
###     MOVE "NO EMPLOYEES FOUND IN DATABASE" TO OUT
### ELSE
###     MOVE "SQL ERROR " TO OUT
###     MOVE SQLCODE TO OUT(11:10)
### END-IF.

This IF statement checks the value of the SQLCODE variable to determine whether the SQL statement executed successfully. If SQLCODE is equal to 0, then the SELECT statement executed successfully and the number of records in the EMPLOYEE table is moved to the DISPLAYRC variable. A message is also moved to the OUT variable to indicate the number of employees in the database. If SQLCODE is equal to 100, then the SELECT statement did not find any records in the EMPLOYEE table. A message is moved to the OUT variable to indicate that no employees were found. If SQLCODE is not equal to 0 or 100, then an SQL error occurred. A message is moved to the OUT variable to indicate that an SQL error occurred and the SQLCODE is moved to the OUT variable.

### DISPLAY OUT.

This statement displays the contents of the OUT variable to the user.

### IF SQLCODE = 0 THEN
###     EXEC SQL SELECT MAX (EMPNO)
###                         INTO :NEXTEMP
###                         FROM EMPLOYEE
###                         END-EXEC

###     MOVE NEXTEMP TO NEXTEMPNO

###     COMPUTE NEXTEMPNO = NEXTEMPNO + 10

###     MOVE NEXTEMPNO TO EMPNO
###     MOVE "FRANK" TO FIRSTNMEP
###     MOVE "JONES" TO LASTNAMEP
###     MOVE "Y" TO MIDINIT
###     MOVE "A00" TO WORKDEPT
###     MOVE "1234" TO PHONENO
###     MOVE "04-30-1979" TO HIREDATE
###     MOVE "Clerk" TO JOB
###     MOVE 15 TO EDLEVEL
###     MOVE "M" TO SEX
###     MOVE "05-30-1954" TO BIRTHDATE
###     MOVE "36170" TO SALARY
###     MOVE "400" TO BONUS
###     MOVE "2387" TO COMM

###     EXEC SQL INSERT INTO EMPLOYEE
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

###     IF SQLCODE = 0 THEN
###        EXEC SQL SELECT *
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

###        EXEC SQL COMMIT END-EXEC

###        MOVE FIRSTNMEP TO OUT
###        MOVE LASTNAMEP TO OUT(14:15)
###        DISPLAY OUT
###        DISPLAY "ADDED TO THE DATABASE"

###     ELSE
###        MOVE "SQL ERROR" TO OUT
###        DISPLAY OUT
###     END-IF

### END-IF.

This IF statement checks the value of the SQLCODE variable to determine whether the SELECT statement executed successfully. If SQLCODE is equal to 0, then the SELECT statement executed successfully and the maximum employee number is moved to the NEXTEMP variable. The NEXTEMP variable is then moved to the NEXTEMPNO variable. The NEXTEMPNO variable is then incremented by 10. The NEXTEMPNO variable is then moved to the EMPNO field of the EMPLOYEE record. The FIRSTNMEP, LASTNAMEP, MIDINIT, WORKDEPT, PHONENO, HIREDATE, JOB, EDLEVEL, SEX, BIRTHDATE, SALARY, BONUS, and COMM fields of the EMPLOYEE record are then set to the appropriate values. An SQL INSERT statement is then executed to insert the new employee record into the EMPLOYEE table. If the INSERT statement executes successfully, then an SQL SELECT statement is executed to retrieve the newly inserted employee record. The retrieved employee record is then displayed to the user. If the INSERT statement does not execute successfully, then an error message is displayed to the user.

### GOBACK.

This statement returns control to the operating system.