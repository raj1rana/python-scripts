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
    #if the player health goes below 30 then adding a break to stop the loop
    if playerhp == 30:
        print("you have low health.     you have been teleported to the nearest inn . ")
        break
