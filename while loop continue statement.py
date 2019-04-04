#importong random module to find the ramdom numbetween variables
import random
#assinging variables
playerhp = 260
ememyatklow = 60
ememyatkhigh = 80
#adding while loop to do the calculation
while playerhp > 30:
#random.randrange to find the ramdom numbers between ememyatkhigh and ememyatklow
    dmg = random.randrange(ememyatklow,ememyatkhigh)
    playerhp = playerhp - dmg

    #adding a if statement to check the player current health
    if playerhp <= 30:
        playerhp = 30
    print("enemy strikes for ",dmg,"points of damage. current hp is ", playerhp)
    #using the continue attribute to continue unless the playerhp is 30 
    if playerhp > 30:
        continue

        print("you have low health.     you have been teleported to the nearest inn . ")

