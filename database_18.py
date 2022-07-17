#connecting database with python

import mysql.connector
conn = mysql.connector.connect(
    user = "root",
    password = "rawgoosh129",
    host = "localhost",
    database = "test"
)
mycursor = conn.cursor()

#creating table using python
"""
mycursor.execute("create table student(roll int primary key, name varchar(50),dob datetime, address(30));")
"""

#inserting data using python
"""
mycursor.execute("insert into employee(id,name,dob,address)values(2,'guy','2000-01-02','Leaf');")
conn.commit()
"""

mycursor.execute("delete from employee where id = 2;")
conn.commit()
#displaying data using python
mycursor.execute("select * from employee")
print(mycursor.fetchall())


