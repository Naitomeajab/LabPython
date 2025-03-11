import stars, sil
from functools import reduce
def task1():
    letters_in_name = ["K", "a", "c", "p", "e", "r"]
    completed_name = lambda x: "".join(x)
    print(completed_name(letters_in_name))
def task2():
    full_name = "Kacper Jabłoński"
    separate = lambda x: x.split()
    words = separate(full_name)
    print(f"{full_name} in seperate words: {words}")
    toLetters = lambda word: list(word)
    for word in words:
        print(f"{word} spread to letters is: {toLetters(word)}")
def task3():
    word = input("Provide word: ")
    letter = input("Which letter to find?: ")
    task3_findLetter(word, letter)
def task3_findLetter(word, letter):
    print(f"Found letter '{letter}' at index of {word.index(letter)}")
def task4():
    logins = []
    passwords = []
    while True:
        user_input = input(f"Provide login: ")
        if user_input == "STOP": break
        logins.append(user_input)
        user_input = input(f"Provide pass: ")
        passwords.append(user_input)
        print("data has been updated")
    data_dictionary = {}
    for login, passw in zip(logins, passwords):
        data_dictionary.update({
            login: passw
        })
    print(data_dictionary)
    return 0
def task5():
    #letter E
    stars.horizontal(8)
    stars.vertical(3)
    stars.horizontal(8)
    stars.vertical(3)
    stars.horizontal(8)
    print("\n\n=======\n")
    #letter L
    stars.vertical(10)
    stars.horizontal(8)
    return 0
def task6():
    n = int(input("Provide N: "))
    k = int(input("Provide K: "))
    newton = sil.silnia(n)/(sil.silnia(k)*sil.silnia(n-k))
    print(f"Newton symbol is: {newton}")
    return 0
def task7():
    numbers = []
    for i in range (1, 1001):
        numbers.append(i)
    numbers = filter(lambda x: x%2 == 0, numbers)
    print(list(numbers))
    return 0
def task8():
    numbers = []
    for i in range (1, 11):
        numbers.append(i)
    multiplication_all = reduce(lambda x, y: x * y, numbers)
    print(multiplication_all)
    return 0
def task9():
    numbers = []
    for i in range (2000,3201):
        numbers.append(i)
    numbers = filter(task9Filter, numbers)
    print(list(numbers))
    return 0
def task9Filter(x):
    if x % 7 == 0 and x % 5 != 0: return True
    else: return False
def task10():
    numbers = []
    for i in range (2000,3201):
        numbers.append(i)
    numbers = filter(lambda x: x % 7 == 0 and x % 5 != 0, numbers)
    print(list(numbers))
    return 0
def task11():
    try:
        userInput = input("Choose letter 'E' or 'L': ")
    except ValueError:
        print("INCORRECT VALUE YOU CIRNO-BRAIN")
        return 0
    userInput.upper()
    if userInput == "E":
        stars.horizontal(8)
        stars.vertical(3)
        stars.horizontal(8)
        stars.vertical(3)
        stars.horizontal(8)
    if userInput == "L":
        stars.vertical(10)
        stars.horizontal(8)
    return 0

def menu():
    while True:
        print("\n=== Labolatorium 2 ===")
        print("1. Zadanie 1")
        print("2. Zadanie 2")
        print("3. zadanie 3")
        print("4. zadanie 4")
        print("5. zadanie 5")
        print("6. zadanie 6")
        print("7. zadanie 7")
        print("8. zadanie 8")
        print("9. zadanie 9")
        print("10. zadanie 10")
        print("11. zadanie 11")

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
        elif choice == "0":
            break
        else:
            print("Błędny wybór.")

if __name__ == "__main__":
    menu()