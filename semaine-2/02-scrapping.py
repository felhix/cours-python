#! python3
# 01-scrapping.py - petit programme qui scrappe les résultats Google de "bonjour monde" et affiche les intitulés et liens de chacun

#importe les modules requests et beautifulsoup
import requests, bs4

#enregistre l'url de la recherche Google de "bonjour monde"
url = 'https://www.google.fr/search?q=bonjour+monde'

#fais uns requête pour obtenir la page
res = requests.get(url)

#enregistre la page dans un objet BeautifulSoup, avec un bon encodage, et le truc parsé
soup = bs4.BeautifulSoup(res.text.encode('utf-8'), 'html.parser')

#obtiens une array des liens (a) insérés dans des h3 ayant une classe de r
links = soup.select('h3.r a')

#print le nombre de liens dans la liste
print("J'ai réussi à trouver " + str(len(links)) + " liens !")

#passe sur chacun des 10 liens de la liste
for link in links:
	print("===============") #permet de séparer les éléments de la boucle pour mieux s'y repérer
	print(link.text) #prends uniquement le texte du lien
	print(link['href'].replace('/url?q=',''))	#récupère l'élément href du lien, soit l'url. Aussi, Google avait ajouté "/url?q=" en début de lien pour faire des liens customs. J'ai supprimé avec la fonction replace()
