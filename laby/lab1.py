# #Zadanie 1
# Utwórz listę z imionami (conajmniej 10 imion, część powinna się powtarzać)
# określ indeks (numer wiersza) w której znajduje się imie osoby, nazwę osoby podaje użytkownik
# ile osób o imieniu wskazanym przez użytkownika znajduje się na liście
# dołącz nowe imie do listy do końca listy
# dołącz nowe imię jako 3 pozycję na liście
# posortuj obiekty w liście, usuń ostatni element z listy
# utwórz nową listę z 3 imionami i dołącz do listy

def task1():
    print("\n=== Task 1: Addition ===")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Result: {a + b}")


def task2():
    print("\n=== Task 2: Multiplication ===")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Result: {a * b}")


def module_menu():
    while True:
        print("\n=== Module 1: Math Operations ===")
        print("1. Task 1 - Addition")
        print("2. Task 2 - Multiplication")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "0":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    module_menu()