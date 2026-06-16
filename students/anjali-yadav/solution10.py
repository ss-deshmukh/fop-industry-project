#problem 1
def add_item(total, price):
    return total + price
def apply_tax(total):
    return total * 1.05
def main():
    total = 0
    total = add_item(total, 40)
    total = add_item(total, 25)
    total = add_item(total, 15)
    print("Cart total:", total)
    taxed_total = apply_tax(total)
    print("With tax:", taxed_total)
main()
