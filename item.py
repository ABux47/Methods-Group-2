ISBN = int()
Title = str()
Author =str()
Genre = str  ()
Year=int ()
Stock=int()
Price= int()
quanity= int(50)
itemsold=int()
history = str()
horror = str()
fantasy = str()
mystery = str ()
wellness =str()
novel=str()
manga=str()
Genre = tuple(history, horror, fantasy, mystery, wellness, novel, manga )
book = tuple(ISBN,Title, Author,Genre, Year, Stock)


library = dict(
    
    {"ISBN":"2543","Title":"Harry Potter: Sorcer Stone", "Author": "J.K. Rowling","Genre":"fantasy", "Year":"1998"},
    {"ISBN":"1654","Title":"The Shining","Author":"Stephen King", "Genre":"horror","Year":"1977"},
    {"ISBN":"7635","Title":"Gone Girl","Author":"Gillian Flynn","Genre":"mystery","Year":"2012"},
    {"ISBN":"5634","Title":"Better Than Before","Author":"Gretchen Rubin","Genre":"wellness","Year":"2015"},
    {"ISBN":"8967","Title":"1491","Author":"Charles C. Mann","Genre":"history","Year":"2005"},
    {"ISBN":"8536","Title":"To Kill A Mockingbird","Author":"Harper Lee", "Genre":"Novel", "Year":"1960"},
    {"ISBN":"3564","Title":"Berserk","Author":"Hakusensha","Genre":"Manga","Year":"1990"}

)


class Item():
    def viewCategory(Genre, Author, Title):
        if (Genre) : 
            input("what is the Genre of the book you are looking for ?:")
            print(library["Genre", "Title"])
        
        elif (Author):
             input("who is the author you are looking for ?")
             print(library["Author","Title"])
        
        elif (Title):
             input(" what is the title of the book you are looking for ?")
             print(library["Title"])

   
    def decreaseStock(int):
        for i in range (quanity):
            stock = print(" number of items in stock",(i-1), end = ":")

    
    def book(self):
       return book(ISBN, Title, Author,Genre, Year, Stock , Price). format(self.ISBN, self.Title,self.Author, self.Genre, self. Year, self.Stock, self.Price)
    ()
