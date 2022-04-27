
from pickle import TRUE


class Order:
    items = []
    quanOfItems = []
    def addOrder(self, numOfItems, user, total, items, quanOfItems):
        self.numOfItems = numOfItems
        self.user = user
        self.total = total
        self.items = items
        self.quanOfItems = quanOfItems

    def getFromFile(self):
        filename = self.user + "Orders.txt"
        file = open( filename, "r")
        self.numOfItems = file.readline()
        self.numOfItems.replace('\n', '')
        self.total = file.readline()
        self.total.replace('\n', '')
        self.address = file.readline()
        self.address.replace('\n', '')
        self.payment = file.readline()
        self.payment.replace('\n', '')

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
    
    def setName(self, user):
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
            print(x + "  Quantity: " + str(self.quanOfItems[count]))
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
            file.write(r + "\n")

        file.write("%\n")

        for t in self.quanOfItems:
            file.write(str(t) + "\n")
    
