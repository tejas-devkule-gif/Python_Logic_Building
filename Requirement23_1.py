class BookStore:
    NoOfBooks=0

    def __init__(self,name,author):
        self.Name=name
        self.Author=author
        
        BookStore.NoOfBooks += 1

    def Display(self):
        print("Book Name is :",self.Name)
        print("Author Name is :",self.Author)


b1=BookStore("Data Structures And Algorithms Made Easy","Narasimha Karumanchi")
b2=BookStore("How to become an Expert in Software Engineering","Marcus Tomlinson")

b1.Display()
print()

b2.Display()
print()

print("Total no of Books :",BookStore.NoOfBooks)

    

    