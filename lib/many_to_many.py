class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []
        self._books = []

    def contracts(self):
        return self._contracts
    
    def books(self):
        return self._books

    def add_contract(self, contract):
        if not isinstance(contract, Contract):
            raise TypeError("contract must be an instance of Contract")
        self._contracts.append(contract)
        if contract.book not in self._books:
            self._books.append(contract.book)

    def total_royalties(self):
        total = 0
        for contract in self._contracts:
            total += contract.royalties
        return total
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    
    pass


class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []
        self._authors = []

    def contracts(self):
        return self._contracts
    
    def authors(self):
        return self._authors
    pass


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be a number")
        if royalties < 0:
            raise ValueError("royalties must be a positive number")
        self.date = date
        self.royalties = royalties
        self.author = author
        self.book = book
        Contract.all.append(self)


        if book not in author.books():
            author._books.append(book)

        book._contracts.append(self)

        if author not in book.authors():
            book._authors.append(author)
            author._contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]

    pass