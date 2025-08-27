Player_horse = {'name': "name", 'speed': 0, 'agility': 0}

John_Prancer = {'name': "John Prancer", 'speed': 5, 'agility': 3}

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Skriv ett nummer.")