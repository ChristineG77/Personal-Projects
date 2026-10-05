#Write a short dungeon crawler with a boss at the end
import magic
#print(magic.magic_number)
print(magic.magic)

#Establish classes and their stats
barbarian={'ATK':3,'DEF':4,'HP':40,'MP':0}
cleric={'ATK':1,'DEF':2,'HP':20,'MP':10}
fighter={'ATK':2,'DEF':3,'HP':30,'MP':5}
Classes =[]
Classes.append(barbarian)
Classes.append(cleric)
Classes.append(fighter)
#Establish potion, armor, weapon variables these are constants
#weapons: sword, mace, staff
sword = "Sword"
mace ="Mace"
staff = "Staff"
weapons = [sword,mace,staff]
#damage numbers
sworddmg = float(2.4)
macedmg = float(3.4)
staffdmg = float(1)
weaponD = [sworddmg,macedmg,staffdmg]
#item prices
swPrice = int(9)
mPrice = int(10)
sPrice=int(5)
weapon_prices = [swPrice,mPrice,sPrice]
#armor: leather, iron, gold
leather = "Leather Armor"
iron = "Iron Armor"
gold = "Gold Armor"
armor = [leather,iron,gold]
#defense numbers
leatherD = int(3)
ironD = int(5)
goldD = int(1)
armorD = [leatherD,ironD,goldD]
#armor pricing
lPrice = int(3)
iPrice = int(7)
gPrice = int(10)
armor_prices = [lPrice,iPrice,gPrice]
#potions: health, mana, fire, ice
health_v = int(10)
mana_v = int(10)
fire_v = int(5)
ice_v = int(7)
potion_effect = [health_v,mana_v,fire_v,ice_v]
#names
health = "Health Potion"
mana = "Mana Potion"
ice = "Ice Potion"
fire = "Fire Potion"
potions = [health,mana,fire,ice]
#pricing
hPrice = int(3)
mPrice = int(4)
fPrice = int(6)
iPrice = int(8)
potion_prices = [hPrice,mPrice,fPrice,iPrice]
#Establish enemy variables and stats using lists these are constants
#enemies: orc, gnome,elemental,fairy
orc = {'ATK':3, 'DEF':4, 'HP':20,'MP':0}
gnome = {'ATK':2, 'DEF':2, 'HP':10,'MP':3}
elemental = {'ATK':1, 'DEF':8, 'HP':5,'MP':10}
fairy = {'ATK':2, 'DEF':3, 'HP':15,'MP':5}
Enemies = []
Enemies.append(orc)
Enemies.append(gnome)
Enemies.append(elemental)
Enemies.append(fairy)
#start if statement to end later


