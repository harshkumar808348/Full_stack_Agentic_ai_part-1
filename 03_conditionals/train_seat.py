seat_type =input("Enter seat type (sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper -NO Ac , beds are availbale")
    case "ac":
        print("Ac - Air conditione ,comfy ride")
    case "general":
        print("General-cheepeat optionm no , reversation")
    case "luxary":
        print("Luxary - Preminuum seats wiht meals")
    case _:
        print("Invalid seat type")
        

    