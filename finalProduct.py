        
from pickle import TRUE
from asyncio.windows_events import NULL
import os
from os.path import exists
#from numpy import logical_not
#from Item import Item 

class Item: 

    def __init__(self):
        self.title = ""
        self.author = ""
        self.ISBN = ""
        self.genre = ""
        self.year = ""
        self.stock = 0
        self.price = 0

    def create(self, title, author, ISBN, genre, year, stock, price):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.year = year
        self.stock = stock
        self.price = price

    def decreaseStock(self, quan):
        self.stock = self.stock - quan
    
    def getStock(self):
        return self.stock

    def getPrice(self):
        return self.price

    def getGenre(self):
        return self.genre

    def getTitle(self):
        return self.title

    def display(self):
        print(self.title + "  " + self.author + "  " + self.ISBN + "  " + self.genre + "  " + self.year)
        print("In stock: " + self.stock + "   $" + self.price)

    def export(self):    
        file = open("inventory.txt", "a")
        file.write(self.title + "\n")
        file.write(self.author + "\n")
        file.write(self.ISBN + "\n")
        file.write(self.genre + "\n")
        file.write(self.year + "\n")
        file.write(str(self.stock) + "\n")
        file.write(str(self.price) + "\n")

    def getFromFile(self, file):
        self.title = file.readline()
        self.title = self.title.strip()
        self.author = file.readline()
        self.author = self.author.strip()
        self.ISBN = file.readline()
        self.ISBN = self.ISBN.strip()
        self.genre = file.readline()
        self.genre = self.genre.strip()
        self.year = file.readline()
        self.year = self.year.strip()
        self.stock = file.readline()
        self.stock = self.stock.strip()
        self.price = file.readline()
        self.price = self.price.strip()


class Cart:
    def __init__(self):
        self.itemList = []
        self.quanOfItems = []
        self.total = 0

    def getItems(self):
        return self.itemList
    
    def getNumOfItems(self):
        return len(self.itemList)

    def getQuan(self):
        return self.quanOfItems
    
    def getTotal(self):
        return self.total

    def addItem(self, item, quan):
        if int(quan) > 0:
            if item in self.itemList:
                if (quan + self.quanOfItems[self.itemList.index(item)]) < item.getStock():
                    self.quanOfItems[self.itemList.index(item)] += quan
                else:
                    print("Not enough stock")
            elif quan > item.getStock():
                print("Quantity chosen is greater than what's in stock")
            else:
                self.itemList.append(item)
                self.quanOfItems.append(quan)
        self.total=0
        for item in self.itemList:
            quan = self.quanOfItems[self.itemList.index(item)]
            cost = float(quan) * float(item.getPrice())
            item.display()
            self.total = float(cost) + self.total
        print("Your current total is $" + '{0:.2f}'.format(self.total) + '\n')
        
    def deleteItem(self, item):
        if self.quanList[self.itemList.index(item)] <= 0:
            self.itemList.pop(item, None)
        else:
            if item in self.itemList:
                self.quanOfItems[self.itemList.index(item)] -= 1
                print("The quantity of " + item.title + " has been decreased by " + str(1) + " leaving " + str(self.quanOfItems[self.itemList.index(item)]) + " book(s) of this title in the cart" )

    def viewCart(self):
        for item in self.itemList:
            item.display()
            print( "Quantity in Cart:" +str(self.quanOfItems[self.itemList.index(item)]))
        print("Total:" + str(self.total))
    
    def clearCart(self):
        self.itemList = []
        self.total = 0
        self.quanOfItems = []





