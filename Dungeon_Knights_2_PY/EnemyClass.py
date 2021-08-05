from globalVars import *

class Enemy():
    def __init__(self,InHp,InDmg,InArmorPen,InArmor):
        self.Hp = InHp
        self.Dmg = InDmg
        self.ArmorPen = InArmorPen
        self.Armor = InArmor

class Zombie(Enemy):
    def __init__(self):
        self.Weakness = ["Kopf","Head","Brain"]
        self.Strength = ["Beißen","Kratzen"]
        self.AttackType = "Nahkampf"

class Werwolf(Enemy):
    def __init__(self):
        self.Weakness = ["Kopf","Head","Brain"]
        self.Strength = ["Beißen","Kratzen"]
        self.AttackType = "Nahkampf"

class Lakai(Enemy):
    def __init__(self):
        self.Weakness = ["","",""]
        self.Strength = ["",""]
        self.AttackType = "Fernkampf"

class Vampir(Enemy):
    def __init__(self):
        self.Weakness = ["Licht","Knoblauch","Kruzefix"]
        self.Strength = ["Beißen","Kratzen"]
        self.AttackType = "Nahkampf"

class Ork(Enemy):
    def __init__(self):
        self.Weakness = ["Komplexität"]
        self.Strength = ["Stärke","Widerstand"]
        self.AttackType = "Nahkampf"

class DarkKnight(Enemy):
    def __init__(self):
        self.Weakness = ["Magie","Keine Ruestung"]
        self.Strength = ["Ruestung","Dunkle Magie"]
        self.AttackType = "Nahkampf"

class Skelett(Enemy):
    def __init__(self):
        self.Weakness = ["Gebrächlich","Schwach"]
        self.Strength = ["Milch"]
        self.AttackType = "Fernkampf"

class DragonClass(Enemy):
    pass

class FireDragon(DragonClass):
    pass

class WaterDragon(DragonClass):
    pass

class EarthDragon(DragonClass):
    pass

class AirDragon(DragonClass):
    pass

class Diabolo(Enemy):
    pass

if __name__ == "__main__":
    pass