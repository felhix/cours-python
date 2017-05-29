#! python3
# 01-strings.py - quelques fonctions pour jouer avec les strings

# On peut commencer et finir un string par des guillemets ou des apostrophes
string_1 = "C'est un string"
string_2 = 'Il dit : "string là aussi"'

# les caractères d'échappement (escape characters) permettent de rentrer des caractères impossobles à rentrer autrement
string_1 = 'Bonjour c\'est Félix' #=> Bonjour c'est félix
string_2 = "Et là il dit : \"C'est aussi un string !\"" #=> Et là il dit : "C'est aussi un string !"
string_3 = "On peut \t aussi \t mettre des tabulations" #=> On peut 	 aussi 	 mettre des tabulations
string_4 = "Ou \n des \n retours \n à \n la \n ligne !"
string_5 = "Ou des antislash comme ça : \\" #=> Ou des antislash comme ça : \

# on peut générer des strings de plusieurs lignes en commençant et finissant par des triple apostrophes

string_long = '''Bonjour,
Ceci est un string long. C'est plutôt cool !

Je peux même faire des retours à la ligne faciles.


J'adore !!!'''

# comme pour les listes, on peut faire in ou not in sur des strings
hello = "Bonjour monde !"
print("Bonjour" in hello) #=> True
print("Jean" not in hello) #=> True

# upper() majuscule un string
string_1 = "Bonjour monde !"
string_1 = string_1.upper() #=> BONJOUR MONDE !

# lower() minuscule un string
string_1 = "BonJOUR mONde !"
string_1 = string_1.lower() #=> "bonjour monde !"

# isupper() checke si un string est majusculé
string_1 = "bonjour monde !"
print(string_1.isupper()) #=> False


# islower() checke si un string est minusculé
string_1 = "bonjour monde !"
print(string_1.islower()) #=> True

# envie de transformer une liste en string ? Il suffit d'utiliser la fonction join() ! Le string sur lequel on éxécute la fonction join() sera ce que l'on mettra entre les éléments de la liste.
liste = ["Mon", "nom", "est", "Félix"]
print(",".join(liste)) #=> "Mon,nom,est,Félix"
print("".join(liste)) #=> "MonnomestFélix"
print(" ".join(liste)) #=> "Mon nom est Félix"
print("LOL".join(liste)) #=> MonLOLnomLOLestLOLFélix

# envie de passer de string à liste ? La fonction split() est ton ami !
string = "Mon nom est Félix"
print(string.split()) #=> ["Mon", "nom", "est", "Félix"]
print(string.split("o")) #=> ["M", "n n", "m est Félix"]



