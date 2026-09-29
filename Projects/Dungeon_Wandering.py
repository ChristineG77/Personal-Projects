#Write a short dungeon crawler with a boss at the end

#Establish classes and their stats

barbarian={'ATK':3,'DEF':4,'HP':40,'MG':0}
cleric={'ATK':1,'DEF':2,'HP':20,'MG':10}
fighter={'ATK':2,'DEF':3,'HP':30,'MG':5}
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
weapon_dmg = [sworddmg,macedmg,staffdmg]
#item prices
swPrice = int(9)
mPrice = int(10)
sPrice=int(5)
weapon_prices = [swPrice,mPrice,sPrice]
#armor: leather, iron, gold
leather = "Leather"
iron = "Iron"
gold = "Gold"
armor = [leather,iron,gold]
#defense numbers
leatherD = int(3)
ironD = int(5)
goldD = int(1)
armorDEF = [leatherD,ironD,goldD]
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
#start if statement to end later


decison = input("Do you want to enter the Dungeon? Yes or No? ")
if decison == "Yes":
    decison = 1
    while decison == 1:
        #Ask the user their na
        #me for the variable player_Name
        player_Name = input("Please enter name here: ")
         #Provide a list of classes, each class has a different set of stats and abilities
         #Ask the user which class they want for the variable player_Class and player_c
        
        player_Class = input("Please pick a class: Barbarian, Cleric, Fighter (Please capatilize the classes name): ")
        player_c = player_Class
        if player_c == "Barbarian":
            player_c = 0
            stats = barbarian
        elif player_c == "Cleric":
            player_c = 1
            stats = cleric
        elif player_c == "Fighter":
            player_c = 2
            stats = fighter
        else:
            print("I think you spelled the class wrong, or didn't capitalize, please start from the top!")
           

        print(player_Name,"chose the", player_Class, " with these stats: ",(Classes[player_c]))

        # based on class determine coin amount. Use if statements 
        
        if stats == barbarian:
            coin = float(15)
        elif stats == cleric:
            coin = float(35)
        elif stats == fighter:
            coin = float(25)
        else:
            print("You didn't pick a class that was avaliable, please try again.")
                
        #give the user an amount of gold between 10-40 pieces and set coin_Purse variable
        player_Purse = coin

        print("You have:",player_Purse,"of gold coins!")
        #Show small shop with weapons and items with pricing
    
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
        print("Come purchase something from the store.")
        def weapon():
            print("Please enter a weapon you want to buy: ")
            Item1 = input("")
            if Item1 == "Sword":
                Item1 = 0
                coin = ((weapon_prices[Item1])-coin)
                print("You have",coin,"left in your coinpurse.")
            elif Item1 == "Mace":
                Item1 = 1
                coin = ((weapon_prices[Item1])-coin)
                print("You have",coin,"left in your coinpurse.")
            elif Item1 == "Staff":
                Item1 = 2
                coin = ((weapon_prices[Item1])-coin)
                print("You have",coin,"left in your coinpurse.")
            else:
                print("No weapon bought")
                print("Would you like to go back and buy something from the store?")
                answer = input()
                if answer == "Yes":
                   weapon()
                else:
                    print("If you're sure, it'll make the dungeon impossible. Onto armor then!")
        weapon()

 #ask user what and if they want to buy anything, 1 weapon, 1 armor, up to 2 potions. 

 #Input what they chose for variables player_Weapon, player_Armor, potion_slot1, potion_slot2

 #subtract the price of each item from the coin_Purse

 #Ask if user is sure about their chioce, if no, ask if they'd like to try again, if yes, send them back to the top
 #end if statement, and move to next section if they choose to
        decison = input("Would you like to go back and restart? Yes or No? ")
        if decison == "Yes":
            decison = 1
        else:    
            print("Lets head into the dungeon")
else:
    print("Have fun elsewhere!")