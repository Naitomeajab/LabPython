import os

lab_list = {
    "1": "lab1/lab1.py",
    "2": "lab2/lab2.py",
    "3": "lab3/lab3.py",
    "4": "lab4/lab4.py"
}

def main_menu():
    while True:
        print("===Programowanie w Python'ie===")
        for key, project in lab_list.items():
            print(f"{key}. {project}")

        print("0. zakończ")
        choice = input("Wprowadź numer: ")

        if choice == "0":
            break

        elif choice in lab_list:
            open_project(lab_list[choice])
        else:
            print("Niepoprawny wybór.")

def open_project(lab_number):
    file = os.path.join("laby", lab_number)
    if os.path.exists(file):
        os.system(f"python {file}")
    else:
        print("Nie znaleziono pliku")

if __name__ == "__main__":
    main_menu()