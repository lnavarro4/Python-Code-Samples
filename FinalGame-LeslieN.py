
#Leslie Navarro
#CSS 225 Final Game

# Chapter 1 - Room Class

class Room:
    def intro_chap1(self):
        self.description = "It’s a bright and sunny afternoon when you reach the small village. You’re able to get a room at the only inn."
        self.options = {
            'stay': self.stay_in,
            'read': self.read_letter,
            'go_town': self.go_into_town
        }

    def display(self):
        print(self.description)
        print("\nWhat would you like to do?")
        print("1. Stay in")
        print("2. Read letter")
        print("3. Go into town")

    def get_choice(self):
        choice = input("\nEnter the number corresponding to your choice: ")
        return choice

    def stay_in(self):
        print("You decide to stay in the inn. Unfortunately, you don't have the necessary supplies for a journey.")
        print("Game Over.")
        self.end_game()

    def read_letter(self):
        print("\nYou open the letter and read it: 'There have been rumors going around about a treasure hidden "
              "inside the caves of a distant village. If you are interested in searching for it yourself, I've "
              "included a map to help you get to the village. Good luck.'")
        self.game_loop()

    def go_into_town(self):
        print("\nYou leave the room and head towards the bustling town.")
        chapter2 = Town()
        chapter2.intro_chap2()
        chapter2.game_loop()

    def player_choice(self, choice):
        if choice == '1':
            self.stay_in()
        elif choice == '2':
            self.read_letter()
        elif choice == '3':
            self.go_into_town()
        else:
            print("Invalid choice. Please choose again.")
            self.game_loop()

    def game_loop(self):
        self.display()
        choice = self.get_choice()
        self.player_choice(choice)

    def end_game(self):
        print("\nWould you like to try again? (Y/N)")
        choice = input()
        if choice.lower() == 'y':
            start_game()
        else:
            print("Thanks for playing!")
            exit()

# Chapter 2 - Town Class

class Town:
    def intro_chap2(self):
        self.description = ("You start hearing music and laughter as you near the center of the town. "
                            "There seems to be a festival going on with games and rides.")
        self.options = {
            'rides': self.go_on_rides,
            'restaurant': self.into_restaurant,
            'games': self.play_games
        }

    def display(self):
        print(self.description)
        print("\nWhat would you like to do?")
        print("1. Go on rides")
        print("2. Go into restaurant")
        print("3. Play games")

    def get_choice(self):
        choice = input("\nEnter the number corresponding to your choice: ")
        return choice

    def go_on_rides(self):
        print("\nYou spent some of your money to go on the rides.")
        self.game_loop()

    def into_restaurant(self):
        print("\nYou go into the restaurant and saw that an eating contest was about to take place. "
              "You participate and end up winning. You're awarded some money.")

        chapter3 = Shop()
        chapter3.intro_chap3()
        chapter3.game_loop()

    def play_games(self):
        print("\nYou spent some of your money to play a few games.")
        self.game_loop()

    def player_choice(self, choice):
        if choice == '1':
            self.go_on_rides()
        elif choice == '2':
            self.into_restaurant()
        elif choice == '3':
            self.play_games()
        else:
            print("Invalid choice. Please choose again.")
            self.game_loop()

    def game_loop(self):
        self.display()
        choice = self.get_choice()
        self.player_choice(choice)

# Chapter 3 - Shop Class

class Shop:
    def __init__(self):
        self.player_choice = None

    def intro_chap3(self):
        self.description = ("You’re about to call it a day when a shop catches your eye. "
                            "Intrigued, you go inside to find an array of supplies available for purchase.")
        self.options = {
            'sword': self.buy_sword,
            'shoes': self.buy_shoes,
            'nothing': self.save_money
        }

    def display(self):
        print(self.description)
        print("\nWhat would you like to do?")
        print("1. Buy sword")
        print("2. Buy shoes")
        print("3. Buy nothing. Save money.")

    def get_choice(self):
        choice = input("\nEnter the number corresponding to your choice: ")
        return choice

    def buy_sword(self):
        print("\nYou buy a sword and feel ready for anything that comes your way.")
        self.player_choice = 'sword'
        self.start_chap4()

    def buy_shoes(self):
        print("\nYou buy shoes, perfect for a long journey.")
        self.player_choice = 'shoes'
        self.start_chap4()

    def save_money(self):
        print("\nYou decide not to buy anything and save your money.")
        self.player_choice = 'nothing'
        self.start_chap4()

    def start_chap4(self):
        chapter4 = Trolls(self.player_choice)
        chapter4.intro_chap4()
        chapter4.game_loop()


    def handle_choice(self, choice):
        if choice == '1':
            self.buy_sword()
        elif choice == '2':
            self.buy_shoes()
        elif choice == '3':
            self.save_money()
        else:
            print("Invalid choice. Please choose again.")
            self.game_loop()

    def game_loop(self):
        self.display()
        choice = self.get_choice()
        self.handle_choice(choice)



