from asyncio.windows_events import NULL
from numpy import logical_not

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
        self.cart = ""
        self.orders = []
        self.numOfOrders = ""

    #Create a file of user account information that will only reference number of orders.
     
    def getFromFile(self):
        filename = self.lname + ".txt"
        file = open( filename, "r")
        self.username = file.readline()
        self.username.replace('\n', '')
        self.fname = file.readline()
        self.fname.replace('\n', '')
        self.lname = file.readline()
        self.lname.replace('\n', '')
        self.password = file.readline()
        self.password.replace('\n', '')
        self.address = file.readline()
        self.address.replace('\n', '')
        self.payment = file.readline()
        self.payment.replace('\n', '')
        self.cart = file.readline()
        self.cart.replace('\n', '')
        self.numOfOrders = file.readline()
        self.numOfOrders.replace('\n', '')


    # Login 

    def setLogin(self, username, password):
        self.username = username
        self.password = password

    def getLogin(self):
        return self.password, self.username

    # Logout 

    def Logout(self):
        self.username = NULL
        self.password = NULL
        print ("You have been succeffully logged out.")
        return self.password, self.username

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

    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username

    def setPassword(self, password):
        self.password = password
        
    def getPassword(self):
        return self.password

    

    # AddPastOrder?

    def retreiveOrders(self):
        for r in range(self.numOfOrders):
            newOrder = Order()
            newOrder.getFromFile()
            self.orders.append(newOrder)

    def displayOrders(self):
        for x in self.orders:
            x.displayOrder()


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

    # DeleteAccount

    def deleteAccount(self):
        del (self.username)
        del (self.password)
        del (self.name)
        del (self.orders)
        del (self.numOfOrders)
        del (self.address)
        del (self.payment)
        del (self.cart)
        del(self.orders)

    #need to clear the file before exporting
    def export(self):
        filename = self.lname + ".txt"
        file = open(filename, "a")
        file.write(self.username + "\n")
        file.write(self.password + "\n")
        file.write(self.fname + "\n")
        file.write(self.lname + "\n")
        file.write(self.address + "\n")
        file.write(self.payment + "\n")
        file.write(self.cart + "\n")
        file.write(self.numOfOrders + "\n")
        file.write(self.address + "\n")
        file.write(self.payment + "\n")

#main driver code

