from stables import input_int

Player_horse = {'name': "name", 'speed': 0, 'agility': 0, 'stat_attribution': True}
print("Skapa din häst! Din häst har speed och agility, max 6 i en stat, max 8 totalt")
Player_horse['name'] = input("Vad heter din häst?: ")


while Player_horse.get('stat_attribution') == True:
    Player_horse['speed'] = input_int("Hur snabb är din häst? (1-7): ")
    Player_horse['agility'] = input_int("Hur smidig är din häst? (1-7): ")

    if Player_horse.get('agility') + Player_horse.get('speed') > 8 or Player_horse.get('agility') + Player_horse.get('speed') < 8:
        print("Felinput. Speed och agility måste vara ett nummer mellan 1-6 och vara 8 totalt")
    else:
        Player_horse['stat_attribution']=False


print("lets ago")
print(f"Så här är din häst: {Player_horse}")