# Chapter 4 - Trolls Class

class Trolls:
    def __init__(self, player_choice):
        self.player_choice = player_choice

    def intro_chap4(self):
        self.description = ("The next morning is just as bright and promising as the one before."
                            "You gather your supplies and begin your journey. "
                            "Suddenly, a group of trolls appears on your path!")
        self.options = {
            'fight': self.fight_trolls,
            'run': self.run_away,
            'bribe': self.bribe_trolls
        }

    def display(self):
        print(self.description)
        print("\nWhat would you like to do?")


        if self.player_choice == 'sword':
            print("1. Fight")
            print("2. Run away")
            print("3. Bribe them to let you through.")
        elif self.player_choice == 'shoes':
            print("1. Fight")
            print("2. Run away")
            print("3. Bribe them to let you through.")
        elif self.player_choice == 'nothing':
            print("1. Fight")
            print("2. Run away")
            print("3. Bribe them to let you through.")

    def get_choice(self):
        choice = input("\nEnter the number corresponding to your choice: ")
        return choice

    def fight_trolls(self):
        if self.player_choice == 'sword':
            print("\nYou draw your sword and prepare for battle!")
            print("You win the fight and continue your journey.")
            self.start_chap5()
        else:
            print("\nYou cannot fight because you didn't buy a sword. You must run or bribe.")
            self.game_loop()

    def run_away(self):
        if self.player_choice == 'shoes':
            print("\nYou decide to run away, narrowly escaping the trolls!")
            print("You continue your journey but lose some time.")
            self.start_chap5()
        else:
            print("\nYou cannot run away because you didn't buy shoes. You must fight or bribe.")
            self.game_loop()

    def bribe_trolls(self):
        if self.player_choice == 'nothing':
            print("\nYou offer them some of your money, and the trolls let you pass.")
            print("You proceed with caution.")
            self.start_chap5()
        else:
            print("\nYou cannot bribe because you bought a sword or shoes. You must fight or run.")
            self.game_loop()

    def start_chap5(self):
        chapter5 = Tunnels()
        chapter5.intro_chap5()
        chapter5.game_loop()


    def handle_choice(self, choice):
        if choice == '1':
            self.fight_trolls()
        elif choice == '2':
            self.run_away()
        elif choice == '3':
            self.bribe_trolls()
        else:
            print("Invalid choice. Please choose again.")
            self.game_loop()

    def game_loop(self):
        self.display()
        choice = self.get_choice()
        self.handle_choice(choice)



# Chapter 5 - Tunnels Class

class Tunnels:

    def intro_chap5(self):
        self.description = "You continue your journey. As the sun starts to set, you finally make it to the cave entrance."
        self.options = {
            '1': self.found_treasure,
            '2': self.wrong_tunnel,
            '3': self.wrong_tunnel
        }

    def display(self):
        print(self.description)
        print("\nThere are three tunnels in front of you. Which way would you like to go?")
        print("1. Left")
        print("2. Straight")
        print("3. Right")

    def get_choice(self):
        choice = input("\nEnter the number corresponding to your choice: ")
        return choice

    def wrong_tunnel(self):
        print("You chose the wrong tunnel. Try again")
        self.game_loop()

    def found_treasure(self):
        print("\nCongratulations! You found the treasure. You make your way back to the inn to rest before going home the next day.")
        exit()

    def handle_choice(self, choice):
        if choice == '1':
            self.found_treasure()
        elif choice == '2':
            self.wrong_tunnel()
        elif choice == '3':
            self.wrong_tunnel()
        else:
            print("Invalid choice. Please choose again.")
            self.game_loop()

    def game_loop(self):
        self.display()
        choice = self.get_choice()
        self.handle_choice(choice)


def start_game():
    chapter1 = Room()
    chapter1.intro_chap1()
    chapter1.game_loop()


start_game()


