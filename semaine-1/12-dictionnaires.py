#! python3
# 12-dictionnaires.py - les dictionnaires et quelques exemples de fonction que l'on peut faire avec

#un dictionnaire est un type de données, qui a un couple de clé - valeur. Chaque clé doit être différente des autres, et la valeur peut prendre le data type que l'on veut
dico_1 = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
dico_2 = {33: "Gironde", 75: "Paris", 1: "Ain" }
dico_3 = {"is_admin": True, 'is_owner': False, 'is_writer': True}
user_1 = {
    "id": 1
    "first_name": "Félix",
    "postal_code": 75002,
    "is_admin": True,
    "post_created": [12, 345, 932]
}

#si l'ordre dans les listes compte, l'ordre dans les dictionnaires ne compte pas
liste_1 = ["chat", "chien", "oiseau"]
liste_2 = ["chien", "chat", "oiseau"]
print(liste_1 == liste_2) #=> False
dico_1 = { "first_name": "Félix", "last_name": "Gaudé", "age": 26}
dico_2 = {"last_name": "Gaudé",  "first_name": "Félix", "age": 26}
print(dico_1 == dico_2) #=> True


#il est possible de chercher une valeur à partir de sa clé
dico_1 = { "first_name": "Félix", "last_name": "Gaudé", "age": 26}
print(dico_1['first_name']) #=> "Félix"


#keys() accède aux clés d'un dictionnaire
dico_1 = {"couleur": "rouge", "age": 42}
for clef in dico_1.keys():
	print(clef) #=> "couleur" "age"

#values() accède aux valeurs d'un dictionnaire
dico_1 = {"couleur": "rouge", "age": 42}
for valeur in dico_1.values():
	print(valeur) #=> "rouge" 42

#items() accède aux éléments d'un dictionnaire
dico_1 = {"couleur": "rouge", "age": 42}
for element in dico_1.items():
	print(element) #=> "couleur": "rouge" "age": 42

#comme pour les listes, on peut checker si une valeur est dans un dictionnaire avec in, not in
dico_1 = {"couleur": "rouge", "age": 42}
print("couleur" in dico_1.keys()) #=> True
print("rouge" in dico_1.values()) #=> True

#setdefault() permet de créer un couple clé - valeur dans un dictionnaire, mais uniquement si cette clé n'existe pas
dico_1 = {"couleur": "rouge", "age": 42}
dico_1.setdefault("nom", "Félix") #créé le couple clé - valeur
dico_1.setdefault("couleur", "jaune") #la clé "couleur" existe déjà : ne fait rien
print(dico_1) #=> {"couleur": "rouge", "age": 42, "nom", "Félix"}

