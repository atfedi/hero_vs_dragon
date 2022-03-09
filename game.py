import random

try:
    hero_hp = int(input("how many hp does the hero have? "))
except:
    hero_hp = 50
try:
    dragon_hp = int(input("how many hp does the dragon have? "))
except:
    dragon_hp = 100
try:
    hero_max_dmg = int(input("what is the max damage caused by the hero? "))
except:
    hero_max_dmg = 20
try:
    dragon_max_dmg = int(input("what is the max damage caused by the dragon? "))
except:
    dragon_max_dmg = 10
finally:
    print("\nThe dragon with", dragon_hp, "hp attacks out hero with", hero_hp, "hp\n")
while True:
    dragon_attack = random.randint(1, dragon_max_dmg)
    hero_hp = hero_hp - dragon_attack

    print("The dragon does", dragon_attack, "damage and the hero has", hero_hp, "hp left")

    if hero_hp <= 0:
        print("\nUnfortunately the dragon killed our hero. RIP sir Bravealot")
        break

    hero_attack = random.randint(1, hero_max_dmg)
    dragon_hp = dragon_hp - hero_attack

    print("The hero does", hero_attack, "damage and the dragon has", dragon_hp, "hp left\n")

    if dragon_hp <= 0:
        print("\nOur valiant hero has slain the dragon!")
        break

    input("Round over. Press any key")