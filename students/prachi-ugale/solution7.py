def tip_calculator():
    bill = float(input("Enter bill amount: "))
    tip_percent = float(input("Enter tip percentage: "))

    tip = bill * tip_percent / 100
    total = bill + tip

    print(f"Tip: {tip:.2f}")
    print(f"Total: {total:.2f}")

tip_calculator()
