import sqlite3

## Connect to sqlite

connection = sqlite3.connect("student.db")

## Create a cursor  object to insert record,create table, retrieve 
cursor = connection.cursor()

## create a table
table_info = """create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);"""

cursor.execute(table_info)

## Insert Some more records into database

cursor.execute('''INSERT INTO STUDENT VALUES ('Ambkeshwar', 'Data Science', 'A',100)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Pramod', 'Data Science', 'B',90)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Ganesh', 'Devops', 'C',80)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Vidhi', 'Devops', 'C',70)''') 

## Display all the records
print("The inserted records are:")

data = cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)

## Close the connection
    
connection.commit()
connection.close()
 