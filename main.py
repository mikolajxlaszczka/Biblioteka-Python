from library import Library
from exceptions import KsiazkaNiedostepnaError

def main():
    biblioteka = Library() # uruchamia konstruktor init() w library i laduje dane z pliku json


    while True: # nieskonczona petla az uzytkownik nie wypisze 0 co zbreakuje program
        print("\n" + "=" * 30)
        print("  --- MINI BIBLIOTEKA ---")
        print("=" * 30)
        print("1. Dodaj nową książkę")
        print("2. Wypożycz książkę")
        print("3. Zwróć książkę")
        print("4. Pokaż dostępne książki")
        print("5. Szukaj książki po kategorii")
        print("6. Usuń książkę")
        print("7. Edytuj książkę")
        print("0. Wyjdź")
        print("=" * 30)

        wybor = input("Wybierz opcję: ")

        try: # dziala do momnentu problemu z wypozyczeniem (jest wypozyczona lub nie ma jej w bazie)
            if wybor == '1':
                title = input("Tytuł: ")
                author = input("Autor: ")
                category = input("Kategoria: ")
                year = input("Rok wydania (4 cyfry): ")
                publisher = input("Wydawca: ")
                pages = input("Ilość stron: ")
                biblioteka.add_book(title, author, category, year, publisher, pages)


            elif wybor == '2':
                title = input("Podaj tytuł książki do wypożyczenia: ")
                if biblioteka.borrow_book(title):
                    print(" Książka została pomyślnie wypożyczona!")


            elif wybor == '3':
                wypozyczone = list(biblioteka.get_borrowed_books())
                if not wypozyczone:
                    print("Brak wypożyczonych książek do zwrotu.")
                else:
                    print("\n--- Aktualnie wypożyczone książki ---")
                    for b in wypozyczone:
                        print(f" '{b.title}' - {b.author}")
                    print("-------------------------------------")
                    title = input("Podaj tytuł książki do zwrotu (lub wpisz 0, aby anulować): ")
                    if title == '0':
                        print("Anulowano operację zwrotu.")
                    elif biblioteka.return_book(title):
                        print(" Książka została zwrócona!")
                    else:
                        print(" Nie znaleziono takiej wypożyczonej książki (sprawdź literówki).")


            elif wybor == '4':
                print("\n--- Dostępne Książki ---")
                dostepne = list(biblioteka.get_available_books())
                if not dostepne:
                    print("Brak wolnych książek.")
                else:
                    for b in dostepne:
                        print(f" '{b.title}' - {b.author} ({b.year})")


            elif wybor == '5':
                dostepne_kat = biblioteka.get_all_categories()
                if not dostepne_kat:
                    print("Obecnie w bibliotece nie ma żadnych książek, a co za tym idzie - kategorii.")
                else:
                    print("\n--- Dostępne kategorie ---")
                    print(", ".join(dostepne_kat))
                    print("--------------------------")
                kat = input("Podaj kategorię do wyszukania: ")
                wyniki = biblioteka.search_by_category(kat)
                if not wyniki:
                    print("Brak wyników w tej kategorii.")
                else:
                    print(f"\n--- Znalezione (posortowane alfabetycznie) ---")
                    for b in wyniki:
                        print(f" '{b.title}' - {b.author}")


            elif wybor == '6':
                title = input("Podaj tytuł książki do usunięcia: ")
                if biblioteka.remove_book(title):
                    print(" Książka została usunięta z systemu!")
                else:
                    print(" Nie znaleziono takiej książki.")


            elif wybor == '7':

                title = input("Podaj tytuł książki, którą chcesz edytować: ")

                book = biblioteka.get_book_info(title)

                if not book:

                    print(" Nie znaleziono takiej książki w systemie.")
                else:
                    print("\n--- Aktualne dane książki ---")
                    print(f"1. Tytuł: {book.title}")
                    print(f"2. Autor: {book.author}")
                    print(f"3. Kategoria: {book.category}")
                    print(f"4. Rok wydania: {book.year}")
                    print(f"5. Wydawca: {book.publisher}")
                    print(f"6. Ilość stron: {book.pages}")
                    print("0. Anuluj edycję")
                    pole = input("\nWybierz numer pola do edycji (0-6): ")
                    if pole == '0':
                        print("Anulowano edycję.")
                    elif pole in ['1', '2', '3', '4', '5', '6']:
                        nowa_wartosc = input("Podaj nową wartość: ")
                        if biblioteka.update_book_field(book.title, pole, nowa_wartosc):
                            print(" Pomyślnie zaktualizowano dane książki!")

                    else:

                        print(" Nieprawidłowy wybór pola.")

            elif wybor == '0':
                print("Zamykanie programu. ")
                break

            else:
                print(" Nieznana opcja. Wybierz numer od 0 do 5.")

        except KsiazkaNiedostepnaError as e:
            print(f"\n BŁĄD BIBLIOTEKI: {e}")

        except Exception as e:
            print(f"\n WYSTĄPIŁ NIEOCZEKIWANY BŁĄD: {e}")

if __name__ == "__main__": #gdy uruchamia sie skrypt w terminalu python przypisuje zmiennej systemowej __name__ wartosc __main__
    # uruchom tylko gdy plik zostal uruchomiony przez uzytkownika
    main()