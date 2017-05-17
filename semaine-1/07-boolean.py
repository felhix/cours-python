#! python3
# 07-boolean.py - quelques booléens, opérateurs, et comparateurs

# Voici quelques comparateurs
print(1 == 1) 							#=> True, car 1 est égal à 1
print(1 == "1") 						#=> False, car 1 est un integer, et "1" est un string
print("Hello" == "Bonjour") #=> False, car ces 2 strings sont différents
print("1" == "1") 					#=> True, car ces 2 strings sont identiques

print(1 != 2) 							#=> True, car 1 est différent de 2
print(1 != "1") 						#=> True, car 1 est un integer, et "1" est un string. Ils sont donc différents
print("Hello" != "Hello") 	#=> False, car ces deux strings sont identiques

print(0 < 1) 		#=> True, car 0 est strictement inférieur à 1
print(-10 < -9) #=> True, car -10 est sctrictement inférieur à -9
print(0 < 0) 		#=> False, car 0 n'est pas strictement inférieur à 0

print(1 > 0) #=> True, car 1 est strictement supérieur à 0

print(0 <= 1) #=> True, car 0 est inférieur ou égal à 1
print(1 <= 1) #=> True, car 1 est inférieur ou égal à 1
print(1 <= 0) #=> False, car 1 n'est pas inférieur ou égal à 0

print(1 >= 0) #=> True, car 1 est supérieur ou égal à 0
print(1 >= 1) #=> True, car 1 est supérieur ou égal à 1
print(0 >= 1) #=> False, car 0 n'est pas supérieur ou égal à 1

#ça marche aussi avec des variables
age = 26
age_dans_1_an = 27
print(age < age_dans_1_an) 			#=> True
print(age == age_dans_1_an) 		#=> False
print(age == age_dans_1_an - 1) #=> True, car 26 est égal à 27 - 1. Les opérations marchent sur les booléens

#et aussi avec les strings
first_name = "Félix"
last_name = "Gaudé"
print("Félix Gaudé" == first_name + " " + last_name) 	#=> True, car les deux renvoient à un string équivalent à "Félix Gaudé"
print(first_name == "félix") 													#=> False, car la casse compte
print(first_name == "Felix") 													#=> False, idem pour les accents

#on peut déclarer une variable en tant que booléen (c'est un data type après tout)
variable_1 = True
variable_2 = 1 > 0								#=> True
variable_3 = age < age_dans_1_an	#=> True

#on peut faire des opérations de booléns avec les opérateurs
print(1 == 1 and 2 == 2) 	#=> True, car 1 et égal à 1 ET 2 est égal à 2
print(2 > 3 and 2 == 2) 	#=> False, car l'une des deux comparaisons est False
print(2 > 3 and 2 == 1)		#=> False, car les deux comparaisons sont False
print(1 == 1 or 2 == 2) 	#=> True, car au moins une des deux comparaisons est True
print(2 > 3 or 2 == 2) 		#=> True, car au moins une des deux comparaisons est True
print(2 > 3 or 2 == 1)		#=> False, car il n'y a pas au moins une des deux comparaisons qui est True

#plus tricky, on peut conjuguer les opérateurs
print(1 == 2 or 2 == 3 or 1 == 1) 		#=> True, car au moins un des éléments de comparaisons est True
print( (1 == 1 and 2 == 3) or 1 == 2)	#=> False. On va résoudre en premier l'opération entre parenthèses (False, car l'un des deux est False) avant de la comparer avec le "or" restant. Les deux sont False, cela renvoie False.