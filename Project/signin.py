# Uname='hareesh'
# Upass='hareesh@123'
# bal=10000

customers=[
    {
        'Uname':'hareesh',
        'Upass':'hareesh@123',
        'bal':10000
    },
    {
        'Uname':'john',
        'Upass':'john@123',
        'bal':20000
    },
    {
        'Uname':'peter',
        'Upass':'peter@123',
        'bal':25000
    }
]

iusername=input('Enter your Username: ')
ipassword=input('Enter your Password: ')

for i in customers:
    if iusername==i['Uname'] and ipassword==i['Upass']:
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
            bal=i['bal']

            match Index:
                case  1:
                    amount=int(input('Enter the withdrwal amount'))
                    if amount>0 and amount<bal:
                        bal-=amount
                        i.update({'bal':bal})
                        print('amount withdraw successful and you acc is :',bal)
                    else:
                        print('insuffient funds')    
                case 2:
                    amount=int(input('Enter the amount: '))
                    if amount>0:
                        bal+=amount
                        i.update({'bal':bal})
                        print('Amount diposited successfully and you current acc bal is:',bal)
                case 3:
                    print('your current account bal is: ',bal)
                case 4:
                    break                      