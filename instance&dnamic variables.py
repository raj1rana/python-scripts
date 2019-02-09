class Enemy:
    #setting the init with variables
    def __init__(self, atklow, atkhigh):
        self.atklow = atklow
        self.atkhigh = atkhigh

    def getatk(self):
        print(self.atklow)

#calling the class with variables given
enemy1 = Enemy(40,49)
#calling the function
enemy1.getatk()
#calling the class with variables given
enemy2 = Enemy(60 ,51)
#calling the function
enemy2.getatk()



#ANOTHER EXAMPLE OF CLASSES WITH INSTANCE VARIABLES ARE

class Enemy:
    hp = 200
    #setting the init with variables
    def __init__(self, atklow, atkhigh):
        self.atklow = atklow
        self.atkhigh = atkhigh

    def getatk(self):

        print("attack is :",self.atklow)

    def totalhp(self):
        print("total health is ",self.hp)

#calling the class with variables given
enemy1 = Enemy(40,49)
#calling the function
enemy1.getatk()
#calling the class with variables given
enemy1.totalhp()
enemy2 = Enemy(60 ,51)
#calling the function
enemy2.getatk()
enemy2.totalhp()


enemy3 = Enemy(10,11)
enemy3.getatk()