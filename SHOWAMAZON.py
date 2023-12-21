def SHOW():
    import mysql.connector
    mydb=mysql.connector.connect(user="root",host="localhost",password="tiger",database="AMAZON")
    cursor=mydb.cursor()
    sql="select * from AMAZON;"
    cursor.execute(sql)
    i=cursor.fetchall()
    for ORDER_ID,PRODUCT,CART,PAYMENT,SHIPPING_DATE in i:
        print("%d \t| '%s' \t| '%s' \t| '%s' \t| '%s'"%(ORDER_ID,PRODUCT,CART,PAYMENT,SHIPPING_DATE))
            
