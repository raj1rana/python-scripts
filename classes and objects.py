#creating a class called Enemy
class Enemy:
#assinging the variables to this class
    atklow = 60
    atkhigh = 80
#creating a function that will print the attack NOTE self is for the class created to use the
#function as it is created within the class
    def getatack(self):
        print(self.atklow)
#calling the class
enemy1 = Enemy()
#calling the function
enemy1.getatack()
#calling the class
enemy2 = Enemy()
#calling the function
enemy2.getatack()