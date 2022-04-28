
def menu1():
    print("Welcome")
    print("1.Login")
    print("2.Create Account")
    print("3.Exit")


def itemsMenu(accnt):
    sortList = []
    print("1.Horror")
    print("2.Historical Fiction")
    print("3.Mystery")
    print("4.Nonfiction")
    input1 = input()
    count = 1
    if input1 == "1":
        for x in inventory:
            if x.getGenre() == "Horror":
                print(str(count) + ".")
                x.display()
                sortList.append(x)
                count+=1
    
    elif input1 == "2":
        for r in inventory:
            if r.getGenre() == "Historical Fiction":
                print(str(count) + ".")
                r.display()
                sortList.append(r)
                count+=1

    elif input1 == "3":
        for y in inventory:
            if y.getGenre() == "Mystery":
                print(str(count) + ".")
                y.display()
                sortList.append(y)
                count+=1

    elif input1 == "4":
        for z in inventory:
            if z.getGenre() == "Nonfiction":
                print(str(count) + ".")
                z.display()
                sortList.append(z)
                count+=1
    
    else: 
        print("Invalid Input")
        return
    

def cartMenu(accnt):
    loop = True
    while loop:
        print("1.View Items in a Genre")
        print("2.View cart")
        print("3.Remove an item from cart")
        print("4.Back")
        input1 = input()
        if input1 == "1":
            itemsMenu(accnt)
        elif input1 == "2":
            print("hello")
        elif input1 == "3":
            # add stuff
            print("Hello")
        elif input1 == "4":
            loop = False
        else: 
            print("Incorrect Input")


def menuAccount(accnt):
    print("1.View Account Information")
    print("2.Edit User Information")
    print("3.View Orders")
    print("4.Edit Cart")
    print("5.Delete Account")
    print("6.Logout")
    input1 = input()

    if input1 == "1":
        #display user infornation
        accnt.displayInfo()

    elif input1 == "2":
        print("1.Address")
        print("2.Payment")
        input2 = input("What would you like to change?")
        if input2 == "1":
            input3 = input("Enter the new address:")
            accnt.setAddress(input3)
        elif input2 == "2":
            input4 = input("Enter the new payment:")
            accnt.setPayment(input4)

    elif input1 == "3":
        accnt.displayOrders()

    elif input1 == "4":
        cartMenu(accnt)
    elif input1 == "5":
        print("Removing account")
        return 5
    elif input1 == "6":
        return 6
    else:
        print("Incorrect Input")
        return 0

#main method
# This program assumes that the inventory file is already filled. There are no methods to add a new stock item.
# We chose to do this because there was no requirement in the 
# assignment stating that the program had to have these functions

accounts = []
nameaccnts = [] # temp array
inventory = []

# getting the inventory from the file
file1 = open("inventory.txt", "r")
for d in range(10):
    itemN = Item()
    itemN.getFromFile(file1)
    inventory.append(itemN)

#getting accounts and orders from the file
if exists("accounts.txt"):
    if os.stat("accounts.txt").st_size != 0:
        f = open("accounts.txt", "r")
        contents = f.read()
        nameaccnts = contents.split("\n")
        for q in nameaccnts:
            newaccnt = Account()
            newaccnt.setFileName(q)
            newaccnt.getFromFile()
            newaccnt.retreiveOrders()
            accounts.append(newaccnt)
exit = 0
while exit != 1:
    menu1()
    input1 = input()
    if input1 == "1":
        usernameIn = input("Enter your username:")
        for x in accounts:
            if x.getUsername() == usernameIn:
                passwordIn = input("Enter your password:")
                if x.getPassword() == passwordIn:
                    #This is a successful login
                    p = True
                    while p:
                        ret = menuAccount(x)
                        if ret == 5:
                            accounts.remove(x)
                        elif ret == 6:
                            p = False
                
                else:
                    print("Incorrect Password")
            else:
                print("This account does not exist")

    elif input1 == "2":
        acctN = Account()
        while TRUE:
            input3 = input("Enter you desired username:")
            brk = True
            for r in accounts:
                if r.getUsername() == input3:
                    print(" This username is taken.")
                    brk = False
            if brk == True:
                acctN.setUsername(input3)
                break
        input4 = input("Enter you desired password:")
        acctN.setPassword(input4)
        
        input5 = input("Enter your first name:")
        acctN.setFName(input5)

        input6 = input("Enter your last name:")
        acctN.setLName(input6)

        input7 = input("Enter your address:")
        acctN.setAddress(input7)

        input8 = input("Enter your payment info:")
        acctN.setPayment(input8)

        accounts.append(acctN)

        print("Account Created")


    elif input1 == "3":
        f1 = open("accounts.txt", "w")
        f5 = open("inventory.txt", "w")
        for s in accounts:
            f1.write(s.getFileName() + "\n")
            s.export()
            s.ordersToFile()

        for u in inventory:
            u.export()
            
        exit = 1
    else:
        print("Incorrect input")
