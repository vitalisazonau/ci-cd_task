import pymssql
import pytest


@pytest.fixture(scope='session')           # Please verify database credentials
def db_conn():
    server = 'localhost'
    database = 'AdventureWorks2012'
    username = 'TestUser'
    password = 'dqe9_4!t1'
    conn = pymssql.connect(server=server, user=username, password=password, database=database)
    yield conn
    conn.close()


def test_1_sum_of_column_values(db_conn):
    """" Test Case #1: [Person].[Address] table has sum of StateProvinceID column values as expected """
    cursor = db_conn.cursor()
    cursor.execute('SELECT SUM(StateProvinceID) FROM [Person].[Address]')
    actual_result = cursor.fetchone()[0]
    expected_result = 966669
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result} instead"
    cursor.close()


def test_2_not_null_addressline1(db_conn):
    """" Test Case #2: [Person].[Address] table has not NULL values in AddressLine1 column """
    cursor = db_conn.cursor()
    cursor.execute('SELECT AddressID FROM [Person].[Address] WHERE AddressLine1 IS NULL')
    actual_result = cursor.fetchone()
    assert actual_result is None, f"Expected None, but got {actual_result} instead"
    cursor.close()


def test_3_values_in_range_of_list(db_conn):
    """" Test Case #3: [Production].[Document] table has DocumentLevel column values in range of list [0, 1, 2] """
    cursor = db_conn.cursor()
    cursor.execute('SELECT DocumentNode, DocumentLevel FROM [Production].[Document] \
                    WHERE DocumentLevel NOT IN (0, 1, 2);')
    actual_result = cursor.fetchone()
    assert actual_result is None, f"Expected None, but got {actual_result} instead"
    cursor.close()


def test_4_max_value_of_column_owner(db_conn):
    """" Test Case #4: [Production].[Document] table has MAX value of Owner column values as expected"""
    cursor = db_conn.cursor()
    cursor.execute('SELECT MAX(Owner) FROM [Production].[Document]')
    actual_result = cursor.fetchone()[0]
    expected_result = 220
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result} instead"
    cursor.close()


def test_5_count_of_table_rows(db_conn):
    """" Test Case #5: Count of rows of [Production].[UnitMeasure] table is as expected"""
    cursor = db_conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM [Production].[UnitMeasure]')
    actual_result = cursor.fetchone()[0]
    expected_result = 38
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result} instead"
    cursor.close()


def test_6_uniqueness_of_unitmeasurecode(db_conn):
    """" Test Case #6: UnitMeasureCode column of [Production].[UnitMeasure] table contains unique values  """
    cursor = db_conn.cursor()
    cursor.execute('SELECT UnitMeasureCode, COUNT(*) FROM [Production].[UnitMeasure] \
                    GROUP BY UnitMeasureCode HAVING COUNT(*) > 1')
    actual_result = cursor.fetchone()
    assert actual_result is None, f"Expected None, but got {actual_result} instead"
    cursor.close()

#####