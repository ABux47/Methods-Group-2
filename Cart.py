from Item import Item 
class Cart:
    def __init__(self):
        self.itemList = {}
        

    def ViewItems(self,item):
        self.item = item
        Item.display(item)


    def AddItem(self, item, stock=1):
        self.item = stock
        if stock > 0:
            if item in self.itemList:
                self.itemList[item] = stock
            elif stock > Item.getStock(item):
                print("Quantity chosen is greater than what's in stock")
            else:
                self.itemList[item] = stock
        Item.display(item)
        totalCost = 0
        for item in self.itemList:
            stock = self.itemList[item]
            cost = stock * item.price
            print("Title: " + item.title + " Quantity: " + str(stock) + " Cost: " + '{0:.2f}'.format(cost))
            totalCost += cost
        print("Your current total is $" + '{0:.2f}'.format(totalCost) + '\n')

    def DeleteItem(self, item, stock=1):
        if stock <= 0:
            self.itemList.pop(item, None)
        else:
            if item in self.itemList:
                if item in self.itemList:
                    self.itemList[item] -= stock
                    tmp = self.itemList[item]
                    print("The quantity of " + item.title + " has been decreased by " + str(stock) + " leaving " + str(tmp) + " book(s) of this title in the cart" )
                else:
                    self.itemList.pop(item, None)
    
    def PlaceOrder(self,stock=1):
        totalCost = 0
        self.item = stock
        for item in self.itemList:
            quantity = self.itemList[item]
            cost = quantity * item.price
            tmp = self.itemList[item]
            print("Title: " + item.title + " Quantity: " + str(tmp) + " Cost: " + '{0:.2f}'.format(cost))
            totalCost += cost
            Item.decreaseStock(item,tmp)
        print("Grand total for this order is $" + '{0:.2f}'.format(totalCost) + '\n')

    def AddDuplicateItem(self, item, stock=1):
        if item in self.itemList:
            task = input("That item already exists in the cart! Would you like to add more? (Y/N): ")
            while(1):
                if task == "Y":
                    more = int(input("How many more would you like to add? "))
                    if stock + more < Item.getStock(item):
                        print("Successfully added " + str(more) + " book(s)")
                        self.itemList[item] = self.itemList[item] + more
                        break
                    else:
                        print("\nError: you have tried to add too many books, try again")
                else:
                    return None