#account class
class Account:

    #constructor currently initializing all variables to strings ""
    def __init__ (self):
        self.username = ""
        self.password = ""
        self.fname = ""
        self.lname = ""
        self.address = ""
        self.payment = ""
        self.cart = Cart()
        self.orders = []
        self.numOfOrders = 0
        self.fileName = ""


        #Create a file of user account information that will only reference number of orders.
     
    def getFromFile(self):
        filename = self.fileName + ".txt"
        file = open(filename, "r")
        self.username = file.readline()
        self.username = self.username.strip()
        self.fname = file.readline()
        self.fname = self.fname.strip()
        self.lname = file.readline()
        self.lname = self.lname.strip()
        self.password = file.readline()
        self.password = self.password.strip()
        self.address = file.readline()
        self.address = self.address.strip()
        self.payment = file.readline()
        self.payment = self.payment.strip()
        self.numOfOrders = file.readline()
        self.numOfOrders = self.numOfOrders.strip()

    #Functions Setters/Getters

    def placeOrder(self):
        newOrder = Order()
        newOrder.addOrder(self.cart.getNumOfItems(), self.fileName, self.cart.getTotal(), self.cart.getItems(), self.cart.getQuan())
        newOrder.setAddress(self.address)
        newOrder.setPayment(self.payment)
        self.orders.append(newOrder)

    # EditName
    def setFName(self, fname):
        self.fname = fname

    def getFName(self):
        return self.fname

    def setLName(self, lname):
        self.lname = lname

    def getLName(self):
        return self.lname

    # Edit Username/Password

    def setPassword(self, password):
        self.password = password
        
    def getPassword(self):
        return self.password

    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username

    def setFileName(self, fileName):
        self.fileName = fileName

    def getFileName(self):
        return self.fileName

    def displayInfo(self):
        print("Username: " + self.username + "\n")
        print("Password: " + self.password + "\n")
        print("First Name: " + self.fname + "\n")
        print("Last Name: " + self.lname + "\n")
        print("Address: " + self.address + "\n")
        print("Payment: " + self.payment + "\n")
        print("Number of Orders: " + str(self.numOfOrders) + "\n")
        

    # Order Functions

    
    def retreiveOrders(self):
        if self.numOfOrders == 0:
            return
        file = open(self.fileName + "Orders.txt", "r")
        for r in range(int(self.numOfOrders)):
            newOrder = Order()
            newOrder.getFromFile(file)
            self.orders.append(newOrder)

    def displayOrders(self):
        for x in self.orders:
            x.viewOrder()

    def cartToOrder(self):
        self.numOfOrders= self.numOfOrders + 1
        newOrder = Order()
        newOrder.addOrder(self.cart.getNumItems(), self.fname + self.lname, self.cart.getTotal(), self.cart.getItems(), self.cart.getQuanList())
        newOrder.setAddress(self.address)
        newOrder.setPayment(self.payment)

    def ordersToFile(self):
        filename= self.fname + self.lname + "Orders.txt"
        open(filename, "w")
        for x in self.orders:
            x.export()
    
    # EditAddress

    def setAddress(self, address):
        self.address = address

    def getAdress(self):
        return self.address

    # EditPayment

    def setPayment(self, payment):
        self.payment = payment

    def getPayment(self):
        return self.payment

        #need to clear the file before exporting
    def export(self):
        filename = self.fileName + ".txt"
        file = open(filename, "w")
        file.write(self.username + "\n")
        file.write(self.password + "\n")
        file.write(self.fname + "\n")
        file.write(self.lname + "\n")
        file.write(self.address + "\n")
        file.write(self.payment + "\n")
        file.write(str(self.numOfOrders) + "\n")
        #file.write(self.address + "\n")
        #file.write(self.payment + "\n")

    # DeleteAccount

    def deleteAccount(self):
        del (self.username)
        del (self.password)
        del (self.fname)
        del (self.lname)
        del (self.orders)
        del (self.numOfOrders)
        del (self.address)
        del (self.payment)
        del (self.cart)
        del(self.orders)




