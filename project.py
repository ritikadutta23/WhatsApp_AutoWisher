import mysql.connector
import datetime
import os
now=str(datetime.date.today())
Today=now[8:10]+now[5:7]
print(Today)

con= mysql.connector.connect(host="localhost",user="root",password="",database ="whatsapp")
cur=con.cursor()
cur.execute(f"SELECT * FROM wishes WHERE BIRTH_DATE = {Today}")
list1=cur.fetchall()
for i in list1:
    print(i)
input("press enter to start wish. Make sure to connect to internet")
for i in list1:
    os.system(f"start https://web.whatsapp.com/send?phone=91{i[2]}^&text=Happy%20Birthday%20to%20you%20{i[0]}")
