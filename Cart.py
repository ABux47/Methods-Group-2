from Item import Item 
class Cart:
    def __init__(self):
        self.itemList = {}
        self.total= 0

    def ViewItems(self):
        print("Items in stock: ")
        for i in self.itemList:
            print(i.name, i.quantity, '{0:.2f}'.format(i.price))

    def AddItem(self, item, quantity=1):
        if quantity > 0:
            if item in self.itemList:
                self.itemList[item] += quantity
            elif quantity > item.quantity:
                print("Quantity chosen is greater than what's in stock")
            else:
                self.itemList[item] = quantity
        self.total=0
        for item in self.itemList:
            quantity = self.itemList[item]
            cost = quantity * item.price
            print("Title: " + item.name + " Quantity: " + str(quantity) + " Cost: " + '{0:.2f}'.format(cost))
            self.total += cost
        print("Your current total is $" + '{0:.2f}'.format(self.total) + '\n')

    def DeleteItem(self, item, quantity):
        if quantity <= 0:
            self.itemList.pop(item, None)
        else:
            if item in self.itemList:
                if quantity < self.itemList[item]:
                    self.itemList[item] -= quantity
                else:
                    self.itemList.pop(item, None)
    
    def PlaceOrder(self):
        self.total = 0
        for item in self.itemList:
            quantity = self.itemList[item]
            cost = quantity * item.price
            print("Title: " + item.name + " Quantity: " + str(quantity) + " Cost: " + '{0:.2f}'.format(cost))
            self.total += cost
            item.quantity -= quantity
        print("Grand total for this order is $" + '{0:.2f}'.format(self.total) + '\n')

    def AddDuplicateItem(self, item, quantity):
        if quantity > 0:
            self.itemList[item] = quantity
        else:
            self.DeleteItem(item)

