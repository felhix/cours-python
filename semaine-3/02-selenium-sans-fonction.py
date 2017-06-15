#! python3
# 02-selenium.py - un programme qui rentre dans vente-privee, sans fonctions

from selenium import webdriver #le driver qui te permet d'aller sur un explorateur internet
from selenium.webdriver.common.keys import Keys #ce qui te permet de rentrer des touches du clavier
import getpass #le module de mot de passe

email = input("Rentre ici ton adresse mail pour vente-privee stp : ")
password = getpass.getpass('Rentre le mot de passe pour l\'email stp : ')
print("Merci ! J'essaie de rentrer dans le site 😉")
driver = webdriver.Firefox() #ouvre Firefox
driver.get("https://secure.fr.vente-privee.com/authentication/portal/FR") #ouvre vente-privee
email_to_fill_in = driver.find_element_by_name("Email") #recherche la case email
email_to_fill_in.clear() #efface les caractères déjà présents
email_to_fill_in.send_keys(email) #rentre l'email
password_to_fill_in = driver.find_element_by_name("Password")
password_to_fill_in.clear()
password_to_fill_in.send_keys(password)
password_to_fill_in.send_keys(Keys.RETURN) #appuie sur la touche "entrée" pour valider