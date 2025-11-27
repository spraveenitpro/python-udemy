value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not Divisible, remainder is {remainder}")


if ( remainder := value % 5 ):
    print(f"Not divisible, remainder is {remainder}")

sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your size: ")) in sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable f{requested_size}")