decision = input("Do you want to enter the Dungeon? Yes or No? ")
if decision == "Yes" or decision == "yes":
    decision = 1
    while decision == 1:
        #Ask the user their na
        #me for the variable player_Name
        player_Name = input("Please enter name here: ")
         #Provide a list of classes, each class has a different set of stats and abilities
         #Ask the user which class they want for the variable player_Class and player_c
        
        player_Class = input("Please pick a class: Barbarian, Cleric, Fighter (Please capatilize the classes name): ")
        player_c = player_Class
        if player_c == "Barbarian" or player_c == "barbarian":
            player_c = 0
            stats = barbarian
        elif player_c == "Cleric" or player_c == "cleric":
            player_c = 1
            stats = cleric
        elif player_c == "Fighter"or player_c == "fighter":
            player_c = 2
            stats = fighter
        else:
            print("I think you spelled the class wrong, please start from the top!")
           

        print(player_Name,"chose the", player_Class, " with these stats: ",(Classes[player_c]))

        # based on class determine coin amount. Use if statements 
        
        if stats == barbarian:
            coin = float(20)
        elif stats == cleric:
            coin = float(35)
        elif stats == fighter:
            coin = float(25)
        else:
            print("You didn't pick a class that was avaliable, please try again.")
        
        player_Purse = coin
        print("You have:",player_Purse,"of gold coins!")
        #Show small shop with weapons and items with pricing
        print("Shop Owner: 'Welcome",player_Name,"! Please come purchase something from my store to aid you on your adventure!'")
        print()
        print("-"*3,"Dungeon Shop, get your gear!","-"*3)
        print(f'{"Items":<30}{"Prices":<30}')
        print(f"{(weapons[0]):<30}{(weapon_prices[0])} gold")
        print(f"{(weapons[1]):<30}{(weapon_prices[1])} gold")
        print(f"{(weapons[2]):<30}{(weapon_prices[2])} gold")
        print(f"{(armor[0]):<30}{(armor_prices[0])} gold")
        print(f"{(armor[1]):<30}{(armor_prices[1])} gold")
        print(f"{(armor[2]):<30}{(armor_prices[2])} gold")
        print(f"{(potions[0]):<30}{(potion_prices[0])} gold")
        print(f"{(potions[1]):<30}{(potion_prices[1])} gold")
        print(f"{(potions[2]):<30}{(potion_prices[2])} gold")
        print(f"{(potions[3]):<30}{(potion_prices[3])} gold")
        print("-"*37)
        
        
        weapon_select = bool
        weapon_select = False
        #give the user an amount of gold between 10-40 pieces and set coin_Purse variable
        while weapon_select == False:    
            print("Shop Owner:'Please tell me the weapon you want to buy': ")
            Item1 = input("")
            if Item1 == "Sword":
                Item1 = 0
                coin = (coin-(weapon_prices[Item1]))
                print("You have",coin,"left in your coinpurse.")
                weapon_name=(weapons[Item1])
                weapon_dmg = (weaponD[Item1])
                weapon_select = True
            elif Item1 == "Mace":
                Item1 = 1
                coin = (coin-(weapon_prices[Item1]))
                print("You have",coin,"left in your coinpurse.")
                weapon_name=(weapons[Item1])
                weapon_dmg = (weaponD[Item1])
                weapon_select = True
            elif Item1 == "Staff":
                Item1 = 2
                coin = (coin-(weapon_prices[Item1]))
                print("You have",coin,"left in your coinpurse.")
                weapon_name=(weapons[Item1])
                weapon_dmg = (weaponD[Item1])
                weapon_select = True
            else:
                print("Shop Owner:'You didn't buy a weapon. Are you sure you would like to continue without one?'")
                answer = input()
                if answer == "Yes":
                   print("Shop Owner:'If you're sure, it'll make the dungeon impossible. Onto armor then!'")
                   weapon_name = ""
                   weapon_select = True
                else:
                    weapon_select = False
        armor_select = bool
        armor_select = False
        while armor_select == False:    
            print("Shop Owner:'Please tell me the armor you want to buy': ")
            Item2 = input("")
            if Item2 == "Leather":
                Item2 = 0
                if coin < (armor_prices[Item2]):
                    print("Shop Owner:'You don't have enough gold for this item!'")
                    armor_select = False
                else:        
                    coin = (coin-(armor_prices[Item2]))
                    print("You have",coin,"left in your coinpurse.")
                    armor_name=(armor[Item2])
                    armor_def = (armorD[Item2])
                    armor_select = True
            elif Item2 == "Iron":
                Item2 = 1
                if coin < (armor_prices[Item2]):
                    print("Shop Owner:'You don't have enough gold for this item!'")
                    armor_select = False
                else:  
                    coin = (coin-(armor_prices[Item2]))
                    print("You have",coin,"left in your coinpurse.")
                    armor_name=(armor[Item2])
                    armor_def = (armorD[Item2])
                    armor_select = True
            elif Item2 == "Gold":
                Item2 = 2
                if coin < (armor_prices[Item2]):
                    print("Shop Owner:'You don't have enough gold for this item!'")
                    armor_select = False
                else:  
                    coin = (coin-(armor_prices[Item2]))
                    print("You have",coin,"left in your coinpurse.")
                    armor_name=(armor[Item2])
                    armor_def = (armorD[Item2])
                    armor_select = True
            else:
                print("Store Owner:'You didn't buy any armor. Are you sure you would like to continue without any?'")
                answer = input()
                if answer == "Yes":
                   print("Store Owner:'If you're sure, it'll make the dungeon impossible. Onto the first Potion!'")
                   armor_name = ""
                   armor_select = True
                else:
                    armor_select = False

        potion1_select = bool
        potion1_select = False
        while potion1_select == False:    
            print("Shop Owner:'Please tell me a potion you want to buy': ")
            Item3 = input("")
            if Item3 == "Health":
                Item3 = 0
                if coin < (potion_prices[Item3]):
                    print("Shop Owner:'You don't have enough gold for this item!'")
                    potion1_select = False
                else:        
                    coin = (coin-(potion_prices[Item3]))
                    print("You have",coin,"left in your coinpurse.")
                    potion_name1=(potions[Item3])
                    potion_slot1 = (potion_effect[Item3])
                    potion1_select = True
            elif Item3 == "Mana":
                Item3 = 1
                if coin < (potion_prices[Item3]):
                    print("Shop Owner:'You don't have enough gold for this item!'")
                    potion_select = False
                else:  
                    coin = (coin-(potion_prices[Item3]))
                    print("You have",coin,"left in your coinpurse.")
                    potion_name1=(potions[Item3])
                    potion_slot1 = (potion_effect[Item3])
                    potion1_select = True
            elif Item3 == "Fire":
                Item3 = 2
                if coin < (potion_prices[Item3]):
                    print("Shop Owner:'You don't have enough gold for this item!'")
                    armor_select = False
                else:  
                    coin = (coin-(potion_prices[Item3]))
                    print("You have",coin,"left in your coinpurse.")
                    potion_name1=(potions[Item3])
                    potion_slot1 = (potion_effect[Item3])
                    potion1_select = True
            elif Item3 == "Ice":
                Item3 = 3
                if coin < (potion_prices[Item3]):
                    print("Shop Owner:'You don't have enough gold for this item!'")
                    potion1_select = False
                else:  
                    coin = (coin-(potion_prices[Item3]))
                    print("You have",coin,"left in your coinpurse.")
                    potion_name1=(potions[Item3])
                    potion_slot1 = (potion_effect[Item3])
                    potion1_select = True
            else:
                print("Store Owner:'You didn't buy a potion. Are you sure you would like to continue without any?'")
                answer = input()
                if answer == "Yes":
                   print("Store Owner:'If you're sure, it'll make the dungeon difficult. Onto the second Potion!'")
                   potion_name1 = ""
                   potion1_select = True
                else:
                    potion1_select = False
            

        potion2_select = bool
        potion2_select = False
        while potion2_select == False:    
            print("Shop Owner:'Please tell me a potion you want to buy': ")
            Item4 = input("")
            if Item4 == "Health":
                Item4 = 0
                if coin < (potion_prices[Item4]):
                    print("Shop Owner:'You don't have enough gold for this item!'")
                    potion2_select = False
                else:        
                    coin = (coin-(potion_prices[Item4]))
                    print("You have",coin,"left in your coinpurse.")
                    potion_name2=(potions[Item4])
                    potion_slot2 = (potion_effect[Item4])
                    potion2_select = True
            elif Item4 == "Mana":
                Item4 = 1
                if coin < (potion_prices[Item4]):
                    print("Shop Owner:'You don't have enough gold for this item!'")
                    potion2_select = False
                else:  
                    coin = (coin-(potion_prices[Item4]))
                    print("You have",coin,"left in your coinpurse.")
                    potion_name2=(potions[Item4])
                    potion_slot2 = (potion_effect[Item4])
                    potion2_select = True
            elif Item4 == "Fire":
                Item4 = 2
                if coin < (potion_prices[Item4]):
                    print("Shop Owner:'You don't have enough gold for this item!'")
                    potion2_select = False
                else:  
                    coin = (coin-(potion_prices[Item4]))
                    print("You have",coin,"left in your coinpurse.")
                    potion_name2=(potions[Item4])
                    potion_slot2 = (potion_effect[Item4])
                    potion2_select = True
            elif Item4 == "Ice":
                Item4 = 3
                if coin < (potion_prices[Item4]):
                    print("Shop Owner:'You don't have enough gold for this item!'")
                    potion2_select = False
                else:  
                    coin = (coin-(potion_prices[Item4]))
                    print("You have",coin,"left in your coinpurse.")
                    potion_name2=(potions[Item4])
                    potion_slot2 = (potion_effect[Item4])
                    potion2_select = True
            else:
                print("Store Owner:'You didn't buy a potion. Are you sure you would like to continue without any?'")
                answer = input()
                if answer == "Yes":
                   print("Store Owner:'If you're sure, it'll make the dungeon difficult!'")
                   potion2_select = True
                   potion_name2 = ""
                else:
                   potion2_select = False
        if potion_name1 == "" and potion_name2 != "":
            print("Shop Owner: You have a",weapon_name,"you have",armor_name,"and you have a",potion_name2)
        elif potion_name2 == "" and potion_name1 != "":
            print("Shop Owner: You have a",weapon_name,"you have,",armor_name, "and you have a", potion_name1)
        elif potion_name1 == "" and potion_name2 == "":
            print("Shop Owner: You have a",weapon_name,"and",armor_name)
        else:
            print("Shop Owner: You have a",weapon_name,"you have",armor_name,"you have a",potion_name1,"and you have a",potion_name2)
 #ask user what and if they want to buy anything, 1 weapon, 1 armor, up to 2 potions. 

 #Input what they chose for variables player_Weapon, player_Armor, potion_slot1, potion_slot2

 #subtract the price of each item from the coin_Purse

 #Ask if user is sure about their chioce, if no, ask if they'd like to try again, if yes, send them back to the top
 #end if statement, and move to next section if they choose to
        decision = input("Would you like to go back and restart? Yes or No? ")
        if decision == "Yes":
            decision = 1
        else:    
            print("Lets head into the dungeon")
else:
    print("Have fun elsewhere!")


player_dmg = weapon_dmg * stats['ATK']
player_def = armor_def * stats['DEF']
player_hp = stats['HP']
player_mp = stats['MP'] 
print("*"*5,"Magicks!","*"*5)
if stats == cleric:
    print("As a Cleric you have access to two magic spells: Heal and Holy.\nHeal will heal you back 5 health and Holy does 6 dmg to enemies.\nHeal uses 3 Mana and Holy uses 5 Mana.")
elif stats == fighter:
    print("As a Fighter you have access to one magic spell: Barrier.\nBarrier will increase you defense by 3 for 1 turn.\nBarrier costs 2 Mana.")
else:
    print("You are a Barbarian and have no need for spells and magic!")
print("*"*20)
#Spells
Heal = 5 * player_hp
Barrier = 3 + player_def
#Holy = 6 - enemy_hp
print("You enter the first Dungeon Room! You see a: ")
battle = True
while battle == True:
    monster = input("Pick a number: 1, 2, 3, or 4")
    if monster != "1" or monster != "2" or monster != "3" or monster != "4":
        print("You didn't pick a number")
        battle = True
    else:
        battle = False
    