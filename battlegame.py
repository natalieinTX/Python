wizard = 1
elf = 2
human = 3

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_damage = 25

while True:
    dragon_hp = 500

    while True:
        print("Choose Wizard (1), Elf (2), or Human (3)")
        character = int(input("Choose your character: "))
        
        if character == 1:
            character_name = "wizard"
            my_hp = wizard_hp
            my_damage = wizard_damage
            print("You chose the wizard")
            break
        elif character == 2:
            character_name = "elf"
            my_hp = elf_hp
            my_damage = elf_damage
            print("You chose the elf")
            break
        elif character == 3:
            character_name = "human"
            my_hp = human_hp
            my_damage = human_damage
            print("You chose the human")
            break
        else:
            print("Unknown character. Please choose again.")
            continue

    while True:
        dragon_hp -= my_damage
        print("The " + character_name + " damaged the dragon!")
        print("The dragon's hitpoints are now: " + str(dragon_hp))
        if dragon_hp <= 0:
            print("The dragon is dead! You win!")
            break

        my_hp -= dragon_damage
        print("The dragon strikes back! Your hitpoints are now: " + str(my_hp))
        if my_hp <= 0:
            print("You are dead. Game over!")
            break

        if my_hp <= 30:
            print("The " + character_name + " has lost the battle.")
            break

    play_again = input("Do you want to go on another adventure? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for visiting the realm! Goodbye!")
        break