# #Zadanie 1
# Utwórz listę z imionami (conajmniej 10 imion, część powinna się powtarzać)
# określ indeks (numer wiersza) w której znajduje się imie osoby, nazwę osoby podaje użytkownik
# ile osób o imieniu wskazanym przez użytkownika znajduje się na liście
# dołącz nowe imie do listy do końca listy
# dołącz nowe imię jako 3 pozycję na liście
# posortuj obiekty w liście, usuń ostatni element z listy
# utwórz nową listę z 3 imionami i dołącz do listy
def task1():
    name_list = ["Anna", "Piotr", "Katarzyna", "Michał", "Anna", "Jakub", "Piotr", "Zofia", "Michał", "Aleksandra"]
    print(name_list)

    name_choice = input("wprowadź imię osoby: ")
    print(f"Pierwsze wystąpienie imienia {name_choice} to {name_list.index(name_choice)}")
    print(f"Liczba osób z tym imieniem to {name_list.count(name_choice)}")

    name_list.append("Maryla")
    name_list.insert(2, "Marcel")
    name_list.sort()
    name_list.pop(-1)
    name_list_aux = ["Piotr", "Kacper", "Aleksander"]
    name_list.extend(name_list_aux)
    print(name_list)

######################Zadanie 2
# Utwórz słownik zawierający  trzy klucze: imie, nazwisko, wiek
# jako wartości w/w kluczy wpisz listy 3-elementowe zawierające dowolne dane osobowe
# następnie wyświetl kompletne dane osoby o numerze wskazanej przez użytkownika

def task2():
    main_dictionary = {
        "imie": ["Anna", "Jan", "Katarzyna"],
        "nazwisko": ["Kowalska", "Nowak", "Wiśniewska"],
        "wiek": [25, 30, 28]
    }
    print(main_dictionary)
    choice = int(input("Wybierz numer osoby (0, 1, 2): "));
    print(f"Imie: {main_dictionary['imie'][choice]}\n Nazwisko: {main_dictionary['nazwisko'][choice]}\n Wiek: {main_dictionary['wiek'][choice]}")

    ######################Zadanie 2.1
    # Do poprzednio utworzonego słownika dodaj nowy klucz o nazwie "kierunek_studiów", wartość w/w klucza dowolna
    # wskazana przez użytkownika

    user_input = input("Dodaj kierunek studiów")
    main_dictionary.update({
        "kierunek_studiow": user_input
    })
    print(main_dictionary)

    ######################Zadanie 2.2
    # Wyświetl nazwy kluczy poprzednio utworzonego słownika, oraz ilość jego elementów
    # ###########################################

    print(f"{main_dictionary.keys()}\n{main_dictionary.values()}")

## 3. Sprawdź wynik działań
# 0 > 1
# 0 <= 1
# 0 >= 1
# 1 == 0
# 1 == 1
# 1 != 0
# 1 != 1
def task3():
    print(0 > 1)
    print(0 <= 1)
    print(0 >= 1)
    print(1 == 0)
    print(1 == 1)
    print(1 != 0)
    print(1 != 1)

## 4. Oblicz wyrażenie 2x+5y   gdzie: x,y to dowolne dwie liczby które podaje użytkownik (w konsoli)
def task4():
    x = int(input("Podaj X: "))
    y = int(input("Podaj Y: "))
    print(f"Wynik wyrażenia: {2*x} + {5*y} = {(2*x) + (5*y)}")
## 5. Wyświetl zdanie "Jestem a b mam c lat studiuję d",
## gdzie : a-imie, a-nazwisko, c-liczba, d-kierunek studiów są dowolne zmienne które podaje użytkownik (wczytywane z klawiatury)
def task5():
    name = input("Imie: ")
    surname = input("Nazwisko: ")
    age = input("Wiek: ")
    studies = input("Kierunek studiów: ")
    print(f"Jestem {name} {surname} mam {age} lat studiuję {studies}")
