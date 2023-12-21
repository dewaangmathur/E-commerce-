def MAIN():
    while True:  
         print("===============================")
         print("")
         print("******WELCOME TO AMAZON******* \n World's best e-commerce platform.")
         print("")
         print("===============================")
         print("1.Admin")
         print("2.User")
         print("3.Quit project")
         print("")
         z=input('enter your choice')
         if z=='1':
             import ADMINCHECK
             ADMINCHECK.ADMINCHECK()
         elif z=='2':
             import SHOWAMAZON
             SHOWAMAZON.SHOW()
             c=input('do you want to reserve a product y/n (choice case sensitive)')
             if c=='y':
                 import ADDORDER
                 ADDORDER.ADDORDER()
         elif z=='3':
             print('thank you for visiting')
             break
         else:
             print('INVALID')
             break
