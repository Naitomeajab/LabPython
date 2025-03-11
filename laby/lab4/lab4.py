import os
def task1():
    print(os.getcwd())
    userInput = str(input("Give the correct path to folder: "))
    os.chdir(userInput)
    print(os.getcwd())
    print(f"Lista danych: {os.listdir(os.getcwd())}")
def task2():
    inputPath = str(input("Give the correct path to folder: "))
    while True:
        userInput = str(input("Should I change the folder? "))
        userInput.lower()
        if userInput == "yes": break
    task2ChangeWorkSpace(inputPath)
    print(os.listdir(os.getcwd()))
def task2ChangeWorkSpace(path):
    os.chdir(path)
def task3():
    return 0
def task4():
    return 0
def task5():
    return 0
def task6():
    return 0
def task7():
    return 0
def task8():
    return 0
def task9():
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
        elif choice == "0":
            break
        else:
            print("Błędny wybór.")

if __name__ == "__main__":
    menu()