## 6. Sprawdź/porównaj czy 1+2+10+20000001+4+347586970885 jest równa 321784560456434534646
def task6():
    sum = 1+2+10+20000001+4+347586970885
    print(f"1+2+10+20000001+4+347586970885 = {sum}\n"
          f"Czy {sum} jest równe 321784560456434534646 ?\n"
          f"{sum == 321784560456434534646}")
## 7. Sprawdź czy suma dowolnych dwóch liczb podanych przez użytkownika jest liczbą parzystą czy nieparzystą wyświetl właściwy komunikat
##   użyj operatora modulo % który zwraca resztę z dzielenia  np. 5%2   czyli 2 reszta 0
def task7():
    x = int(input("Wprowadź pierwszą liczbę: "))
    y = int(input("Wprowadź drugą liczbę: "))
    sum = x+y
    print(f"Suma {x} i {y} to {sum}. Czy {sum} jest parzystą liczbą? {sum % 2 == 0}")
## 8. Utwórz prosty kalkulator dla 2 zmiennych podanych przez użytkownika, który obliczy: sumę, różnicę,
## iloczyn, iloraz, potęgę tych liczb, nie zapomnij o stosownych komentarzach informacyjnych dla użytkownika.
def task8():
    x = int(input("Wprowadź pierwszą liczbę: "))
    y = int(input("Wprowadź drugą liczbę: "))
    while True:
        print("1. Suma")
        print("2. Różnica")
        print("3. Iloczyn")
        print("4. Iloraz")
        print("5. Potęga")
        choice = input("Wybierz operację: ")
        if choice == "1":
            print(f"{x} + {y} = {x+y}")
        elif choice == "2":
            print(f"{x} - {y} = {x-y}")
        elif choice == "3":
            print(f"{x} * {y} = {x*y}")
        elif choice == "4":
            print(f"{x} / {y} = {x/y}")
        elif choice == "5":
            print(f"{x} ^ {y} = {x^y}")
        else:
            print("niepoprawna wartość")
## 9. Dla dowolnego x sprawdź wynik działań (x > 1 and x < 13) oraz (x != 5 or x < 0)
def task9():
    x = int(input("Wprowadź liczbę: "))
    print(f"{x} > 1 AND {x} < 13? {(x > 1) & (x < 13)}")
    print(f"{x} != 5 OR {x} < 0? {(x != 5) | (x < 0)}")
# Zadania dodatkowe:
# 10. Wykonaj mini ankietę tj. poproś użytkownika o następujące informacje: imie, nazwisko, wiek, zadaj mu pytania: "Czy zdrowo się odżywiasz?",
# , "Czy lubisz sport?" i dodatkowo 3 inne własne. Po uzyskaniu wszystkich odpowiedzi wyświetl ich podsumowanie.
def task10():
    name = input("Imie: ")
    surname = input("Nazwisko: ")
    age = input("Wiek: ")
    while True:
        is_eating_healthy = input("Czy zdrowo się odrzywiasz? y/n: ")
        if is_eating_healthy == "y": break
        if is_eating_healthy == "n":
            is_eating_healthy = ""
            break
        else:
            print("Niepoprawna odpowiedź.")
    while True:
        is_liking_sport = input("Czy lubisz sport? Y/N: ")
        if is_liking_sport == "y": break
        if is_liking_sport == "n":
            is_liking_sport = ""
            break
        else:
            print("Niepoprawna odpowiedź.")
    while True:
        is_liking_warhammer = input("Czy lubisz uniwersum Warhammer 40k? y/n: ")
        if is_liking_warhammer == "y": break
        if is_liking_warhammer == "n":
            is_liking_warhammer = ""
            break
        else:
            print("Niepoprawna odpowiedź.")
    while True:
        is_liking_paradox = input("Czy lubisz developera Paradox Interactive? y/n: ")
        if is_liking_paradox == "y": break
        if is_liking_paradox == "n":
            is_liking_paradox = ""
            break
        else:
            print("Niepoprawna odpowiedź.")
    while True:
        is_liking_cirno = input("Czy lubisz Cirno? y/n: ")
        if is_liking_cirno == "n":
            is_liking_cirno = ""
            break
        else:
            print("Niepoprawna odpowiedź, dozwolona: n.")
    print(f"Imię: {name}\n"
          f"Naziwsko: {surname}\n"
          f"Wiek: {age}\n"
          f"Zdowo się odrzywia: {bool(is_eating_healthy)}\n"
          f"Lubi sport: {bool(is_liking_sport)}\n"
          f"Lubi uniwersum Warhammer'a: {bool(is_liking_warhammer)}\n"
          f"Lubi paradox: {bool(is_liking_paradox)}\n"
          f"Lubi Cirno: {bool(is_liking_cirno)}") #Zawsze false
