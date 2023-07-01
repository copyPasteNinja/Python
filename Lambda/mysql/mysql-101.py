import mysql.connector


db_connection = mysql.connector.connect(
  	host="localhost",
  	user="root",
  	passwd="iefwog8iuPbaj;",
    auth_plugin='mysql_native_password'
    )


# # creating database_cursor to perform SQL operation
# db_cursor = db_connection.cursor()
# # executing cursor with execute method and pass SQL query
# db_cursor.execute("CREATE DATABASE elginexpress")
# # get list of all databases
# db_cursor.execute("SHOW DATABASES")
# #print all databases
# for db in db_cursor:
# 	print(db)

def create_tb(database, tableName):
    db_cursor = db_connection.cursor()
    #Here creating database table as student'
    db_cursor.execute("USE %s" % database)
    db_cursor.execute("""CREATE TABLE %s 
        (
            licenseid VARCHAR(20) NOT NULL PRIMARY KEY,
            unit INT, 
            name VARCHAR(255),
            owner VARCHAR(5),
            address VARCHAR(255),
            email VARCHAR(50),
            phone VARCHAR(11)
        )""" % tableName
    )
    #Get database table'
    db_cursor.execute("SHOW TABLES")
    for db in db_cursor:
        print(db)

# create_tb(database="elginexpress", tableName="drivers")


def delete_tb(database, tableName):
    db_cursor = db_connection.cursor()
    #Here creating database table as student'
    db_cursor.execute("USE %s" % database)
    db_cursor.execute("DROP TABLE %s" % tableName)
    print("Tables: " + db_cursor.execute("SHOW TABLES"))
# delete_tb(database="elginexpress", tableName="drivers")


def get_tables(database):
    db_cursor = db_connection.cursor()
    db_cursor.execute("USE %s" % database)
    db_cursor.execute("SHOW TABLES")
    for db in db_cursor:
        print(db)
# get_tables(database="elginexpress")

def insert_data(**kwargs):
    db_cursor = db_connection.cursor()
    db_cursor.execute("USE elginexpress")
    student_sql_query = """INSERT INTO 
        drivers(licenseid,unit,name,owner,address,email,phone) 
        VALUES('ID2387654', 116, 'Zhapar Uluu', 'True', '123 Main St, City, ST 10060', 'zhapar@email.com', '8478709232')"""

    #Execute cursor and pass query as well as student data
    db_cursor.execute(student_sql_query)
    db_connection.commit()
    print(db_cursor.rowcount, "Record Inserted")

db_cursor = db_connection.cursor()
db_cursor.execute("USE elginexpress")
db_cursor.execute("SELECT name FROM drivers")

myresult = db_cursor.fetchall()

for x in myresult:
  print(x)


