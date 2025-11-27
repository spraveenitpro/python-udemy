flavours = ["Ginder", "Out of Stock", "Lemon", "Tulsi", "Discontinued"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found!")
        break
    print(f"{flavour} item found")

print("Out of the loop")