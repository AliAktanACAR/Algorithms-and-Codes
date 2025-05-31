import random

# Base class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} attacks {other.name} and deals {damage} damage!")

    def is_alive(self):
        return self.health > 0

# Hero class (inherits from Character)
class Hero(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)
        self.potions = 3

    def heal(self):
        if self.potions > 0:
            self.health += 30
            self.potions -= 1
            print(f"{self.name} uses a potion and heals 30 HP!")
        else:
            print("No potions left!")

# Enemy class (inherits from Character)
class Enemy(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=15)

# Game start
hero = Hero("Knight")
enemy = Enemy("Orc")

print("⚔️  Battle Start! ⚔️")
print(f"{hero.name} vs {enemy.name}\n")

# Turn-based combat
while hero.is_alive() and enemy.is_alive():
    print(f"\n{hero.name} HP: {hero.health} | {enemy.name} HP: {enemy.health}")
    action = input("Choose action: [A]ttack or [H]eal: ").lower()

    if action == 'a':
        hero.attack(enemy)
    elif action == 'h':
        hero.heal()
    else:
        print("Invalid action!")

    if enemy.is_alive():
        enemy.attack(hero)

# Game result
if hero.is_alive():
    print(f"\n🎉 {hero.name} won the battle!")
else:
    print(f"\n💀 {hero.name} was defeated...")
