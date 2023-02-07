#Créé par : Ardox
#Le : 07/02/2023
#pour : AxOS

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Quelle operation voulez vous faire?")
print("1.Addition")
print("2.Soutraction")
print("3.Multiplication")
print("4.Division")

while True:
    choice = input("Entrez votre choix(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Entrez le premier nombre: "))
            num2 = float(input("Entrez le second nombre: "))
        except ValueError:
            print("Entrée invalide. Vouillez réesayer")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    
        next_calculation = input("Voulez vous continuer ? (O/N): ")
        if next_calculation == "n" or "N":
          break
    else:
        print("Entrée invalide")