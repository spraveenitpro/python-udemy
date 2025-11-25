value = input("Enter the ticket category you require?").lower()

print (value)

match value:
    case "sleeper":
        print (f"You selected {value}")
    case "ac":
         print (f"You selected {value}")
    case "general":
         print (f"You selected {value}")
    case "luxury":
         print (f"You selected {value}")
    case _:
         print (f"Please enter a predetermined value!!")