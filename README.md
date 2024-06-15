# Chess Engine in Python (using arcade)

## Projekt powstał na zaliczenie kursu 'Python 2' na kierunku Informatyka w Uniwersytecie Dolnośląskim DSW we Wrocławiu przez studenta 1 roku Informatyki (Mateusz Sujewicz, nr indeksu: 52796)


Ten projekt został stworzony i był rozwijany z myślą o wsparciu gry przeciwko botowi (z użyciem sztucznej inteligencji, czy to w formie algorytmu szachowego czy na bazie systemu AI-generated response'ów). 
Żaden z botów nie został jeszcze niestety zaimplementowany, wbrew temu co mówi nazwa projektu, jednak w planach mam dodanie takich funkcjonalności w ramach jego prywatnego rozwoju.


Na tym etapie jednak stworzony został cały silnik do gry w szachy, zorganizowany tak, by można było grać dwoma graczami przeciwko sobie, a w przyszłości modyfikować własne zachowania graczy-botów. Uporządkowano również 
(w mniejszym lub większym stopniu) strukturę danych projektu, tak, by poszczególne jego części w miarę przejrzysty sposób komunikowały się ze sobą (Board Interface - Board-Game channel, Game Interface - Game-Main channel: bardzo uproszczony).
Nieliczne wyjątki na obecnym etapie jednak obejmują brak roszad (Bicie w przelocie występuje i powinno działać zgodnie z regułami gry) oraz graficzny interfejs użytkownika, reprezentowany w terminalu, aczkolwiek z naciskiem na brak 
automatycznego obracania planszy zgodnie z kolorem aktywnego gracza.


## Wykorzystane technologie: 
Python3.12
bbuilt-in moduły: re, enum


## Zastosowane praktyki:
 - podział na klasy i moduły
 - dziedziczenie wspierające organizację klas
 - własne wyjątki w celu lepszego zarządzania różnymi rodzajami błędnych ruchów w szachach oraz ułatwienia komunikacji w interfejsie Game-Main (własne komunikaty obsłużonych wyjątków jako komunikaty podające użytkownikowi przyczynę błędu, 
umieszczone w jednym pliku chess_exceptions.py)
 - tworzenie pojedynczych kopii obiektów - pionków szachowych, zamiast każdej instancji na każdym polu - ma to na celu ograniczenie niepotrzebnego zużycia zasobów pamięciowych przez dane, które są wspólne dla wszystkich pionków tego rodzaju 
(z wyjątkiem podwojonych kopii wzgledem kolorów) - pozycje pionków przechowywane są przez obiekt klasy Board jako wskaźniki na pionki
 - numerajca ID pionków w celu minimalnej optymalizacji czasu sprawdzania rodzaju pionków
 - organizacja całej gry w sposób charakterystyczny dla silników zarządzania grami (wywoływanie aktualizacji i rysowania wszystkich komponentów gry, przechowywanie stanu aktualnej rozgrywki szachowej)
