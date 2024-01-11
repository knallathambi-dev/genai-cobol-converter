import sqlalchemy as sa

engine = sa.create_engine("oracle://username:password@host:port/sid")


def main():
    with engine.connect() as conn:
        # Get the number of employees in the database
        result = conn.execute("SELECT COUNT(*) FROM EMPLOYEE")
        record_count = result.fetchone()[0]

        # Display the number of employees
        print("THE NUMBER OF EMPLOYEES IN THE DATABASE IS", record_count)

        # If there are no employees, display a message
        if record_count == 0:
            print("NO EMPLOYEES FOUND IN DATABASE")
            return

        # Get the next employee number
        result = conn.execute("SELECT MAX(EMPNO) FROM EMPLOYEE")
        next_empno = result.fetchone()[0] + 10

        # Insert a new employee into the database
        conn.execute(
            "INSERT INTO EMPLOYEE "
            "(EMPNO, FIRSTNME, MIDINIT, LASTNAME, WORKDEPT, PHONENO, HIREDATE, JOB, EDLEVEL, SEX, BIRTHDATE, SALARY, BONUS, COMM) "
            "VALUES (:empno, :firstnme, :midinit, :lastname, :workdept, :phoneno, :hiredate, :job, :edlevel, :sex, :birthdate, :salary, :bonus, :comm)",
            {
                "empno": next_empno,
                "firstnme": "FRANK",
                "midinit": "Y",
                "lastname": "JONES",
                "workdept": "A00",
                "phoneno": "1234",
                "hiredate": "04-30-1979",
                "job": "Clerk",
                "edlevel": 15,
                "sex": "M",
                "birthdate": "05-30-1954",
                "salary": 36170,
                "bonus": 400,
                "comm": 2387,
            },
        )

        # Commit the changes
        conn.commit()

        # Select the newly inserted employee from the database
        result = conn.execute(
            "SELECT * FROM EMPLOYEE WHERE EMPNO = :empno", {"empno": next_empno}
        )

        # Display the newly inserted employee
        employee = result.fetchone()
        print(f"{employee.FIRSTNME} {employee.LASTNAME} ADDED TO THE DATABASE")


if __name__ == "__main__":
    main()
