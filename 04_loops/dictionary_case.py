users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 140, "coupon": "F20"},
    {"id": 3, "total": 160, "coupon": "E20"},
    {"id": 4, "total": 110, "coupon": "G20"},
]

discounts = {
    "P20": (0.2, 0),
    "F20": (0.5, 0),
    "E20": (0, 10),
    "G20": (0.1, 0)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"])
    discount = user["total"] * percent + fixed
    print(f" User {user["id"]} paid {user["total"]} and got discount of {discount}")
    