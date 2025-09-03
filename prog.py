from stables import input_int
from random import randint, choice


Player_horse = {'name': "name", 'speed': 0, 'agility': 0, 'stat_attribution': True}
print("Skapa din häst! Din häst har speed och agility, max 7 i en stat, max 8 totalt")
Player_horse['name'] = input("Vad heter din häst?: ")


while Player_horse.get('stat_attribution') == True:
    Player_horse['speed'] = input_int("Hur snabb är din häst? (1-7): ")
    Player_horse['agility'] = input_int("Hur smidig är din häst? (1-7): ")

    if Player_horse.get('agility') + Player_horse.get('speed') > 8 or Player_horse.get('agility') + Player_horse.get('speed') < 8 or Player_horse.get('speed')<1 or Player_horse.get('agility')<1 :
        print("Felinput. Speed och agility måste vara ett nummer mellan 1-6 och vara 8 totalt")
    else:
        Player_horse['stat_attribution']=False

print(f"Så här är din häst: Name: {Player_horse.get('name')} Speed: {Player_horse.get('speed')} Agility: {Player_horse.get('agility')}")

print("/")

def create_computer_pony():
    speed = randint(1,6)
    names=["RoboHorse", "Clanker", "Goldship", "horsie", "john hooves", "Gatling Horse", "Karl", "John Pony", "Elvis Ponies", "Man O'War", "American Johnny", "El Diablo", "Kunst", "Adam Horser"]
    horse = {'name':choice(names), 'speed': speed, 'agility': 8-speed}
    return horse

computer_horse = create_computer_pony()

print(f"Din häst kommer spela emot {computer_horse}. Hästen som tar sig längst under given tid (10 enheter) vinner. Hur långt det blir är uträknat med hästens (speed + 1 till 6) - (agility - 1 till 6)")
start = input("Enter för att Starta: ")

def game_turn():
    player_speed = Player_horse['speed'] + randint(1,6)
    player_agility = Player_horse['agility'] - randint(1,6)
    if player_agility > 0:
        player_speed -= player_agility
    
    computer_speed = computer_horse['speed'] + randint(1,6)
    computer_agility = computer_horse['agility'] - randint(1,6)
    if computer_agility > 0:
       computer_speed -= computer_agility
    
    return [player_speed, computer_speed]

for i in range(10):
    steps = game_turn
