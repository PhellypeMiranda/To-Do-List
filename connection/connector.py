import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self._host = host
        self._user = user
        self.__password = password
        self._database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
           self.connection = mysql.connector.connect(
                host=self._host,
                user=self._user,
                passwd=self.__password,
                database=self._database
            )
           self.cursor = self.connection.cursor()
        except mysql.connector.Error:
            input("Impossible to connect to the database, press enter to continue offline")

    def save_task_in_db(self):
        self.cursor.execute("INSERT INTO tasks () VALUES ( %s, %s, %s, %s, %s, %s, %s)",)

mydb = Database(host="localhost", user="root", password="21101992", database="to_do_list")
mydb.connect()
mycursor = mydb.cursor()
print(mydb)