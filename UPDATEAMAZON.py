def UPDATE():
    import mysql.connector
    mydb=mysql.connector.connect(user="root",host="localhost",password="tiger",database='AMAZON')
    cursor=mydb.cursor()
    a=int(input('enter order id to be updated:'))
    b=input('enter updated PRODUCT:')
    c=input('enter updated quantity:')
    d=input('enter updated mode of payment:')
    e=input('enter updated shipping date:')
    #values=(b,c,d,e,a)
    #run="update AMAZON set PRODUCT='%s',CART='%s',PAYMENT='%s',SHIPPING_DATE='%s' where ORDER_ID=%d"
    #cursor.execute(run,values)
    cursor.execute("update AMAZON set PRODUCT='%s',CART='%s',PAYMENT='%s',SHIPMENT_DATE='%s' where ORDER_ID=%d"%(b,c,d,e,a))
    print("ORDER UPDATED SUCCESSFULLY!")
    mydb.commit()
