from random import randint, choice
#Player_horse = {'name': "name", 'speed': 3, 'agility': 5, 'stat_attribution': True}}
#John_Prancer = {'name': "John Prancer", 'speed': 5, 'agility': 3}
#computer_horse = create_computer_pony()
#print(computer_horse)

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Skriv ett nummer.")


def input_clamp(stat_name, prompt, clamp = 7):
    while Player_horse[stat_name] < 1 or Player_horse[stat_name] > clamp:
        Player_horse[stat_name] = input_int(prompt)