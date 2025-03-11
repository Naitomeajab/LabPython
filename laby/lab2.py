import random
def task1():
    set_gene1 = set(['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
                    'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                    'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
    set_gene2 = set(['SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
                    'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421', 'ANGC3', 'WELNT14', 'EOO11',
                    'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
    set_gene3 = set(['SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3','GALNT14', 'ERCC11',
                    'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT15', 'EOO1',
                    'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'])
    #part A
    print(f"Shared genes: {set_gene1.intersection(set_gene2.intersection(set_gene3))}")
    #part B
    print(f"Genes for patient 1 and 2: {set_gene1.intersection(set_gene2)}")
    print(f"Genes for patient 1 and 3: {set_gene1.intersection(set_gene3)}")
    print(f"Genes for patient 2 and 3: {set_gene2.intersection(set_gene3)}")
    #part C
    print(f"Genes exclusive for patient 1: {set_gene1.difference(set_gene2.union(set_gene3))}")
    print(f"Genes exclusive for patient 2: {set_gene2.difference(set_gene1.union(set_gene3))}")
    print(f"Genes exclusive for patient 3: {set_gene3.difference(set_gene1.union(set_gene2))}")

def task2():
    lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
                    'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                    'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']
    if lista_gene1.count("FGFR4"):
        print(f"FGFR4 {lista_gene1.index('FGFR4')}")
    else:
        print("FGFR4 is not found")
    if lista_gene1.count("FGERA4"):
        print(f"FGERA4 {lista_gene1.index('FGERA4')}")
    else:
        print("FGERA4 is not found")
def task3():
    text = ("Ale nie wszystkim ludziom maszyny pomogą skupić się na jakości. Istnieją pewne nudne czynności, przy "
            "których maszyny wypadają bardzo źle. Armia kiepsko opłacanych pracowników po cichu wykonuje więc te prace. "
            "Na przykład przy projekcie Amazon Mechanical Turk– stronie prowadzonej przez internetowego sprzedawcę, "
            "gdzie zleceniodawcy płacą za proste (choć pewnie nudne) drobne zadania, które dla maszyn są jednak zbyt "
            "skomplikowane. Chodzi o transkrypcję klipów audio, tagowanie zdjęć przy użyciu odpowiednich słów kluczy, "
            "przepisywanie skopiowanych rachunków na arkusze. Amazon nazywa je „zadaniami dla ludzkiej inteligencji” "
            "lub HIT-ami (ang. Human Intelligence Task), a zleceniodawcy płacą kilka centów za sztukę. Nazwa Mechanical "
            "Turk pochodzi od sztucznej maszyny do gry w szachy z XVIII wieku: choć wyglądała jak robot, "
            "w środku schowany był w tajemnicy człowiek.")
    text.strip()
    #part A
    print(f"In above paragraph, word 'Emma' has appearade {text.count('Emma')} times.")
    #part B
    text = text.upper()
    print(text)
    #part C
    word_list = text.split(" ")
    print(word_list)
    #part D
    sentence_list = text.split(". ")
    print(sentence_list)
    print(f"There is {len(sentence_list)} sentences in the text")

def task4():
    number = int(input("Input your number: "))
    if number % 2 == 0:
        print(f"Number {number} is even")
    else:
        print(f"Number {number} is odd")
def task5():
    max_score = 15
    score = int(input("Input your score"))
    score_in_percentage = (score/max_score) * 100
    match score_in_percentage:
        case _ if 51 <= score_in_percentage <= 60:
            grade = 3
        case _ if 61 <= score_in_percentage <= 70:
            grade = 3.5
        case _ if 71 <= score_in_percentage <= 80:
            grade = 4
        case _ if 81 <= score_in_percentage <= 90:
            grade = 4.5
        case _ if 91 <= score_in_percentage:
            grade = 5
        case _ if 101 <= score_in_percentage:
            grade = "score given is out of allowed range (0-15)"
        case _:
            grade = 2
    print(f"Your grade is: {grade}")
def task6():
    limit_range = int(input("Input your sequence limit: "))
    sum = 0
    for x in range(1, limit_range+1):
        sum += (1/x)
    print(f"Final result is: {sum}")
def task7():
    for x in range(1,11):
        print(f"root of {x} is: {x ** (1/2)}")
def task8():
    a = int(input("Provide number a: "))
    b = int(input("Provide number b: "))
    c = int(input("Provide number c: "))
    discriminant = (b ** 2) - (4 * a * c);
    if discriminant > 0:
        root1 = (-b + (discriminant ** 0.5))/(2 * a)
        root2 = (-b - (discriminant ** 0.5)) / (2 * a)
        print(f"Two roots: {root1} and {root2}")
    elif discriminant == 0:
        root = (-b)/(2 * a)
        print(f"Root: {root}")
    else:
        print(f"There are no roots, discriminant is negative")
def task9():
    correct_numbers = [];
    for number in range (1,1001):
        is_allowed = True
        for digit in str(number):
            if int(digit) % 2 == 1:
                is_allowed = False
        if is_allowed:
            correct_numbers.append(str(number))
    print(",".join(correct_numbers))
def task10():
    while True:
        try:
            x = int(input("Provide number X: "))
            y = int(input("Provide number Y: "))
        except ValueError:
            print("Invalid input!")
            continue
        if x == 0 or y == 0: break
        print(f"{x} times {y} is {x*y}")
def task11():
    passes = ["CirnoIsBad", "Kurumi"]
    pass_attempt = input("Provide password: ")
    if (passes.count(pass_attempt) == 1):
        print("Kacper Jabłoński")
    else:
        print("Incorrect")
def task12():
    allowed_numbers = []
    for x in range(1,101):
        rand_number = random.randint(1,9001)
        if rand_number % 2 == 1:
            allowed_numbers.append(str(rand_number))
    print(",".join(allowed_numbers))
def task13():
    passes = ["CirnoIsBad", "Kurumi"]
    pass_attempt = input("Provide password: ")
    print("Kacper Jabłoński") if (passes.count(pass_attempt) == 1) else print("Incorrect")
def task14():
    a = int(input("Provide A: "))
    b = int(input("Provide B: "))
    c = int(input("Provide C: "))
    if (a % 2 == 0 and b % 2 == 0 and c % 2 == 0):
        task14_function(a, b, c)
    else:
        print("Incorrect numbers, they must even numbers")
def task14_function(x, y, z):
    print(f"{x} x {y} x {z} is equal to {x*y*z}")


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
        print("12. zadanie 12")
        print("13. zadanie 13")
        print("14. zadanie 14")

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
        elif choice == "14":
            task14()
        elif choice == "0":
            break
        else:
            print("Błędny wybór.")

if __name__ == "__main__":
    menu()