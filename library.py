import re
import json
import functools
from datetime import datetime

from book import Book
from exceptions import KsiazkaNiedostepnaError
def log_action(func): # dekorator
    @functools.wraps(func) # nadpisana funckja nie traci swojej nazwy i dokumentacji
    def wrapper(*args, **kwargs):
        czas = datetime.now().strftime("%H:%M:%S") # pobiera z systemu obecny czas
        print(f"--- LOG. Wykonano systemową akcję o {czas} ---") # print do konsoli
        return func(*args, **kwargs) # wywolanie orginalnej funkcji + jej wynik
    return wrapper

class Library:
    def __init__(self): # konstruktor
        self.filepath = "dane.json"  # zdefiniowanie sciezki do pliku json i pustej listy books
        self.books = []
        self.load_data() # przy kazdym uruchomieniu biblioteka probuje wyciaganc z dysku dane

    def add_book(self, title, author, category, year, publisher, pages):
        if not re.match(r"^\d{4}$", str(year)): # filtrowanie przez regex - wymusza wpisanie dokladnie 4 cyfr
            print("Błąd: Rok musi składać się z 4 cyfr!")
            return
        nowa_ksiazka = Book(title, author, category, year, publisher, pages)
        self.books.append(nowa_ksiazka)
        self.save_data()

    def save_data(self):
        with open(self.filepath, 'w', encoding='utf-8') as plik: # tryb 'w' wyciagasz atrybuty z kazdego obiektu Book z listy i tworzy slownik
            dane_do_zapisu = []
            for b in self.books:
                dane_do_zapisu.append({
                    "title": b.title,
                    "author": b.author,
                    "category": b.category,
                    "year": b.year,
                    "publisher": b.publisher,
                    "pages": b.pages,
                    "is_borrowed": b.is_borrowed
                })
            json.dump(dane_do_zapisu, plik, indent=4, ensure_ascii=False) # zapisanie slownika
            # ensure_ascii=False gwarantuje ze polskie znaki zapisza sie poprawnie


    def load_data(self): # deserializacja
        try:
            with open(self.filepath, 'r', encoding='utf-8') as plik: # tryb 'r' zamienia pliki json na pythonowe + petla przechodzi po kazdym elemencie i buduje klase Book
                dane = json.load(plik)


                self.books = []
                for element in dane:
                    ksiazka = Book(
                        element["title"],
                        element["author"],
                        element["category"],
                        element["year"],
                        element["publisher"],
                        element["pages"],
                        element["is_borrowed"]
                    )
                    self.books.append(ksiazka)

        except FileNotFoundError: # zabezpieczneie zeby nie wywalilo bledem gdy ktos odpali program poraz pierwszy i bedzie mial pusta liste (bo json nie istnieje)
            self.books = []



    def get_all_categories(self):
        kategorie = {book.category for book in self.books}
        return sorted(list(kategorie))


    def search_by_category(self, category_name):
        found_books = [book for book in self.books if book.category.lower() == category_name.lower()] # list comprehension - jednolinijkowy sposob na stworzenie przefiltrowanej listy

        found_books.sort(key=lambda b: b.title) # lambda mowi metodzie zeby ukladajac alfabetycznie patrzyla tylko na atrybut title

        return found_books


    @log_action
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    raise KsiazkaNiedostepnaError(title)
                else:
                    book.is_borrowed = True
                    self.save_data()
                    return True

        raise KsiazkaNiedostepnaError(title)

    @log_action
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                self.save_data()
                return True
        return False


    @log_action
    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                self.save_data()
                return True
        return False

    def get_book_info(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    @log_action
    def update_book_field(self, title, pole, nowa_wartosc):
        for book in self.books:
            if book.title.lower() == title.lower():
                if pole == '1':
                    book.title = nowa_wartosc
                elif pole == '2':
                    book.author = nowa_wartosc
                elif pole == '3':
                    book.category = nowa_wartosc
                elif pole == '4':
                    if not re.match(r"^\d{4}$", str(nowa_wartosc)):
                        print(" Błąd: Rok wydania musi składać się z 4 cyfr!")
                        return False
                    book.year = nowa_wartosc
                elif pole == '5':
                    book.publisher = nowa_wartosc
                elif pole == '6':
                    book.pages = nowa_wartosc

                self.save_data()
                return True
        return False

# generatory - zamiast robic pusta liste wynik=[...] i na koniec return uzywamy instrukcji yield book w petli
    #generator po to ze jakby biblioteka miala milion ksiazek to program nie musialby ladowac ich wszystkich do listy w pamieci RAM
    # wypluwa wartosci pojedynczo na zadanie programu
    def get_available_books(self):
        for book in self.books:
            if not book.is_borrowed:
                yield book

    def get_borrowed_books(self):
        for book in self.books:
            if book.is_borrowed:
                yield book