#! python3
# 10-boucle-while.py - comment marche la boucle while

#une boucle while dit "tant que cette condition n'est pas respectée, faire ceci"
password = "azerty"
print("Écris ton mot de passe stp 🙊")
input_user = input()

while input_user != password:	#tant que le mot de passe rentré n'est pas égal à "azerty", le programme exécutera les ligne 10 et 11
	print("Oups mdp erroné ! Retente stp")
	input_user = input()
print("Bravo, bienvenue !!")	#le programme n'arrivera pas à cette ligne tant qu'il sera bloqué dans la boucle