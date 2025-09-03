def input_name(prompt = "Skriv ditt namn: ", lenght = 2) => str:
    name = ""
    while len(name)<lenght:
        name = input(prompt)
    return name