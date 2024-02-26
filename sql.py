import sqlite3

## Connect to SQLite
conn = sqlite3.connect("student.db")

## Create a cursor object to insert records, create table and retrieve
cursor = conn.cursor()

## Create Table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Jazay','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('John','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Kevin','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Lorna','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Michele','DEVOPS','A',35)''')

## Disspaly ALl the records

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in databse
conn.commit()
conn.close()