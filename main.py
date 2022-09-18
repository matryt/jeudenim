from random import randint as rd
from time import sleep as sp
from random import random as rm

nombre_allumettes = 16
ordi = False

def debut():
	global ordi
	print('Bonjour et bienvenue dans ce jeu de Nim Python ! \n\n')
	o = input("Veux-tu jouer contre un autre joueur ou contre l'ordinateur ? (j/o) \n")
	if o == 'o':
		ordi = True
	difficulte()
	h = input('Voulez-vous avoir les règles du jeu ? (o/n) \n')
	if h == 'o':
		return regles()

def difficulte():
	global nombre_allumettes
	d = {1 : 16, 2 : 20, 3 : 25}
	dif = int(input("Quelle difficulté souhaitez-vous ? (1 = 16 allumettes ; 2 = 20 allumettes ; 3 = 25 allumettes) \n"))
	while not 1 <= dif <= 3:
		print('Impossible ! Cette difficulté est inconnue !')
		dif = int(input("Quelle difficulté souhaitez-vous ? (1 = 16 allumettes ; 2 = 20 allumettes ; 3 = 25 allumettes) \n"))
	nombre_allumettes = d[dif]

def regles():
	print('Le jeu de Nim se joue à 2.')
	print("Au début de la partie,  16 allumettes sont disposées.  Elles sont modélisées comme ceci : ")
	print_allumettes()
	print("Chacun à son tour,  le joueur peut prendre 1, 2 ou 3 allumettes parmi celles restantes. \n")
	print("Celui qui prend la dernière allumette a perdu. ")
	print(ligne())

def joueurs():
	if not ordi:
		return tuple(input(f"Quel est le nom du joueur {i + 1} ? \n") for i in range(2))
	else:
		return input(f"Quel est le nom du joueur ? \n")

def print_allumettes(nombre = 1):
	for _ in range(nombre):
		print('.', end='  ')
	print('\n')
	for _ in range(2):
		for _ in range(nombre):
			print('|', end='  ')
		print('\n')

def ligne():
	return "".join("-" for _ in range(30))

def nombre_ordi():
	if rm() < 0.75:
		if (nombre_allumettes - 1) % 4 == 1 and nombre_allumettes >= 1:
			return 1
		if (nombre_allumettes - 2) % 4 == 1 and nombre_allumettes >= 2:
			return 2
		if (nombre_allumettes - 3) % 4 == 1 and nombre_allumettes - 3 >= 0:
			return 3
		return 1
	else:
		a = rd(1, 3)
		while nombre_allumettes - a < 0:
			a = rd(1, 3)
		return a

def jeu_a_2(joueur1, joueur2):
	while nombre_allumettes != 0:
		tour(joueur1)
		if nombre_allumettes <= 0:
			return gagne(joueur2)
		tour(joueur2)
		if nombre_allumettes <= 0:
			return gagne(joueur1)

def jeu_ordi(joueur):
	while nombre_allumettes != 0:
		tour(joueur)
		if nombre_allumettes <= 0:
			return gagne("L'ordi")
		tour_ordi()
		if nombre_allumettes <= 0:
			return gagne(joueur)

def tour(j):
	global nombre_allumettes
	l = ligne()
	print(f"C'est à {j} de jouer ! Voici l' (les) allumette(s) restante(s) : \n")
	print_allumettes(nombre_allumettes)
	a = int(input("Combien voulez-vous prendre d'allumette(s) ? "))
	while not 1 <= a <= 3:
		print("Impossible ! Vous devez prendre entre 1 et 3 allumette(s) !")
		a = int(input("Combien voulez-vous prendre d'allumette(s) ? "))
	while nombre_allumettes - a < 0:
		print(f"Vous ne pouvez pas prendre {a} allumette(s), car il n'en reste que {nombre_allumettes} !")
		a = int(input("Combien voulez-vous prendre d'allumette(s) ? "))
	nombre_allumettes -= a
	print("Ton tour est terminé !")
	print(l)

def tour_ordi():
	global nombre_allumettes
	l = ligne()
	print("L'ordinateur réfléchit....")
	sp(1)
	n = nombre_ordi()
	nombre_allumettes -= n
	print(f"L'ordinateur enlève {n} allumette(s) !")
	print(l)

def gagne(g):
	if g == "L'ordi":
		print("L'ordinateur a gagné contre toi ! Dommage, ce sera pour la prochaine fois !")
	else:
		print(f"{g} a gagné ! Bravo à toi !")

def main():
	l = ligne()
	debut()
	if ordi:
		j1 = joueurs()
	else:
		j1, j2 = joueurs()
	print(l)
	print('Début du jeu !'.center(30))
	print(l)
	if ordi:
		jeu_ordi(j1)
	else:
		jeu_a_2(j1, j2)

main()