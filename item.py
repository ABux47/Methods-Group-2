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
