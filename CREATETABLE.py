import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="AMAZON")
cursor=mydb.cursor()
y="CREATE TABLE AMAZON(ORDER_ID INTEGER NOT NULL PRIMARY KEY,PRODUCT VARCHAR(50) NOT NULL,CART VARCHAR(20) NOT NULL,PAYMENT VARCHAR(25) NOT NULL,SHIPMENT_DATE DATE)"
cursor.execute(y)

