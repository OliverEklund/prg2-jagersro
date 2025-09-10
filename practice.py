horses = [
    {"name": "John Prancer", "speed": 5, "agility": 3},
    {"name": "El Diablo", "speed": 7, "agility": 1},
    {"name": "Kunst", "speed": 3, "agility": 5},
    {"name": "Clanker", "speed": 3, "agility": 5},
    {"name": "John Prancer", "speed": 5, "agility": 3},
    {"name": "El Diablo", "speed": 7, "agility": 1},
    {"name": "Karl", "speed": 3, "agility": 5},
    {"name": "Clanker", "speed": 1, "agility": 7},
    {"name": "Goldship", "speed": 4, "agility": 4},
    {"name": "Gatling Horse", "speed": 3, "agility": 5},
    {"name": "Elvis Pony", "speed": 5, "agility": 3},
    {"name": "Man'O War", "speed": 2, "agility": 6}

]

def print_horse_info(horse: dict) -> None:
    print(f"{horse['name']} är en häst som har {horse['speed']} speed och {horse['agility']} agility")

for horse in horses:
    print_horse_info(horse)

print("//")
print(horses[1])
print("//")
print_horse_info(horses[0])