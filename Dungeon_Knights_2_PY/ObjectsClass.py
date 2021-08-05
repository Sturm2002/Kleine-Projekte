"""

GameObject
   V
Chests,      Items,Trader
   V           V
LightChest     V
               V
       Schwerter,Wand,Bow,Consumables
                  V            V
            Dark Mage, Mage    V
                           Potions,Lockpicks
                             V
                           Health,Mana,Armor
                             V
                        Small,Big

"""

from globalVars import *

class GameObject():
   pass

class Chest(GameObject):
   pass

class LightChest(Chest):
   pass

class MediumChest(Chest):
   pass

class HardChest(Chest):
   pass

class Items(GameObject):
   pass

class Schwert(Items):
   pass

class Wand(Items):
   pass

class DarkWand(Wand):
   pass

class LightWand(Wand):
   pass

class Bow(Items):
   pass

class Consumables(Items):
   pass

class Potions(Consumables):
   pass

class Healing(Potions):
   pass

class Strength(Potions):
   pass

class Armor(Potions):
   pass

class Mana(Potions):
   pass

class Lockpick(Consumables):
   pass

class Trader(GameObject):
   pass



if __name__ == "__main__":
    pass