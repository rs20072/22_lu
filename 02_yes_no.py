
show_instructions = ""
while show_instructions != "xxx":
    show_instructions = input("have you played this game before? ").lower()

    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")

    elif show_instructions == "Y":
        print("program continues")

    elif show_instructions == "no":
        print("display instructions")

    elif show_instructions == "n":
        print("display instructions")

    else:
        print("please enter yes or no")



        
