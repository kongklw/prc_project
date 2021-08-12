import mysql.connector

cnx = mysql.connector.connect(user='root', password='mysql',
                              host='127.0.0.1',
                              database='kong')
cnx.close()