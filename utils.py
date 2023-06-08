# Module 'estd_connection' has been hidden for security purposes using '.gitignore'.
from estd_connection import estd_connection
import csv
cursor = estd_connection()


# Function to insert data in table by establishing connection to the PostgreSQL database.
def insert_into_table(info):
    data = f"""
    INSERT INTO INFO(
        TITLE,
        FIRST_NAME,
        LAST_NAME,
        AGE,
        NATIONALITY,
        REGISTRATION_STATUS,
        COMLETED_COURSES,
        SEMESTERS
    ) 
    VALUES (
        '{info["TITLE"]}',
        '{info["FIRST_NAME"]}',
        '{info["LAST_NAME"]}',
        '{info["AGE"]}',
        '{info["NATIONALITY"]}',
        '{info["REGISTRATION_STATUS"]}',
        '{info["COMLETED_COURSES"]}',
        '{info["SEMESTERS"]}'
    )
    """
    cursor.execute(data)
    print("Data Inserted !!")