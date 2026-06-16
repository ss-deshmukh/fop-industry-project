#problem 1total = 0

def add_item(price):
    global total
    total += price
    return total

def apply_tax():
    return total * 1.05

def main():
    add_item(40)
    add_item(25)
    add_item(15)

    print(f"Items added. Cart total: {total}")
    print(f"With 5% tax: {apply_tax():.2f}")

if __name__ == "__main__":
    main()
  
  #problem 2
def get_name():
    return input("Name: ")

def get_city():
    return input("city: ")
    
def get_language():
    return input("language: ")

def main():
    name = get_name()
    city = get_city()
    language = get_language()

main()

#problem 3
def rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

a, p = rectangle(5, 3)
print("Area:", a)
print("Perimeter:", p)
