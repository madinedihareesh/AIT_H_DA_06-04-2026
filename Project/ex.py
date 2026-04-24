Uname='hareesh'
Upass='hareesh@123'
bal=10000

iusername=input('Enter your Username: ')
ipassword=input('Enter your Password: ')

if Uname==iusername and Upass==ipassword:
    print('Hi',iusername,'. Login successful')
    while True:
        print('''
        Welcome to the Back
        Menu
        1.Withdraw
        2.Diposite
        3.Bal Enq
        4.Exit                              
''')
        Index=int(input('Enter your choice: '))

        match Index:
            case  1:
                amount=int(input('Enter the withdrwal amount'))
                if amount>0 and amount<bal:
                    bal-=amount
                    print('amount withdraw successful and you acc is :',bal)
                else:
                    print('insuffient funds')    
            case 2:
                amount=int(input('Enter the amount: '))
                if amount>0:
                    bal+=amount
                    print('Amount diposited successfully and you current acc bal is:',bal)
            case 3:
                print('your current account bal is: ',bal)
            case 4:
                break                      