from actors import Creature, Wizard, Dragon, SmallAnimal
import random
import time

def main():
    show_header()
    game_loop()


def show_header():
    print('-----------------------')
    print('     WIZARD BATTLE')
    print('-----------------------')
    print()


def game_loop():

    creatures = [
        SmallAnimal("Toad", 1),
        Creature("Tiger", 12),
        SmallAnimal("Bat", 3),
        Dragon("Dragon", 50, 2, True),
        Wizard("Boss", 100)
    ]

    hero = Wizard("Gandalf", 80)

    while True:

        active_creature = random.choice(creatures)
        print(f"A {active_creature.name} of level {active_creature.level} has appeared from a dark and foggy forest...")
        print()

        cmd = input("Do you [a]ttack, [r]un away, or [l]ook around? ")
        if cmd == "a":
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard retreats and takes time to recover.")
                time.sleep(5)
                print("The wizard returns revitalized.")
        elif cmd == "r":
            print("The wizard has become unsure of his power and flees")
        elif cmd == "l":
            print(f"The wizard {hero.name} looks around and sees:")
            for c in creatures:
                print(f"A {c.name} of level {c.level}")
        else:
            cmd2 = input("Do you want to exit the game? y/n ")
            if cmd2 == "y":
                print("Exiting game. Goodbye.")
                break
            else:
                continue

        if not creatures:
            print("You defeated all the creatures. Well done.")
            break

if __name__ == "__main__":
    main()
