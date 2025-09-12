from random import randint

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Skriv ett nummer.")

while True:
    print("/")
    print("Ny Runda har börjat")
    times_guessed = 1
    Number = randint(1,10)
    Guess_amount = input_int("Hur många gissningar tror du det kommer ta?: ")

    player_Question = True
    while player_Question is True:
        print("Gissa talet från 1-10.")
        player_answer = input_int("")

        if player_answer == Number and times_guessed == Guess_amount :
            print("Du Vann och med rätt antal gissningar!")
            player_Question = False

        elif player_answer == Number:
            print("Du Vann!")
            player_Question = False
        
        else:
            print("Försök igen!")
            times_guessed += 1