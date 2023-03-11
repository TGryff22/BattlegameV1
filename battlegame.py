wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 170

wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 110

dragon_hp = 300
dragon_damage = 50

while True:

    while True:
        print("1) " + "Wizard" "\n"  "2) " + "Elf" "\n" "3) " +
              "Human" "\n" "4) " + "Orc"  "\n" "5) " + "Exit")

        character = input("Choose your character or exit the game: ")

        if character.lower() == "1" or character.lower() == "wizard":
            player = "Wizard"
            my_hp = wizard_hp
            my_damage = wizard_damage
            print("You have chosen the character: " "\n" + player,
                  "\n" "Health: ", my_hp, "\n" "Damage: ", my_damage)
            break
        elif character.lower() == "2" or character.lower() == "elf":
            player = "Elf"
            my_hp = elf_hp
            my_damage = elf_damage
            print("You have chosen the character: " "\n" + player,
                  "\n" "Health: ", my_hp, "\n" "Damage: ", my_damage)
            break
        elif character.lower() == "3" or character.lower() == "human":
            player = "Human"
            my_hp = human_hp
            my_damage = human_damage
            print("You have chosen the character: " "\n" + player,
                  "\n" "Health: ", my_hp, "\n" "Damage: ", my_damage)
            break
        elif character.lower() == "4" or character.lower() == "orc":
            player = "Orc"
            my_hp = orc_hp
            my_damage = orc_damage
            print("You have chosen the character: " "\n" + player,
                  "\n" "Health: ", my_hp, "\n" "Damage: ", my_damage)
            break
        elif character.lower() == "5" or character.lower() == "exit":
            exit()
        else:
            print("Unknown Character" "\n")

    while True:
        dragon_hp = dragon_hp - my_damage

        print("\n" "The", player, "damaged the Dragon!")
        print("The Dragon's hitpoints are now: ", dragon_hp)

        if dragon_hp <= 0:
            print("\n" "The Dragon has lost the battle")
            break

        my_hp = my_hp - dragon_damage

        print("\n" "The dragon strikes back at the " + player)
        print("The", player + "'s", "hitpoints are now: ", my_hp)

        if my_hp <= 0:
            print("\n" "The", player, "has lost the battle")
            break

    print("\n" "Would you like to play again? Type yes or no: ")
    again = input()
    if again.lower() == "yes":
        print("\n" "Game starting again!" "\n")
    elif again.lower() == "no":
        print("\n" "Bye")
        exit()
