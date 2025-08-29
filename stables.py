from random import randint, choice
Player_horse = {'name': "name", 'speed': 3, 'agility': 5}
John_Prancer = {'name': "John Prancer", 'speed': 5, 'agility': 3}

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Skriv ett nummer.")



#computer_horse = create_computer_pony()
#print(computer_horse)