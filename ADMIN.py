def ADMIN():
    import ADDAMAZON
    import UPDATEAMAZON
    import DELETEAMAZON
    import SHOWAMAZON
    x=True
    while x==True:
        print()
        print('1.ADD ORDER')
        print('2.UPDATE ORDER')
        print('3.DELETE ORDER')
        print('4.SHOW ALL ORDERS')
        print('5. EXIT')
        print()
        y=input('ENTER YOUR CHOICE.:')
        print()
        if y=='1':
            ADDAMAZON.ADD()
        elif y=='2':
            UPDATEAMAZON.UPDATE()
        elif y=='3':
            DELETEAMAZON.DELETE()
        elif y=='4':
            SHOWAMAZON.SHOW()
        elif y=='5':
            print('Thank You')
            break
        else:
            print('wrong CHOICE')


