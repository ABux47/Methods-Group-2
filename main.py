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
