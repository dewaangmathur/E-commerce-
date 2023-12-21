def ADD():
    import mysql.connector
    mydb=mysql.connector.connect(user="root",host="localhost",password="tiger",database='AMAZON')
    cursor=mydb.cursor()
    a=input('enter product id: ')
    b=input('enter product name: ')
    c=input('enter quantity: ')
    d=input('enter mode of payment: ')
    e=input('enter shipping date: ')
    values=(a,b,c,d,e)
    run="INSERT INTO AMAZON(ORDER_ID,PRODUCT,CART,PAYMENT,SHIPMENT_DATE) VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(run,values)
    print("ORDER ADDED SUCCESSFULLY!")
    mydb.commit()
