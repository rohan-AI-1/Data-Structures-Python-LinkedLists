class Bank:
    next_acc_no=8473625348230
    acc_no=next_acc_no
    account={}
    def __init__(self,cust_name,mobile_no,acc_no,amt):
        self.cust_name=cust_name
        self.mobile_no=mobile_no
        self.acc_no=acc_no
        self.amt=amt
    @classmethod
    def createAccount(cls):
        amt=0
        cust_name=input("Enter the customer name:")
        mobile_no=input("Enter the mobile number:")
        acc_no=cls.next_acc_no+1
        print("Deposit the Initial Deposit Amount( Rs.3000 or more) to start the acoount")
        amount=int(input("Enter the amount to be deposited:"))
        if(amount>=3000):
            amt=amt+amount
            print(f"Your Account created successfully!\nAccount Number:{cls.acc_no}")
        else:
            while(amount<3000):
                print("Invalid Initial Deposit Amount")
                amount=int(input("Enter valid Initial Deposit Amount:"))
            amt=amt+amount
            print(f"Your Account created successfully!\nAccount Number:{cls.acc_no}")
        cls.account[cls.acc_no]={
            "Name":cust_name,
            "Phone Number":mobile_no,
            "Amount":amt
        }
        customer=Bank(cust_name,mobile_no,acc_no,amt)
        cls.acc_no=cls.acc_no+1
    
    @classmethod
    def Display(cls):
        Acc_NO=int(input("Enter your Account Number:"))
        if Acc_NO in cls.account:
            print(cls.account[Acc_NO])
        else:
            print("Invalid Account Number")
            while(Acc_NO not in cls.account):
                Acc_NO=int(input("Enter your valid Account Number:"))
                if Acc_NO in cls.account:
                    print(cls.account[cls.Acc_NO])
                    break
        print("Your Account Information printed successfully")

    @classmethod
    def Deposit(cls):
        Acc_NO=int(input("Enter your Account Number:"))
        if Acc_NO in cls.account:
            Amount=int(input("Enter the Amount to be deposited:"))
            cls.account[Acc_NO]["Amount"]=cls.account[Acc_NO]["Amount"]+Amount
            print("Amount Deposited Succesfully")
        else:
            print("Invalid Account Number")
            while(Acc_NO not in cls.account):
                Acc_NO=int(input("Enter your valid Account Number:"))
                if Acc_NO in cls.account:
                    Amount=int(input("Enter the Amount to be deposited:"))
                    cls.account[Acc_NO]["Amount"]=cls.account[Acc_NO]["Amount"]+Amount
                    print("Amount Deposited Succesfully")
                    break

        decide=int(input("Do you want to view your account information(1/0):"))
        if decide==1 or decide==0:
            if decide==1:
                print(cls.account[Acc_NO])
            else:
                return
        else:
            print("Invalid Choice")
    @classmethod
    def Withdraw(cls):
        Acc_NO=int(input("Enter your Account Number:"))
        if Acc_NO in cls.account:
            Amount=int(input("Enter the Amount to be withdrawn:"))
            if cls.account[Acc_NO]["Amount"]-Amount<3000:
                print("Insufficient Balance")
                while cls.account[Acc_NO]["Amount"]-Amount<3000:
                    Amount=int(input("Enter the valid Amount to be withdrawn:"))
                cls.account[Acc_NO]["Amount"]=cls.account[Acc_NO]["Amount"]-Amount
                print("Amount withdrawn Succesfully")
        else:
            print("Invalid Account Number")
            while(Acc_NO not in cls.account):
                Acc_NO=int(input("Enter your valid Account Number:"))
                if Acc_NO in cls.account:
                    Amount=int(input("Enter the Amount to be withdrawn:"))
                    cls.account[Acc_NO]["Amount"]=cls.account[Acc_NO]["Amount"]-Amount
                    print("Amount withdrawn Succesfully")
                    break

        decide=int(input("Do you want to view your account information(1/0):"))
        if decide==1 or decide==0:
            if decide==1:
                print(cls.account[Acc_NO])
            else:
                return

    @classmethod
    def CheckBalance(cls):
        Acc_NO=int(input("Enter your Account Number:"))
        if Acc_NO in cls.account:
            print(cls.account[Acc_NO]["Amount"])
        else:
            while (Acc_NO not in cls.account):
                print("Invalid Account Number")
                Acc_NO=int(input("Enter your Account Number:"))
                if Acc_NO in cls.account:
                    print(cls.account[Acc_NO]["Amount"])
                    break
        print("Balance has been printed")
    
    @classmethod
    def Logout(cls):
        print("Thank You For Taking Our Bank Services!See you back")
        exit(0)

    @classmethod
    def Bank_Services(cls):
        while(True):
            print("1. Create Your Account")
            print("2. Display Account Details")
            print("3. Deposit Money")
            print("4. Withdaw Money")
            print("5. Check Balance")
            print("6. LogOut")

            try:
                ch=int(input("Enter your Choice:"))
            
            except ValueError:
                print("Invalid Choice")
            
            if(ch==1):
                cls.createAccount()
                
            elif ch==2:
                cls.Display()
                
            elif ch==3:
                cls.Deposit()

            elif ch==4:
                cls.Withdraw()

            elif ch==5:
                cls.CheckBalance()

            elif ch==6:
                cls.Logout()

            else:
                print("Invalid Choice")
Bank.Bank_Services()






            
            

