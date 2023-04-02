
# Full documentation on all structures
# https://docs.python.org/
#	or install sth via pip
#	https://pypi.org

from typing import Dict
import random
import datetime

# General settings
droprate_doubled = 0;
number_of_pulls = 10**3;

''' use dict as a replacement for maps in C++
	https://docs.python.org/3/c-api/dict.html
	https://www.w3schools.com/python/python_ref_dictionary.asp
dict_exl = {
	2 : 0.885,
	3 : 0.085,
	4 : 0.03
	}

print("Know your type: dict_exl = ", type(star_chances))
'''
# class as a base for pulled characters
# character(name: str, star: int)
class character:
	name: str	# Name
	star: int	# star_rating
	anzahl: int = 0	# Anzahl gezogener Charaktere
	# Define variables for draw-chances as a division of unity
	#	the idea is to have " rand in [a,b)", hence the probability is "wkeit = b-a"
	a: float	# in (0,1) lower bound
	b: float	# in (0,1) upper bound
	wkeit: float = 0
	# Jede zehnte Ziehung hat "Guaranteed Drop Rates"
	a_10: float	# in (0,1) lower bound
	b_10: float	# in (0,1) upper bound
	wkeit_10: float
	# "self" is the same as "this" in e.g. Java
	#	BUT IN PYTHON IT LITERALLY HAS TO BE TYPED EVERYWHERE!!!!!!!!!!!!!!!!!!!!!!!!
	def __init__(self, name: str, star: int):
		self.name = name
		self.star = star
	# Normales ziehen
	def set_draw_chances(self, a: float,b: float):
		self.a = a
		self.b = b
		self.wkeit = b-a
	# Jede zehnte Ziehung hat "Guaranteed Drop Rates"
	def set_draw_10_chances(self, a: float, b:float):
		self.a_10 = a
		self.b_10 = b
		self.wkeit_10 = b-a
	# Jede zehnte Ziehung hat andere Dropchancen
	def get_draw_chances(self, ziehung_anz: int):
		if ziehung_anz % 10 == 0:
			return [self.a_10, self.b_10]
		else:
			return [self.a, self.b]
	def add(self):
		self.anzahl += 1
	def get_anzahl(self):
		return self.anzahl
	def print_stats(self):
		if self.wkeit > 0:
			print("Name = ", self.name, "\n\tSterne = ", self.star, "\n\tAnzahl = ", self.anzahl, "\n\tPull-Chance = ", self.wkeit)
		else:
			print("Name = ", self.name, "\n\tSterne = ", self.star, "\n\tAnzahl = ", self.anzahl, "\n\tPull-Chance = na")


