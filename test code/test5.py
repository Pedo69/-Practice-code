unit = int(input("Enter the unit number: "))
price = float(input("Enter thr price: "))
member = input("You are a member ? (yes/no): ")
total = unit * price
if member == "yes":
    if total <= 500:
        discount = total * 0.1
    elif total >= 500 and total < 1000:
        discount = total * 0.15
    elif total > 1000:
        discount = total * 0.2
    else:
        print("Invalid input")
elif member == "no":
    if total <= 500:
        discount = total * 0.05
    elif total >= 500 and total < 1000:
        discount = total * 0.1
    elif total > 1000:
        discount = total * 0.15
    else:
        print("Invalid input")

amount = total - discount
print(f"Total amount: {total:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Amount after discount: {amount:.2f}")