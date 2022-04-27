from asyncio.windows_events import NULL
from numpy import logical_not

#account class
class Account:

    #constructor currently initializing all variables to strings ""
    def __init__ (self):
        self.username = ""
        self.password = ""
        self.name = ""
        self.address = ""
        self.payment = ""
        self.cart = ""
        self.orders = []
        self.numOfOrders = ""
    #Functions Setters/Getters

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
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    # Edit Username/Password

    def setPassword(self, password):
        self.password = password
        
    def getPassword(self):
        return self.password

    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username

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
        address =  input("Enter you address: ")

    def getAdress(self):
        return self.address

    # EditPayment

    def setPayment(self, payment):
        self.payment = payment
        payment =  input("Enter you payment info: ")

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

