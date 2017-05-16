#! python3
# 03-variables.py - montre comment les variables marchent

# Une variable peut prendre n'importe quel type de donnée. Ici, nous allons déclarer 3 variables. Déclarer une variable c'est comme dire à l'ordinateur que la variable [variable] a une valeur de [valeur] à l'intérieur. Ceci sera stocké dans la mémoire vive de l'ordinateur.
variable_1 = 1 # un integer
variable_2 = "Ceci est un string qui est tout à fait valide pour une variable" # un string
variable_3 = 2.0 # un float

#Nous pouvons effectuer tout type d'opérations sur des variables. Ici par exemple nous allons demander au programme d'afficher dans la console la valeur de variable_1
print(variable_1) #=> 1

#L'un des aspects très cools des variables est qu'on peut les modifier à notre guise
variable_1 = "Cette variable était un integer, maintenant c'est un string"
variable_2 = "On peut aussi juste modifier la valeur, et garder le même type de donnée"
variable_3 = variable_3 + 4.0 # ici nous disons à variable_3 de prendre la valeur de elle-même, plus 4.0. Ainsi variable_3 sera égale à 6.0

#Ainsi, à partir de la ligne 13 du programme, variable_1 aura sa valeur changée. Sur si l'on affiche variable_1, cela affichera sa nouvelle valeur, et non pas celle déclarée en ligne 5
print(variable_1) #=> "Cette variable était un integer, maintenant c'est un string"

#On peut faire tout type d'opérations sur une variable. Là je vais déclarer deux variables, puis les multiplier entre elles pour m'apercevoir qu'on envoie trop d'emails
number_of_emails_sent_per_hour = 12
number_of_hours_per_day = 24
print(number_of_hours_per_day * number_of_emails_sent_per_hour) #=> 288

#Ou alors j'ai envie d'afficher mon nom en entier
first_name = "Félix"
last_name = "Gaudé"
print("Bonjour " + first_name + " " + last_name) #=> Bonjour Félix Gaudé

#Attention à ne pas faire des opérations foireuses sur les variables. Il n'est pas possible d'additionner un string avec un integer donc la ligne suivante va renvoyer un bug
age = 26
#print("Bonjour " + first_name + " tu as " + age + " ans !")