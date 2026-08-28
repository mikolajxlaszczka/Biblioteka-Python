class Book: # zdefiniowanie klasy - szablon do tworzenia konkretnych obiektow
    def __init__(self, title, author, category, year, publisher, pages, is_borrowed=False): #konstruktor
        # self to ten konkretny obiekt ktory tworzymy w nawiasie parametry
        self.title = title #przypisania
        self.author = author
        self.category = category
        self.year = year
        self.publisher = publisher
        self.pages = pages
        self.is_borrowed = is_borrowed