#! python3
# 08-if-else-elif.py - comment faire marcher une condition si


#voici comment marche une condition en si
statement = True	# déclare une variable égale à un booléen True
if statement:		# si cette condition est True, alors exécutez le bloc ci-dessous
	print("C'est vrai !!!")	#le bloc est indenté (appuyer sur "TAB" pour indenter un bloc), c'est ce que l'on exécutera si jamais la condition est remplie
print("Je sors du bloc, on reprend une activité normale !") #l'indentation redevenue normale, c'est comme dire au programme "sors de cette condition"


#comme la notion de bloc peut paraitre déroutante, voici un exemple de blocs dans un bloc
if 1 == 1:
	print("Je suis dans le bloc qui dépend du if de la ligne 12")
	print("Moi aussi car j'ai le même niveau d'indentation")
	if 1 == 0:
		print("Je suis dans un autre niveau d'indentation, je dépend du if de la ligne 15")
	print("Je dépend du if de la ligne 12 car j'ai son niveau d'indentation")
	if 0 == 0:
		if 1 > 0:
			print("Je dépend du if de la ligne 19")
		print("Je viens de mettre fin au if de la ligne 19 car j'ai pris un niveau d'indentation moins grand")

print("Je viens de mettre fin à ce bloc bien complexe, et par ailleurs je ne dépend pas de ce bloc")


#on peut mettre "else" (sinon) après un if, pour exécuter une action si jamais le if est False
if 1 == 1:
	print("C'est vrai")
else: #else créé un nouveau bloc, il revient au niveau d'indentation du if de la ligne 28 pour pouvoir s'exécuter
	print("FAUX !")


#aussi, vous pouvez utiliser elif qui équivaut à sinon si
age = 100	#tu as 100 ans
if age < 10:	#si tu as moins de 10 ans
	print("Tu es très jeune !")	# tu es jeune
elif age > 90:	#sinon si tu as plus de 90 ans
	print("Tu es très vieux !")	#tu es très vieux
else:	#sinon
	print("Tu es ni jeune, ni vieux")	#tu es ni jeune, ni vieux


#l'avantage de elif est quand vous pouvez mettre plein de cas à la suite. Utile quand vous avez plein de cas différents pour votre condition
city = "Trifouillis-en-bled"
if city == "Paris":
	print("Waw la Tour Eiffel")
elif city == "Lyon":
	print("Meh")
elif city == "Lille":
	print("Le welsh c'est trop bon")
elif city == "Bordeaux":
	print("La plus belle ville au monde")
elif city == "Toulouse":
	print("La ville rose")
elif city == "Marseille":
	print("Pastis à ma santé !")
else:
	print("Je ne connais pas (encore) cette ville !")