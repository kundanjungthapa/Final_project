# First time creating a table named 'final_project' in database 'postgres' in myadmin
from estd_connection import estd_connection

cursor = estd_connection()

sql = """
CREATE TABLE INFO(
    TITLE CHAR(4),
    FIRST_NAME CHAR(20),
    LAST_NAME CHAR(20),
    AGE INT,
    NATIONALITY CHAR(20),
    REGISTRATION_STATUS CHAR(20),
    COMLETED_COURSES INT,
    SEMESTERS INT
)
"""

cursor.execute(sql)
print("Table created successfully !" )