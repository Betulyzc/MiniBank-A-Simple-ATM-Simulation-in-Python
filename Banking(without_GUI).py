customer_accounts=[
    {
        "name":"Betül",
        "surname":" Yazıcı",
        "accountNumber":1,
        "balance":150000,
        "additionalAccount":5000,
        "username":"betulYazici",
        "password":"1234"
    },
    {
        "name":"Cansu",
        "surname":"İnam",
        "accountNumber":2,
        "balance":5000,
        "additionalAccount":2000,
        "username":"inamCansu",
        "password":"4321"
    }
]


def operationsMenu(account):
    print(f"Welcome {account['name']}.")
    print("Which action would you like to perform?")
    print(" 1- Balance Inquiry\n 2-Withdraw Money\n 3- Deposit Money\n 4- Exit the menu")

    
    while True:
        try: 
            selectedOperationNumber=int(input("Please enter the number:"))
            if (selectedOperationNumber==1):
                balanceInquiry(account)
                break 
            elif(selectedOperationNumber==2):
                withdrawMoney(account)
                break
            elif(selectedOperationNumber==3):
                depositMoney(account)
                break
            elif(selectedOperationNumber==4):
                print("Exiting the menu...")
                break
            else:
                print("Invalid Value Please enter a number between 1 and 4 (1- Balance Inquiry, 2-Withdraw Money, 3- Deposit Money, 4- Exit the menu)")
        except ValueError:
            print("Invalid Input! Please enter a number between 1 and 4 (1- Balance Inquiry, 2-Withdraw Money, 3- Deposit Money, 4- Exit the menu)")


    
def balanceInquiry(account):
    print(f"Your account balance is {account['balance']} liras")
    print(f"Additional balance: {account['additionalAccount']}.")

def withdrawMoney(account):
    requestedMoney=int(input("How much money do you want to withdraw from your account:"))

    if requestedMoney <= 0:
            print("Invalid amount! Please enter a positive value.")
            return

    if account['balance']>=requestedMoney:
        account['balance']-=requestedMoney
        print("The withdrawal transaction is successful.")
        print(f"Remaining limit in additional account: {account['additionalAccount']}------ main account: {account['balance']}")

   
    elif (account['balance']<requestedMoney):
    
        if(account['balance']+account['additionalAccount']<requestedMoney):
            print("Withdrawal failed. Insufficient funds.")

        elif(account['balance']+ account['additionalAccount']>requestedMoney):
            answer=input("The amount you want to withdraw exceeds the main amount. Would you like to apply for an additional account?Yes(y),No(n): ").lower()
        
            if(answer=="y"):
                requestedMoney-=account['balance']
                account['balance']=0
                account['additionalAccount']-=requestedMoney
                print("The withdrawal transaction is successful with Additional Account.")
                print(f"Remaining limit in additional account: {account['additionalAccount']}------ main account: {account['balance']}")
        
            elif(answer=="n"):
                print("Withdrawal failed.")
        
        else:
            raise ValueError("You entered an invalid character.")

        

def depositMoney(account):
    try:
        amount = int(input("How much money do you want to deposit: "))
        if amount > 0:
            account['balance'] += amount
            print(f"Successfully deposited {amount} liras into your account.")
        else:
            print(" Invalid amount! Please enter a positive value.")
    except ValueError:
        print(" Invalid input! Please enter a valid number.")

    print(f"Updated account balance: {account['balance']} liras")

    
def login():
    username=input("username: ")
    password=input("password: ")

    isLoggedIn=False

    for account in customer_accounts:
        if (account['username']==username and account['password']==password):
            isLoggedIn=True
            operationsMenu(account)
            break

    if not(isLoggedIn):
        print("Username or password is incorrect!")


login()
    
