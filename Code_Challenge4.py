print("Welcome to the Manga/Manhwa Reader Recomender")
print("Answer a few questions to find your next read")
genre = input("What genre do you like? (comedy, action, romance):")


if genre == "comedy":
    length = input("How long the mangga should be? (short, medium, long):")
    
    if length == "short":
        colored = input("Which on you like? (colored, black and white): ")

        if colored == "colored":
            print("We recomend: I'm Not That Kind Of Talent")
        if colored == "black and white":
            print("We Recomend: Kagurabachi")

    elif length == "medium":
        colored = input("Which on you like? (colored, black and white): ")

        if colored == "colored":
            print("We recomend: The Greatest Estate Designer")
        if colored == "black and white":
            print("We Recomend: Kaiju No. 8")

    elif length == "long":
        colored = input("Which on you like? (colored, black and white): ")
        
        if colored == "colored":
            print("We recomend: Eleceed")
        if colored == "black and white":
            print("We Recomend: Jagaaaaaan")
    else:
        print("Invalid")

elif genre == "action":
    length = input("How long the mangga should be? (short, medium, long):")
    
    if length == "short":
        colored = input("Which on you like? (colored, black and white): ")

        if colored == "colored":
            print("We recomend: Dig or Die")
        if colored == "black and white":
            print("We Recomend: kyoushitsu Jibaku Club")

    elif length == "medium":
        colored = input("Which on you like? (colored, black and white): ")

        if colored == "colored":
            print("We recomend: God Game")
        if colored == "black and white":
            print("We Recomend: Terror Man")

    elif length == "long":
        colored = input("Which on you like? (colored, black and white): ")
        
        if colored == "colored":
            print("We recomend: Demonic Emperor")
        if colored == "black and white":
            print("We Recomend: Tokyo Ghoul")
    else:
        print("Invalid")

elif genre == "romance":
    length = input("How long the mangga should be? (short, medium, long):")
    
    if length == "short":
        colored = input("Which on you like? (colored, black and white): ")

        if colored == "colored":
            print("We recomend: Reign Of The Seven Speelblades")
        if colored == "black and white":
            print("We Recomend: Companyy and Prvate Life")

    elif length == "medium":
        colored = input("Which on you like? (colored, black and white): ")

        if colored == "colored":
            print("We recomend: Unholy Blood")
        if colored == "black and white":
            print("We Recomend: Orange")

    elif length == "long":
        colored = input("Which on you like? (colored, black and white): ")
        
        if colored == "colored":
            print("We recomend: True Beauty")
        if colored == "black and white":
            print("We Recomend: Skip Beat")
    else:
        print("Invalid")
else:
    print("Invalid")