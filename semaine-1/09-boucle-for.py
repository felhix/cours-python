#! python3
# 09-boucle-for.py - comment marche la boucle for

# for en Python permet de boucler sur une fonction en fonction de paramètres. Voici comment elle se construit : 
# for variable_locale in ce_sur_quoi_on_boucle:
#		lignes_de_bloc


# au début nous allons apprendre à boucler sur la fonction range(). Voici comment boucler 5 fois un print("Bonjour") :
for variable_locale in range(0,5): #on va boucler 5 fois car l'ordi prend la portée qu'est 5-0
	print("Bonjour")
print("Idem que pour if, une fois sorti du bloc en reprenant une identation normale, on n'est pas considéré dedans, donc cette ligne ne bouclera pas")


#la variable locale ne peut être utilisée que dans le bloc de la boucle for, mais elle sera super pratique
for numero_de_la_boucle in range(0,5):
	print("Voici le numéro de la boucle : " + str(numero_de_la_boucle)) #=> affiche de 0 à 4


#un ordinateur compte toujours à partir de 0. Mais on peut changer les paramètres de la fonction range pour rémédier à cela
for numero_de_boucle in range(1,6):
	print("Nouveau numéro : " + str(numero_de_boucle)) #=> de 1 à 5, coolos, non ?

#ou alors on peut changer la variable locale dans la boucle :
for numero_de_boucle in range(0,5):
	print("Nouveau numéro : " + str(numero_de_boucle + 1)) #=> de 1 à 5, coolos, non ?


#une boucle for peut s'appliquer sur certains types de données, les strings par exemple
for caractere in "Hello":
	print(caractere) #=> H - e - l - l - o
