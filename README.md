# Chess Engine in Python (using arcade)
---

## Projekt powstał na zaliczenie kursu 'Programowanie w języku Python 2' na II semestrze kierunku Informatyka w Uniwersytecie Dolnośląskim DSW we Wrocławiu
Ten projekt został stworzony i był rozwijany z myślą o wsparciu gry przeciwko botowi (z użyciem sztucznej inteligencji, czy to w formie algorytmu szachowego czy na bazie systemu AI-generated response'ów).

Na tym etapie utworzony został działający (niemal w pełni - za wyjątkiem roszad, patu i zaawansowanych promocji) silnik szachowy, a także możliwość grania przeciwko botowi opartego na technologii Stockfish.

---
## Wykorzystane technologie: 
- Python3.12
- Built-in moduły: re, enum
- Moduły chess oraz chess.engine
- Zewnętrzne oprogramowanie Stockfish


---
## Zastosowane praktyki:
 - podział na klasy i moduły
 - dziedziczenie wspierające organizację klas
 - własne wyjątki w celu lepszego zarządzania różnymi rodzajami błędnych ruchów w szachach oraz ułatwienia komunikacji w interfejsie Game-Main (własne komunikaty obsłużonych wyjątków jako komunikaty podające użytkownikowi przyczynę błędu, 
umieszczone w jednym pliku chess_exceptions.py)
 - tworzenie pojedynczych kopii obiektów - pionków szachowych, zamiast każdej instancji na każdym polu - ma to na celu ograniczenie niepotrzebnego zużycia zasobów pamięciowych przez dane, które są wspólne dla wszystkich pionków tego rodzaju 
(z wyjątkiem podwojonych kopii wzgledem kolorów) - pozycje pionków przechowywane są przez obiekt klasy Board jako wskaźniki na pionki
 - numerajca ID pionków w celu minimalnej optymalizacji czasu sprawdzania rodzaju pionków
 - organizacja całej gry w sposób charakterystyczny dla silników zarządzania grami (wywoływanie aktualizacji i rysowania wszystkich komponentów gry, przechowywanie stanu aktualnej rozgrywki szachowej)
 - implementacja bota szachowego z wykorzystaniem zewnętrznych i wewnętrznych technologii (Stockfish i moduł chess.engine)


---
**Autor projektu:**
Mateusz Sujewicz, student II semestru Informatyki na Uniwersytecie Dolnośląskim DSW we Wrocławiu
