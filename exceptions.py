class KsiazkaNiedostepnaError(Exception):
    # dzieki temu ze dziedziczmy po klasie excpetion to system pozwala rzucac blad za pomoca raise w library.py + wylapywanie w try-except
    def __init__(self, title): # konstruktor bledu
        super().__init__(f"BŁAD! Niestety, książka '{title}' jest już wypożyczona lub nie ma jej w bazie.")
        # super() zwraca obiekt rodzica uruchom konstruktor z klasy rodzica i wywolaj ten tekst - lapiemy blad jako zmienna e (pod nia kryje sie tekst)

