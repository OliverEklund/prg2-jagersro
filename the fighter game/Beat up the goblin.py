def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Skriv ett nummer.")

Player = {"Health": 100, "Attack": 10}
John_Goblin = {"Name": "Goblin", "Health": 50, "Attack": 10, "Armor": 15}

turn = True
while turn is True:

    print(f"A {John_Goblin['Name']} with {John_Goblin['Health']} health stands in front of you. What do you do?")
    print("1: Attack him")
    print("2: NOTHING")
    player_choice = input_int("")

    if player_choice == 1:
       John_Goblin["Health"] -= Player["Attack"]


    if player_choice == 2:
        print("You do nothing")



    if Player["Health"] <=0:
        print("YOU ARE DEAD")
        turn = False
    if John_Goblin["Health"] <=0:
        print("YOU WON")
        turn = False

        #print("Which bodypart?")
        #print("1: Head")
        #print("2: Torso")
        #print("3: Arms")
        #print("4: Legs")