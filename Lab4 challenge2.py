class Borrower:
    """Represents a person that can borrow books"""

    newIdCode = 1;  # Class variable

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.id = Borrower.newIdCode
        Borrower.newIdCode += 1  # Updates for next new borrower ...
        self.booksBorrowed = []

    def borrowBook(self, book):
        self.booksBorrowed.append(book)

    def showAllBooks(self):
        if len(self.booksBorrowed) == 0:
            print('No books out at the moment')
        else:
            for i in self.booksBorrowed:
                i.showTitle()

    def showBorrowerDetails(self):
        print("Name isL: " + self.firstname + self.lastname + "Id is: ", self.id, end='\n')


class Book:
    """A class to represent a book in a library"""

    def __init__(self, title, author, code, onLoan=False):
        self.title = title
        self.author = author
        self.code = code
        self.onLoan = onLoan

    def showTitle(self):
        print("Title :" + self.title, end='\n')


class Library:
    """A class to represent a lending library"""

    def __init__(self):
        self.allBorrowers = []
        self.allBooks = []

    def addBook(self, book):
        self.allBooks.append(book)

    def addBorrower(self, borrower):
        self.allBorrowers.append(borrower)

    def lendBook(self, borrower, book):
        if not book.onLoan:
            print('Lending book', book.title, 'to', borrower.firstname, borrower.lastname)
            book.onLoan = True
            borrower.borrowBook(book)
        else:
            print('Sorry the book already on loan.', end='\n')


def main():
    ## Create some books ...
    book1 = Book('Kafkas motorbike', 'Bridget Jones', 1290)
    book2 = Book('Cooking with Custard', 'Jello Biafra', 1002)
    book3 = Book('History of Bagpipes', 'John Cairncross', 987)

    # Put the books in the library
    library = Library()  # Creates the library
    library.addBook(book1)
    library.addBook(book2)
    library.addBook(book3)

    # Create some borrowers ...
    bor1 = Borrower('Kevin', 'Wilson')
    bor2 = Borrower('Rita', 'Shapiro')
    bor3 = Borrower('Max', 'Normal')

    library.addBorrower(bor1)
    library.addBorrower(bor2)
    library.addBorrower(bor3)

    # make some loans ...
    library.lendBook(bor1, book1)
    bor1.showBorrowerDetails()
    bor1.showAllBooks()
    library.lendBook(bor2, book3)
    bor2.showBorrowerDetails()
    bor2.showAllBooks()
    # Try to lend book3 out again ....
    library.lendBook(bor3, book3)


if __name__ == "__main__":
    main()
