import mysql.connector

try:
    mydb = mysql.connector.connect(
        host ='localhost',
        user = 'root',
        password ='Progamer12345'
    )
    cursor =mydb.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as er:
        print(f"Failed creating database: {er}")
    cursor.close()
    mydb.close()

except mysql.connector.Error as er:
    print(f"failed with{er}")
    