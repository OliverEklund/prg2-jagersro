from random import randint, choice

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Skriv ett nummer osm är 10 eller under.")

while True:
    food = ["Tacos", "Köttgryta", "Korvstroganoff", "Revbenspjäll", "Pastasallad", "Pasta & köttfärssås", "Ryggfile", "Nuggets", "Fries", "Churros", "KebabPizza", "Pizza", "Pölsa", "Ölkorv", "Fisk", "Jello", "Rysgrynsgröt", "Gröt", "Sandwich"]
    print("Skriv nummret som representerar maten du tycker om mest")
    print("Skriv 0 för att rulla om")

    counter = 0
    for i in range(10):
        Food_printed = choice(food)
        counter += 1
        print(f"{counter}: {Food_printed}")
        food.remove(Food_printed)

    user_is_decide = True
    while user_is_decide is True:
        User_fav = input_int("")
        if User_fav == 0:
            user_is_decide = False
        if User_fav > 10:
            print("to large")
        if User_fav < 11:
            print("coolt val")
            
