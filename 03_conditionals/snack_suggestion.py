snack = input("Enter your preferred snack: ").lower()
print(f"user said {snack}")

if snack == "cookies" or snack == "samosa":
    print (f"Great choice! we will serve you {snack}")
else:
    print("That is not currently available!")