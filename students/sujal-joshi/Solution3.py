#problem1
def greet():
    name = input("Sujal")
    age = int(input("29"))
    
    print(f"Hi {name}! Next year you will be {age + 1}.")

greet()

#problem2
def tip_calculator():
    bill = float(input("850.50 "))
    tip_percent = float(input("12"))

    tip = (bill * tip_percent) / 100
    total = bill + tip

    print(f"Tip: {tip:.2f}")
    print(f"Total: {total:.2f}")

tip_calculator()
