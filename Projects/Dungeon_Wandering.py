#Write a short dungeon crawler with a boss at the end

#Establish potion, armor, weapon variables these are constants
#weapons: sword, mace, staff
weapon = {'sword':2.4, 'mace':3.4, 'staff': 1}
#armor: leather, iron, gold
armor = {'leather':3,'iron':5,'gold':2}
#potions: health, mana, fire, ice
health = int(10)
mana = int(10)
fire = int(5)
ice = int(7)
restore = [health,mana]
damage = [fire,ice]
#Establish enemy variables and stats using lists these are constants
#enemies: orc, gnome,elemental,fairy
orc = {'ATK':3, 'DEF':4, 'HP':20,'MP':0}
gnome = {'ATK':2, 'DEF':2, 'HP':10,'MP':3}
elemental = {'ATK':1, 'DEF':8, 'HP':5,'MP':10}
fairy = {'ATK':2, 'DEF':3, 'HP':15,'MP':5}
#start if statement to end later


decison = input("Do you want to enter the Dungeon? Yes or No? ")
if decison == "Yes":
    decison = 1
    while decison ==1:
        #Ask the user their na
        #me for the variable player_Name
        player_Name = input("Please enter name here: ")
#Provide a list of classes, each class has a different set of stats and abilities
        decison = input("Would you like to go back and restart? Yes or No? ")
        if decison == "Yes":
            decison = 1
        else:
            decison = 0
#Ask the user which class they want for the variable player_Class, then set the player_Health, player_Mana, player_ATK, player_MAG
# based on the number for the stat from the class list. Use if statements 

#give the user a random amount of gold between 10-40 pieces and set coin_Purse variable 

#Show small shop with weapons and items with pricing

#ask user what and if they want to buy anything, 1 weapon, 1 armor, up to 2 potions. 

#Input what they chose for variables player_Weapon, player_Armor, potion_slot1, potion_slot2

#subtract the price of each item from the coin_Purse

#Ask if user is sure about their chioce, if no, ask if they'd like to try again, if yes, send them back to the top
#end if statement, and move to next section if they choose to
else:
    print("Lets head into the dungeon!")