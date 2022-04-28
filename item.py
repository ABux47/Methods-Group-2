
class Item: 

    def __init__(self, title, author, ISBN, genre, year, stock, price):
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

    def getTitle(self):
        return self.title

    def display(self):
        print(self.title + " " + self.author + " " + self.ISBN + " " + self.genre + " " + self.year)
        print("In stock: " + self.stock + "   $" + self.price)
