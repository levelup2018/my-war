class Warrior:
    attack = 15
    health = 20
    
    def real_attack(self, opp):
        return opp.attack
    
    def kick(self, war):
        war.health -= self.real_attack(war)
        
    def is_alive(self):
        return not self.health <= 0
    
    def show_status(self):
        print('H:{}'.format(self.health))


class SuperWarrior(Warrior):
    attack = 100
    health = 100

class Mechnik(Warrior):
    attack = 20

class Konnica(Warrior):
    defence = 1
    
    def real_attack(self, war):
        real_attack = war.attack - self.defence
        if real_attack > 0:
             return real_attack
            
        return 0

class Heler(Warrior):
    attack = 1
    health = 100

class Boss(Konnica):
    attack = 100

class Army:
    def __init__(self, cls, amount):
        self.units = []
        for i in range(amount):
            self.units.append(cls())


class Battle:
    def __init__(self, army1, army2):
        self.army1 = army1
        self.army2 = army2
    
    def ww_fight(self, war1, war2):
        kicker = war1
        reciver = war2
        while war1.is_alive() and war2.is_alive():
            kicker.kick(reciver)
            kicker, reciver = reciver, kicker
            war1.show_status()
            war2.show_status()
            print('ROUND')
    
        return war1.is_alive()
    
    def fight(self):
        army1 = self.army1
        army2 = self.army2
        while army1.has_units() and  army2.has_units():
            kicker = army1.get_first()
            reciver = army2.get_first()
            
            result = self.ww_fight(kicker, reciver)
            
            if result:
                army2.remove_unit()
            else:
                army1.remove_unit()

def fight(war1, war2):
    kicker = war1
    reciver = war2
    while war1.is_alive() and war2.is_alive():
        kicker.kick(reciver)
        kicker, reciver = reciver, kicker
        war1.show_status()
        war2.show_status()
        print('ROUND')
    
    return war1.is_alive()