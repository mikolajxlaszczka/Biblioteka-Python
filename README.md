Mini Biblioteka w Pythonie  

1. OPIS DZIAŁANIA

Konsolowy system do zarządzania zbiorem książek w bibliotece , w pracy wykorzystuje prog. obiektowe oraz podział na moduły
Zakres działania programu:
- Dodawanie nowych książek (+ walidacja roku wydania - regex)
- System wypożyczania i zwracania + obsługa wyjątków
- Wyświetlenie za pomocą generatora co oszczędza pamięć
- Możliwośc wyszukiwania książek po kategorii (comprehension + lambda)

Wszystkie operacje sa logowane przez dekorator - stan jest zapisywany do pliku [dane.json] przez serializacje i context menager-a


2. URUCHOMIENIE
    1) Zainstalowanie środowiska Python 3.6+
    2) Otworzenie terminalu w katalogu z rozpakowanym projektem
    3) Uruchomienie programu - odpowiednio  dla systemu operacyjnego :
        - Windows : ```bash , python main.py
        - MacOS : python3 main.py
