from asyncio.windows_events import NULL

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


        #Create a file of user account information that will only reference number of orders.
     
    def getFromFile(self):
        filename = self.fname + self.lname + ".txt"
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
        self.numOfOrders = file.readline()
        self.numOfOrders.replace('\n', '')

    #Functions Setters/Getters


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

    def getFileName(self):
        return self.fname + self.lname

    def displayInfo(self):
        print("Username: " + self.username, end='')
        print("Password: " + self.password, end='')
        print("First Name: " + self.fname, end='')
        print("Last Name: " + self.lname, end='')
        print("Address: " + self.address, end='')
        print("Payment: " + self.payment, end='')
        print("Number of Orders: " + self.numOfOrders, end='')

    # Order Functions

    
    def retreiveOrders(self):
        if self.numOfOrders == 0:
            return
        for r in range(self.numOfOrders):
            newOrder = Order()
            newOrder.getFromFile()
            self.orders.append(newOrder)

    def displayOrders(self):
        for x in self.orders:
            x.displayOrder()

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
        address =  input("Enter you address: ")

    def getAdress(self):
        return self.address

    # EditPayment

    def setPayment(self, payment):
        self.payment = payment
        payment =  input("Enter you payment info: ")

    def getPayment(self):
        return self.payment

        #need to clear the file before exporting
    def export(self):
        filename = self.fname + self.lname + ".txt"
        file = open(filename, "w")
        file.write(self.username + "\n")
        file.write(self.password + "\n")
        file.write(self.fname + "\n")
        file.write(self.lname + "\n")
        file.write(self.address + "\n")
        file.write(self.payment + "\n")
        file.write(self.numOfOrders + "\n")
        file.write(self.address + "\n")
        file.write(self.payment + "\n")

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
