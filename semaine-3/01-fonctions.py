#! python3
# 01-fonctions.py - quelques exemples de fonctions

#voici un exemple de fonction qui ne passe pas de paramètre
def print_three_times_hello():
	print("Hello !" * 3)

#voici comment exécuter une fonction
print_three_times_hello()

#voici un exemple de fonction qui passe un type de donnée en paramètre
def to_the_square(number):
	return number ** 2

#voici comment exécuter une fonction
random_number = 2
to_the_square(random_number) # 4

#voici un exemple de fonction qui passe plusieurs arguments
def multiply(number1, number2):
	return number1 * number2

#voici comment exécuter une fonction
random_number1 = 2
random_number2 = 3
multiply(2,3) # 6


# les fonctions sont bien pour refactoriser un programme et le rendre plus lisible. Voici par exemple un programme qui demande un nombre au user et qui affiche son carré
def ask_number_to_user():
	number = int(input("Dis un chiffre : "))
	return(number)

def square_number_and_print_it(number):
	square = number ** 2
	print("Le carré est : " + str(square))

def run_program(): # je définis une fonction qui embarque tout le programme
	number = ask_number_to_user()
	square_number_and_print_it(number)

run_program() # j'exécute la fonction qui embarque le programme : ça exécute le programme