class Order:
    items = []
    quanOfItems = []
    def addOrder(self, numOfItems, user, total, items, quanOfItems):
        self.numOfItems = numOfItems
        self.user = user
        self.total = total
        self.items = items
        self.quanOfItems = quanOfItems

    def getFromFile(self, file):
        self.numOfItems = file.readline()
        self.numOfItems = self.numOfItems.strip()
        self.total = file.readline()
        self.total = self.total.strip()
        self.address = file.readline()
        self.address = self.address.strip()
        self.payment = file.readline()
        self.payment = self.payment.strip()

        while TRUE:
            line = file.readline()
            line.replace('\n', '')
            if line == "%\n":
                break
            self.items.append(line)
        length = len(self.items)
        
        for x in range(length):
            line2= file.readline()
            line2.replace('\n', '')
            self.quanOfItems.append(line2)


    def setAddress(self, addressIn):
        self.address = addressIn
    
    def setUser(self, user):
        self.user = user

    def setPayment(self, paymentIn):
        self.payment = paymentIn

    def getAddress(self):
        return self.address
    
    def getPayment(self):
        return self.payment

    def viewOrder(self):
        count = 0

        for x in self.items:
            if isinstance(x, Item):
                x.display()
            else:
                print(x)
            print("Quantity: " + str(self.quanOfItems[count]))
            count= count+1
        
        print ("Sent to " + self.address)
        print ("Payment: " + self.payment)
        print("Total: " + str(self.total))


#need to clear the file before exporting
    def export(self):
        filename = self.user + "Orders.txt"
        file = open( filename, "a")
        file.write(str(self.numOfItems) + "\n")
        file.write(str(self.total) + "\n")
        file.write(self.address + "\n")
        file.write(self.payment + "\n")
        for r in self.items:
            file.write(r.getTitle() + "\n")

        file.write("%\n")

        for t in self.quanOfItems:
            file.write(str(t) + "\n")
    

#Main Driver
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
                print(str(count) + ".", end='')
                x.display()
                sortList.append(x)
                count+=1
    
    elif input1 == "2":
        for r in inventory:
            if r.getGenre() == "Historical Fiction":
                print(str(count) + ".", end='')
                r.display()
                sortList.append(r)
                count+=1

    elif input1 == "3":
        for y in inventory:
            if y.getGenre() == "Mystery":
                print(str(count) + ".",end='')
                y.display()
                sortList.append(y)
                count+=1

    elif input1 == "4":
        for z in inventory:
            if z.getGenre() == "Nonfiction":
                print(str(count) + ".",end='')
                z.display()
                sortList.append(z)
                count+=1
    
    else: 
        print("Invalid Input")
        return
    
    input2 = input("Enter the number by the book you would like to puchase or type 0 to go back")
    if input2 == "0":
        return
    elif input2 == "1":
        input3 = input("How many would you like?")
        accnt.cart.addItem(sortList[0], input3)
    
    elif input2 == "2":
        if len(sortList) >= 2:
            input3 = input("How many would you like?")
            accnt.cart.addItem(sortList[1], input3)
        else:
            print("Invalid Input")

    elif input2 == "3":
        if len(sortList) >= 3:
            input3 = input("How many would you like?")
            accnt.cart.addItem(sortList[2], input3)
        else:
            print("Invalid Input")
    
    elif input2 == "4":
        if len(sortList) >= 4:
            input3 = input("How many would you like?")
            accnt.cart.addItem(sortList[3], input3)
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")


def cartMenu(accnt):
    loop = True
    while loop:
        print("1.View Items in a Genre")
        print("2.View cart")
        print("3.Remove an item from cart")
        print("4.Place Order")
        print("5.Back")
        input1 = input()
        if input1 == "1":
            itemsMenu(accnt)
        elif input1 == "2":
            accnt.cart.viewCart()
        elif input1 == "3":
            input5 = input("Enter the title of the book you would like to remove")
            found = False
            for item in inventory:
                if input5 == item.getTitle():
                    found = True
                    accnt.cart.deleteItem(item)
            if found == False:
                print("Invalid Title")

        elif input1 == "4": 
            accnt.placeOrder()
            accnt.cart.clearCart()
        elif input1 == "5":
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

        acctN.setFileName(acctN.getFName() + acctN.getLName())
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