# 11. Twoim zadaniem jest przygotowanie uniwersalnego i profesjonalnego życiorysu, złożonego z 5-ciu zdań, które wyświetlisz na ekranie
# Użytkownik wpisuje tylko swoje imie, nazwisko, wiek, zawód, miejsce urodzenia, zainteresowania i ... życiorys jest gotowy.
def task11():
    name = input("Imie: ")
    surname = input("Nazwisko: ")
    age = input("Wiek: ")
    employment = input("Zawód: ")
    place_of_origin = input("Miejsce urodzenia: ")
    interests = input("Zainteresowania: ")
    print(f"Nazywam się {name} {surname}, mam {age} lat, i jestem profesjonalistą w zawodzie {employment}. "
          f"Urodziłem się w {place_of_origin}."
          f"Jestem osobą, która stawia na ciągły rozwój zawodowy i osobisty. Moją pasją jest {interests}, "
          f"a w pracy stawiam na wysoką jakość oraz efektywność.")
# 12. Przygotuj dla dziecka, które uczy się czytać zestaw sylab do nauki, ale zrób to inteligentnie tj.
# dziecko wpisuje na klawiaturze 1 spółgłoskę a Ty dodajesz do niej odpowiednie samogłoski i wyświetlasz całość na ekranie
def task12():
    vowels_list = ["A", "E", "I", "O", "U", "Y", "Ó"]
    while True:
        prefix = input("Wprowadź spółgłoskę: ")
        if vowels_list.count(prefix) == 0 and len(prefix) == 1:
            break
        else:
            print("Niepoprawna wartość")
    print(f"Sylaby dla {prefix}\n")
    iterator = 0
    while iterator < len(vowels_list):
        print(f"{prefix}{vowels_list[iterator]}")
        iterator += 1
# 13. Użytkownik podaje imie, sprawdź czy to imie to Janusz lub Grażyna)
def task13():
    name = input("Imie: ")
    if name == "Janusz" or name == "Grażyna": result = ""
    else: result = "NIE"
    print(f"Twoje imie to {result} Janusz albo Grażyna")

def menu():
    while True:
        print("\n=== Labolatorium 1 ===")
        print("1. Zadanie 1")
        print("2. Zadanie 2")
        print("3. zadanie 3")
        print("4. zadanie 4 - 2x+5y")
        print("5. zadanie 5 - Jestem a b mam c lat studiuję d")
        print("6. zadanie 6")
        print("7. zadanie 7")
        print("8. zadanie 8")
        print("9. zadanie 9")
        print("10. zadanie 10")
        print("11. zadanie 11")
        print("12. zadanie 12")
        print("13. zadanie 13")

        print("0. Back to Main Menu")

        choice = input("Wybierz zadanie: ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "5":
            task5()
        elif choice == "6":
            task6()
        elif choice == "7":
            task7()
        elif choice == "8":
            task8()
        elif choice == "9":
            task9()
        elif choice == "10":
            task10()
        elif choice == "11":
            task11()
        elif choice == "12":
            task12()
        elif choice == "13":
            task13()
        elif choice == "0":
            break
        else:
            print("Błędny wybór.")


if __name__ == "__main__":
    menu()