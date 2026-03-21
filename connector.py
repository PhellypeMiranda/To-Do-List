import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="21101992",
    database="to_do_list"
)


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tasks")
tasks = mycursor.fetchall()
for x in tasks:
    print(x)

print(type(tasks))