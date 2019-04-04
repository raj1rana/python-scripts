class Enemy:
    def __init__(self, hp, mp):  # def init inside the class
        self.max_hp = hp  # set the variables
        self.hp = hp
        self.max_mp = mp
        self.mp = mp

    def gethp(self):  # another function that will return the hp
        return self.hp