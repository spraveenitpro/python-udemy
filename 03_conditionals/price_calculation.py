size = input("Enter the size you require").lower()

if size == "small":
    print(f"The price for {size} is $10")
elif size == "medium":
    print(f"The price for {size} is $15")
elif size == "large":
    print(f"The price for {size} is $20")
else:
    print("Unknown cup size!!")