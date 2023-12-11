import time
from rich import print

class AdventureGame:
    def __init__(self):
        self.name = ""

    def clear_screen(self):
        print("\n" * 200)

    def introduction(self):
        self.clear_screen()
        print("[bold underline]<<<<<<Mystical Quest>>>>>>[/bold underline]\n\n")
        time.sleep(3)
        print("\nIn a land of magic and mystery, a hero emerges from the shadows.")
        time.sleep(1)
        self.name = input("What is the name of this mysterious adventurer? > ")
        print(f"{self.name}, the enigmatic mage, staff in hand and ready for an extraordinary journey!")
        time.sleep(1)
        print("Dark forces are stirring in the shadows....")
        time.sleep(1)
        print("A pair of glowing eyes observes the hero...")
        time.sleep(1)
        print(f"Will {self.name} triumph and unravel ancient secrets, or succumb to the forces of darkness...?")
        time.sleep(1)
        print("\n" * 3)
        print("The fate of the realm hangs in the balance...\n...\n...\n...")

    def game_start(self):
        self.clear_screen()
        print("You find yourself at the crossroads of destiny. There's little gold in your pouch, "
              "but your magical powers are at their peak.")
        print("In the vicinity, three figures catch your attention: A mysterious wanderer and a pair of enchanted guardians.")

        while True:
            print("\n----------")
            print("Do you approach the...\n")
            print("1. Mysterious wanderer")
            print("2. Enchanted guardians")
            print("help - if you seek guidance")
            print("quit - to abandon your quest")

            cmd = input(f"{self.name}> ").lower()

            if cmd == "1":
                self.approach_mysterious_wanderer()
            elif cmd == "2":
                self.approach_enchanted_guardians()
            elif cmd == "help":
                print("Choose your actions wisely. Type 'quit' to leave the mystical quest.")
            elif cmd == "quit":
                print("\n-----------")
                time.sleep(1)
                print(f"{self.name} decides to return to their sanctuary, leaving the realm to its mysterious fate...")
                time.sleep(5)
                break
            else:
                print("Unknown command. Type 'help' for assistance.")

    def approach_mysterious_wanderer(self):
        self.clear_screen()
        print(f"You approach the mysterious wanderer and exchange greetings.")
        print(f"The wanderer, with a knowing smile, whispers:")
        print(f"Bring me a rare herb, and I shall reveal the location of a hidden artifact...")
        time.sleep(2)

    def approach_enchanted_guardians(self):
        self.clear_screen()
        print(f"You walk up to the enchanted guardians and acknowledge their presence.")
        print(f"The guardians, with glowing auras, speak in unison:")
        print(f'"{self.name}, seeker of mysteries, prove your worth to pass through our sacred portal..."')
        time.sleep(2)

if __name__ == "__main__":
    adventure_game = AdventureGame()
    adventure_game.introduction()
    adventure_game.game_start()
