def DELETE():
    import mysql.connector
    mydb=mysql.connector.connect(user="root",host="localhost",password="tiger",database='AMAZON')
    cursor=mydb.cursor()
    a=input('enter order id to be deleted:')
    cursor.execute("delete from AMAZON where order_id='{}'".format(a))
    print("ORDER DELETED SUCCESSFULLY!")
    mydb.commit()
