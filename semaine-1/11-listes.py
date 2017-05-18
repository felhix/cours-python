#! python3
# 11-listes.py - la liste et quelques exemples de fonction que l'on peut faire avec


#voici comment déclarer une liste
liste_1 = [1, 2 ,3]
liste_2 = ["Bonjour", 2, 3.14, True, [1, 2], {"name": "Félix", "age": 26} ] #une liste peut avoir tout type de data type en valeur
liste_3 = [] #une liste peut être vide, ou contenir plusieurs centaines de de variables
variable = 1
liste_4 = [liste_3, variable] #une liste peut contenir des variables

#pour accéder à un élément d'une liste, il faut faire liste[index]
liste_1 = ["chat", "chien", "oiseau"]
print(liste_1[0]) #=> "chat", car l'ordinateur commence à compter à partir de zéro
print(liste_1[1]) #=> "chien"
print(liste_1[2]) #=> "oiseau"

#si liste[0] fera toujours référence au premier élément d'une liste, liste[-1] fera appel au dernier
liste_1 = ["chat", "chien", "oiseau"]
print(liste_1[-1]) #=> "oiseau"
print(liste_1[-2]) #=> "chien"

#on peut effectuer des opérations sur les valeurs d'une liste. On peut les modifier, ou bien effectuer des fonctions dessus
liste_1 = ["12", "25", "13"] # trois strings
print(liste_1[0] + liste_1[1] + liste_1[2]) #=> "122513", oups comme c'est trois strings, une addition va les concaténer
liste_1[0] = 12 # On peut les changer
liste_1[1] = int(liste_1[1])
print(liste_1[0] + liste_1[1] + int(liste_1[-1])) #=> 50

#on peut obtenir le nombre d'élements d'une liste avec len()
liste_1 = [12, 25, 13]
print(len(liste_1)) #=> 3

#on peut virer des éléments d'une liste avec del(), qui suprrime avec l'index
liste_1 = [2, 3, 4, 1, 2]
del(liste_1[1]) # del() enlève un élément d'une liste à partir de son index
print(liste_1) #=> [2, 4, 1, 2], le deuxième élément de la liste a été supprimé

#on peut aussi virer des éléments d'une liste avec remove(), qui suprrime avec la valeur
liste_1 = [2, 3, 4, 1, 2]
liste_1.remove(2) # remove() enlève un élément d'une liste à partir de sa valeur
print(liste_1) #=> [3, 4, 1, 2], il reste un élément avec une valeur de 2 car la fonction remove() n'enlève la première occurence sur laquelle elle tombe

#on peut voir si une valeur est dans une liste ou pas avec in et not in
liste_1 = ["chat", "chien", "oiseau", "poulet"]
print("chat" in liste_1) #=> True
print("cheval" in liste_1) #=> False
print("cheval" not in liste_1) #=> True
print("oiseau" not in liste_1) #=> False

#on peut ajouter un élément dans une liste avec append()
liste_1 = ["chat", "oiseau", "chien", "lion"]
liste_1.append("poisson") # ajout de "poisson" en dernière position
print(liste_1) #=> ["chat", "oiseau", "chien", "lion", "poisson"]

#on peut aussi ajouter un élément dans une liste avec insert(), qui permet de choisir l'index de l'élément choisi
liste_1 = ["chat", "oiseau", "chien", "lion"]
liste_1.insert(1, "poisson") #ajout de "poisson" à l'index 1, soit en deuxième position
print(liste_1) #=> ["chat", "poisson", "oiseau", "chien", "lion"]
liste_1.insert(4, "tigre")
print(liste_1) #=> ["chat", "poisson", "oiseau", "chien", "tigre" "lion"]


#for est très cool avec les listes pour passer sur tous les éléments
liste_1 = ["chat", "oiseau", "chien", "poulet"]
for element in liste_1:
	print(element) # affiche les éléments de la liste un par un

#avec for index in range(len(liste)), on modifier les éléments de la liste
liste_1 = ["chat", "oiseau", "chien", "poulet"]
for index in range(len(liste_1)):
	liste_1[index] = "canard" # transforme tous les animaux en canard

