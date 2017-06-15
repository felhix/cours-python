#! python3
# 03-selenium.py - un programme qui rentre dans vente-privee, avec des fonctions pour un code plus propre

from selenium import webdriver #le driver qui te permet d'aller sur un explorateur internet
from selenium.webdriver.common.keys import Keys #ce qui te permet de rentrer des touches du clavier
import getpass #le module de mot de passe

def get_credentials():
	email = input("Rentre ici ton adresse mail pour vente-privee stp : ")
	password = getpass.getpass('Rentre le mot de passe pour l\'email stp : ')
	print("Merci ! J'essaie de rentrer dans le site 😉")
	return email, password

def open_vente_privee():
	driver = webdriver.Firefox() #ouvre Firefox
	driver.get("https://secure.fr.vente-privee.com/authentication/portal/FR") #ouvre vente-privee
	return driver

def fill_in_email(email, driver):
	email_to_fill_in = driver.find_element_by_name("Email") #recherche la case email
	email_to_fill_in.clear() #efface les caractères déjà présents
	email_to_fill_in.send_keys(email) #rentre l'email

def fill_in_password_and_press_return(password, driver):
	password_to_fill_in = driver.find_element_by_name("Password")
	password_to_fill_in.clear()
	password_to_fill_in.send_keys(password)
	password_to_fill_in.send_keys(Keys.RETURN) #appuie sur la touche "entrée" pour valider

def perform():
	email, password = get_credentials()
	driver = open_vente_privee()
	fill_in_email(email, driver)
	fill_in_password_and_press_return(password, driver)

perform()