# class for pulling characters
#	it depends on the number of pulls and type event
#	chance_event_character: float	# Dropchance per event character. Assumes the dropchance of all event characters is equal
# event(number_event_characters: int, chance_event_characters: float, droprate_doubled: bool)
class event:
	#--- class variables -------------------------------------------------------
	pull_anz = 0
	crystals_spend = 0
	number_event_characters: int	# Event characters are not named but enumerated
	chance_event_character: float	# Dropchance per event character. Assumes the dropchance of all event characters is equal
	droprate_doubled = 0
	Seed = datetime.datetime.now()	# Fix "random" Seed
	# Dictionary: Links key und rechts Element. Der key muss nicht den gleichen Namen wie den der Klasse tragen
	dict_chars = {
		"zweiSterne" : character("zweiSterne", 2),
		"dreiSterne" : character("dreiSterne", 3),
		"nichtEvent_vierSterne" : character("nichtEvent_vierSterne", 4)
		}

	#--- Initializing class -------------------------------------------------------
	def __init__(self, number_event_characters: int, chance_event_character:float, droprate_doubled: bool):
		self.number_event_characters = number_event_characters
		self.chance_event_character = chance_event_character
		self.droprate_doubled = droprate_doubled
		random.seed(str (self.Seed))	# ohne Argumente funktioniert die Systemzeit als Seed
		# Dropliste um Anzahl der Eventcharactere erweitern
		for i in range(number_event_characters):
			self.dict_chars.update({"Event_vierSterne_"+str(i) : character("Event_vierSterne_"+str(i), 4)})

		# Setze Charakterwahrscheinlichkeiten zum Schluss der Initialisierunt als Teilung der 1
		self._set_chances()

	#--- Private functions for class event ---------------------------------------
	def _set_chances(self):
		a:float = 0; a_10: float = 0
		b:float = 0; b_10:float = 0
		c:float = 0; c_10: float = 0	# c = b-a
		# Dropchancen in Events mit 3% für 4-Sterne
		if self.droprate_doubled == 0:
			c = 0.885; b = c
			self.dict_chars.get("zweiSterne").set_draw_chances(a, b)
			self.dict_chars.get("zweiSterne").set_draw_10_chances(a_10, b_10)
			c = 0.085; c_10 = 0.97
			a = b; b += c; a_10 = b_10; b_10 += c_10
			self.dict_chars.get("dreiSterne").set_draw_chances(a, b)
			self.dict_chars.get("dreiSterne").set_draw_10_chances(a_10, b_10)
			# nicht Event 4-Sterne ist 4-Sterne-Chance Minus Eventcharacterchancen
			c = 0.03 - self.number_event_characters*self.chance_event_character
			c_10 = c
			a = b; b += c; a_10 = b_10; b_10 += c_10
			self.dict_chars.get("nichtEvent_vierSterne").set_draw_chances(0, b)
			self.dict_chars.get("nichtEvent_vierSterne").set_draw_10_chances(a_10, b_10)
			# Eventcharaterdropchance setzen
			c = self.chance_event_character
			for i in range(self.number_event_characters):
				a = b; b += c
				c_10 = c
				a_10 = b_10; b_10 += c_10
				self.dict_chars.get("Event_vierSterne_"+str(i)).set_draw_chances(a,b)
				self.dict_chars.get("Event_vierSterne_"+str(i)).set_draw_10_chances(a_10, b_10)

		# Dropchancen in Events mit 6% für 4-Sterne
		if self.droprate_doubled == 1:
			c = 0.855; b = c
			self.dict_chars.get("zweiSterne").set_draw_chances(a, b)
			self.dict_chars.get("zweiSterne").set_draw_10_chances(a_10, b_10)
			c = 0.085; c_10 = 0.94
			a = b; b += c; a_10 = b_10; b_10 += c_10
			self.dict_chars.get("dreiSterne").set_draw_chances(a, b)
			self.dict_chars.get("dreiSterne").set_draw_10_chances(a_10, b_10)
			# nicht Event 4-Sterne ist 4-Sterne-Chance Minus Eventcharacterchancen
			c = 0.06 - self.number_event_characters*self.chance_event_character
			c_10 = c
			a = b; b += c; a_10 = b_10; b_10 += c_10
			self.dict_chars.get("nichtEvent_vierSterne").set_draw_chances(a, b)
			self.dict_chars.get("nichtEvent_vierSterne").set_draw_10_chances(a_10, b_10)
			# Eventcharaterdropchance setzen
			c = self.chance_event_character
			for i in range(self.number_event_characters):
				a = b; b += c
				c_10 = c
				a_10 = b_10; b_10 += c_10
				self.dict_chars.get("Event_vierSterne_"+str(i)).set_draw_chances(a,b)
				self.dict_chars.get("Event_vierSterne_"+str(i)).set_draw_10_chances(a_10, b_10)

	#--- Public functions for class event ---------------------------------------
	# Ziehe einen neuen Character
	#	vielleicht auch draw nennen...
	def pull(self):
		self.pull_anz += 1	# D.h. man fängt bei 1 an zu zählen!
		self.crystals_spend += 300
		wkeit = random.random()	# result in [0,1)
		for character in self.dict_chars.values():
			[a, b] = character.get_draw_chances(self.pull_anz)
			if a<=wkeit<b:
				character.add()
				break

	# Seed selber wählen falls gewünscht
	def set_seed(self, zufallseed: int):
		random.seed(zufallseed)

	def print_pulls(self):
		total_anz: int = 0
		print("Anzahl Ziehungen = ", self.pull_anz, "\nKristalle ausgegeben = ", self.crystals_spend)
		for character in self.dict_chars.values():
			character.print_stats()
			total_anz += character.get_anzahl()
			print("\tAnteil an Ziehungen = ", character.get_anzahl() / self.pull_anz)
		print("Gesamtanzahl registrierter Ziehungen = ", total_anz)

	def print_pull_intervals(self):
		print("Normale Ziehung:")
		for character in self.dict_chars.values():
			print("[", character.a, ", ", character.b, ") fuer ", character.name)
		print("Jede zehnte Ziehung:")
		for character in self.dict_chars.values():
			print("[", character.a_10, ", ", character.b_10, ") fuer ", character.name)
# End of class event



'''
Shiraishi_An = character("Shiraishi_An", 4)
Shiraishi_An.add()
Shiraishi_An.add()
Shiraishi_An.print_stats()
'''

# event(number_event_characters: int, chance_event_characters: float, droprate_doubled: bool)
aktuelles_event = event(6, 0.004, True)

for i in range(14*10):
	aktuelles_event.pull()
aktuelles_event.print_pulls()

# aktuelles_event.print_pull_intervals()