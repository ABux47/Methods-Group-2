class Item: 

    def __init__(self):
        self.title = ""
        self.author = ""
        self.ISBN = ""
        self.genre = ""
        self.year = ""
        self.stock = 0
        self.price = 0

    def decreaseStock(self, quan):
        self.stock = self.stock - quan
    
    def getStock(self):
        return self.stock

    def getPrice(self):
        return self.price

    def getTitle(self):
        return self.title

    def display(self):
        print(self.title + " " + self.author + " " + self.ISBN + " " + self.genre + " " + self.year)
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

    def getFromFile(self):
        file = open("inventory.txt", "r")
        self.title = file.readline()
        self.title.replace('\n', '')
        self.author = file.readline()
        self.author.replace('\n', '')
        self.ISBN = file.readline()
        self.ISBN.replace('\n', '')
        self.genre = file.readline()
        self.genre.replace('\n', '')
        self.year = file.readline()
        self.year.replace('\n', '')
        self.stock = file.readline()
        self.stock.replace('\n', '')
        self.price = file.readline()
        self.price.replace('\n', '')
 
