import random
import time


def print_sleep(message_to_print):
    print(message_to_print)
    time.sleep(.5)


def intro(enemy, weapon):
    print_sleep("You find yourself standing in an open field")
    print_sleep("filled with grass and yellow wildflowers.")
    print_sleep("Rumor has it that a " + enemy + " is somewhere around here, ")
    print_sleep("and has been terrifying the nearby village.")
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep("In your hand you hold your trusty")
    print_sleep("(but not very effective dagger)")


def path(enemy, weapon):
    while True:
        path = input("Enter 1 to knock on the door of the house.\n"
                     "Enter 2 to peer into the cave.\n"
                     "What would you like to do?\n"
                     "(Please enter 1 or 2.)")
        if path == '1':
            approach_house(enemy, weapon)
            if "sword" in weapon:
                house(enemy, weapon)
            else:
                print_sleep("You feel a bit under-prepared for this, "
                            "what with only having a tiny dagger.")
                house(enemy, weapon)
        else:
            if path == '2':
                cave(enemy, weapon)


def approach_house(enemy, weapon):
    print_sleep("You approach the door of the house.")
    print_sleep("You are about to knock when the door opens an "
                "out steps a " + enemy + ".")
    print_sleep("Eep! This is the " + enemy + "'s house!")
    print_sleep("The " + enemy + " attacks you!")


def house(enemy, weapon):
    if "sword" in weapon:
        choice = input("What would you like to do, (1) fight or (2) run away?")
        if choice == '1':
            print_sleep("As the " + enemy + " moves to attack, you "
                        "unsheath your new sword.")
            print_sleep("The Sword of Ogoroth shines brightly in your hand "
                        "as you brace yourself for the attack")
            print_sleep("But the " + enemy + " takes one look at your shiny "
                        "new toy and runs away!")
            print_sleep("You have rid the town of the " + enemy + ". You are "
                        "victorious!")
            play_again()
        elif choice == '2':
            print_sleep("You run back into the field. Luckily, you don't seem "
                        "to have been followed")
            path(enemy, weapon)
        else:
            house(enemy, weapon)
    else:
        choice = input("What would you like to do, (1) fight or (2) run away?")
        if choice == '1':
            print_sleep("You do your best...")
            print_sleep("but your dagger is no match for the " + enemy + ".")
            print_sleep("You have been defeated!")
            play_again()
        elif choice == '2':
            print_sleep("You run back into the field. Luckily, you don't seem "
                        "to have been followed")
            path(enemy, weapon)
        else:
            house(enemy, weapon)


def cave(enemy, weapon):
    print_sleep("You peer cautiously into the cave.")
    if "sword" in weapon:
        print_sleep("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
        print_sleep("You walk back into the field.")
        path(enemy, weapon)
    else:
        print_sleep("It turns out to be only a very small cave.")
        print_sleep("Your eye catches a glint of metal behind a rock.")
        print_sleep("You have found the magical Sword of Ogoroth!")
        print_sleep("You discard your silly old dagger and take the sword "
                    "with you.")
        print_sleep("You walk back out to the field.")
        weapon.append("sword")
        path(enemy, weapon)


def play_again():
    while True:
        play_again = input("Would you like to play again? yes or no?")
        if play_again == 'yes':
            print_sleep("Excellent! Restarting the game ...")
            play_game()
        else:
            if play_again == 'no':
                print_sleep("Thanks for playing! See you next time.")


def play_game():
    weapon = []
    enemies = ("warlock", "wicked fairy", "pirate", "gorgon", "dragon",
               "troll")
    enemy = random.choice(enemies)
    intro(enemy, weapon)
    path(enemy, weapon)


play_game()
