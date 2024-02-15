class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def listedBooks(self):
        self.file.seek(0)
        books = self.file.read().splitlines()

        for book in books:
            book_info = book.strip().split(",")
            print("Book's name:", book_info[0] + "," + " Book's author:",book_info[1])

    def addBook(self):
        title = input("Please enter the book's name:")
        author = input("Please enter the author's name:")
        releaseYear = input("Please enter the first release year:")
        page = input("Please enter the number of pages:")

        newBook = str(title+","+author+","+releaseYear+","+page+"\n")

        self.file.write(newBook)

    def removeBook(self):
        bookName = input("Enter the book's name that you want to remove: ")
        bookName = bookName.lower()

        self.file.seek(0)
        books = self.file.readlines()

        newList = []

        removed = False
        for book in books:
            if book.split(",")[0].lower() == bookName:
                removed = True
            else:
                newList.append(book)

        if removed:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(newList)
            print("Book removed")
        else:
            print("Book not found.")


lib = Library()
a = 0
while a < 1:
    print("""
            *** MENU***
            1) List Books
            2) Add Book
            3) Remove Book
            4) Quit
    """)
    welcome = int(input("Please select a menu item you want to take:"))

    if welcome == 1:
        lib.listedBooks()
    elif welcome == 2:
        lib.addBook()
    elif welcome == 3:
        lib.removeBook()
    elif welcome == 4:
        a = a+1
    else:
        print("The menu item you choose is invalid, try again.")
