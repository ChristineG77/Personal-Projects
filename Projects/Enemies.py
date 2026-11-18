#Establish enemy variables and stats using lists these are constants
import random
#enemies: orc, gnome,elemental,fairy
Enemy = ["Orc","Gnome","Fairy","Elemental","King Slime"]
orc = {'ATK':6, 'DEF':6, 'HP':20,'MP':0}
gnome = {'ATK':4, 'DEF':2, 'HP':10,'MP':3}
elemental = {'ATK':1, 'DEF':7, 'HP':5,'MP':10}
fairy = {'ATK':2, 'DEF':3, 'HP':15,'MP':5}
king_slime = {'ATK':8, 'DEF':6, 'HP':45,'MP':0}

Enemies = []
Enemies.append(orc)
Enemies.append(gnome)
Enemies.append(fairy)
Enemies.append(elemental)
Enemies.append(king_slime)
enemy = Enemies[monster]
enemy_name = Enemy[monster]
enemy_hp = enemy['HP']
enemy_atk = enemy['ATK']
enemy_def = enemy['DEF']
enemy_mp = enemy['MP']
enemy_maxhp = enemy_hp