#! python3
# 06-qq-fonctions - voici quelques fonctions de base : len(), str(), int(), input(), float()

#	str() - transforme en string l'argument passé à l'intérieur des parenthèses
nb_inbox = 2
#	print("Tu as " + nb_inbox + " messages en attente") #=> error
print("Tu as " + str(nb_inbox) + " messages en attente") #=> "Tu as 2 messages en attente"
print(str(nb_inbox)) #=> "2"

#	int() - transforme en integer l'argument passé à l'intérieur des parenthèses
input_user = "2"
#	print(2 + input_user) => error
print(2 + int(input_user)) #=> 4
print(int(input_user)) #=> 2

#	float() - transforme en float l'argument passé à l'intérieur des parenthèses
input_user = "2"
print(float(input_user)) #=> 2.0

#	len() - calcule la taille de l'argument passé en paramètre
five_letter_word = "Hello"
print(len(five_letter_word)) # => 5

#	input() - demandera à l'utilisateur de rentrer une chaine de caractères et d'appuyer sur entrée. La fonction input() enregistrera la saisie toujours en string
print("Bonjour, comment t'appelles-tu ?")
name_user = input() #=> Je saisis "Félix"
print("Bonjour " + name_user) #=> "Bonjour Félix"
