#! python3
# 03-variables.py - montre les trois premiers types de données

#Voici quelques integer, ou entier relatifs
integer_1 = 1
integer_2 = 0 		#un relatif peut être égal à 0
integer_3 = 4
integer_4 = -12 	#un relatif peut être négatif
integer_5 = 1 + 5 	#il est possible d'effectuer des opérations dessus

#Il y a aussi les floats, ou rééls
float_1 = 1.0 	#dès que vous ajoutez un virgule avec un chiffre derrière un nombre, l'ordinateur comprend que c'est un float
float_2 = -2.5
float_3 = 1/3	#une division de relatifs en fait un float

#enfin, il y a les strings, ou chaines de caractères. Une erreur commune (qui arrive même à moi) est d'oublier les guillemets. Pour qu'un programme comprenne que vous parlez d'un string, mettez TOUJOURS des guillemets
string_1 = "Voici un string"
string_2 = 'Cela marche aussi avec les apostrophes'
string_3 = "mot" # un string peut ne faire qu'un mot
string_4 = "      " #ou une suite de white spaces
string_5 = "1" #un chiffre entre guillemets sera considéré comme un string. Sans les guillemets, ce sera considété comme un integer.