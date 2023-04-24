This is Pytest test suite for AdventureWorks2012 database testing.
The suite contains 6 test cases for testing database tables:

-[Person].[Address]
-[Production].[Document]
-[Production].[UnitMeasure]

Test cases themself are described in test_description.txt

To start test suite running please follow the steps:

0. Install Python 3
1. Install pip
2. Install additional libraries using pip:
    pip install pytest
    pip install pyodbc
    pip install pytest-html
3. Provide user credentials for database connection in def db_conn() function in test_cases.py file
   Note: user should have permissions to select [Person] and [Production] schemes
   Verify database host and port, change them in def db_conn() function in test_cases.py if needed
4. Run test suite using command:
    pytest --html=report.html
5. Find test result report in report.html file (open in browser)