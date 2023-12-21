def MAIN():
    while True:
        z=input('enter your choice')
        if z=='1':
            import ADMIN
            ADMIN.ADMIN()
        elif z=='2':
           import SHOWAMAZON
           SHOWAMAZON.SHOW()
        elif z=='3':
           print('thank you for visiting')
           break
        else:
            print('INVALID')
            break
