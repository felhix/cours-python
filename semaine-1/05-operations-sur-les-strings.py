#! python3
# 05-operations-sur-les-strings.py - montre quelques opérations que l'on peut effectuer sur les strings

#on peut concaténer des strings
print("Bonjour" + "monde !") #=> "Bonjourmonde !"
print("Bonjour" + " " + "monde !") #=> "Bonjour monde !"
print("Bonjour " + "monde !") #=> "Bonjour monde !"

#on peut multiplier un string
print("Ce plat était " + 'super-' * 3 + "bon") #=> "Ce plat était super-super-super-bon"

#voici quelques exemple de bugs ; ce sont des opérations que l'on ne peut pas faire avec un string
#	print("Jean" + 2 ) #=> error, l'ordinateur considère "Jean" comme un string, et considère 2 comme un integer. On ne peut pas additionner un string à un integer
#	print("Jean" * "Raoul" ) #=> error, il n'est pas possible de multiplier des strings entre eux
#	print("Jean" * 12.3943 ) # => error, il n'est pas possible de multiplier un string à un float
# 	print("Jean" * 2.0) # => error, il n'est pas possible de multiplier un string à un float