def calculate_bill(cups, price_per_cup):
    return int(cups) * price_per_cup


def add_vat(price, vat_rate):
    vat_amount = price * (vat_rate / 100)
    return vat_amount


print (f"Total bill is {calculate_bill(4, 4.5)} and VAT amount is {add_vat(calculate_bill(4, 4.5), 10)}")
print (f"Total bill is {calculate_bill(3,6.5)} and VAT amount is {add_vat(calculate_bill(3,6.5), 10)}")
print (f"Total bill is {calculate_bill(5,3.4)} and VAT amount is {add_vat(calculate_bill(5,3.4), 10)}")


orders = [100, 150, 300, 50, 200]

for order in orders:
    final_amount = add_vat(order, 10)
    print(f"Order amount is {order} and final amount is {final_amount}")