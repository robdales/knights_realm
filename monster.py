#Monster! :)

class Monster(object):
    
    def __init__(self, name, weapon, hp=10):
        self.name = name
        self.weapon = weapon
        self.hp = hp
    def attack(self):
        print "{monster} attacks with a {weapon}!".format(monster=self.name, weapon=self.weapon)
    
    def __str__(self):
        template = "{monster}: {hp} hp left.  Current weapon: {weapon}"
        #return life bar too
        return template.format(monster=self.name, hp=self.hp, weapon=self.weapon)
    def ouch(self):
        if self.hp > 1:
            print "damage to {name}!".format(name=self.name)
            self.hp= self.hp-5
            print self.hp
            if self.hp < 1:
                print "{name} is dead!".format(name=self.name)
                exit(0)
                #might be better to return value so exit not needed

class MagicMonster(Monster):
    def __init__(self, name, weapon, spell, hp=10):

        Monster.__init__(self, name=name, weapon=weapon,hp=hp)
        self.spell=spell


    def cast(self):
        print "{monster} casts {spell}.  Damage done!".format(
            monster=self.name,
            spell=self.spell)

class Hero(Monster):
    def __init__(self, name, weapon, items, hp=10):
        
        Monster.__init__(self, name=name, weapon=weapon,hp=hp)
        self.items=items

    def items(self):
        '''collect and use items'''
        print 'rare earthworms'
        print collection
       # item select
        
    def help(self):
        '''prints out key buttons''' 
        print '''
        a)call your mama!
        s)send Christmas cards
        l)use life line
        p)is that your final answer?
        '''
    
    def potion(self):
        print "you feel strong like bull. Hp level up!"
        self.hp = self.hp+10
        print "you now have %s HP!" % self.hp

