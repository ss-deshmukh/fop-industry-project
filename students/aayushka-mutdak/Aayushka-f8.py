#problem 
def add_item(running_total, price):
    return running_total + price

def apply_tax(cart_total):
    return cart_total * 1.05

def main():
    total = 0
    total = add_item(total, 40)
    total = add_item(total, 25)
    total = add_item(total, 15)

    print(f"Items added. Cart total: {total}")
    print(f"With 5% tax: {apply_tax(total):.2f}")

if __name__ == "__main__":
    main()
  #problem
  def name():
    name = input("Enter your name: ")
    return(name)
def age():
    age = int(input("Enter your age: "))
    return(age)
def city():
    city = input("Enter your city: ")
    return(city)
def lang():
    fav_lang = input("Enter your favourite programming language: ")
    return(fav_lang)
def year():
    years = int(input("How many years have you been coding? "))
    return(years )
    
    bio = f"""
**About Me*
Name: {a}
Age: {b}
City: {c}
Favourite Language: {d}
Years Coding: {e}
"""
    
    return(bio)

def main():
    a=name()
    b=age()
    c=city()
    d=lang()
    e=year()
    print (f"{a}\n{b}\n{c}\n{d}\n{e}\n")
main()
#problem
def rectangle(l,b):
    rarea=l*b
    return(rarea)
def circle(r):
    carea=3.14*r*r
    return(carea)
def main():
    a=rectangle(2,3)
    b=circle(3)
    print(a)
    print(b)
    
main()
#problem
def add_item(running_total, price):
    return running_total + price

def apply_tax(cart_total):
    return cart_total * 1.05

def main():
    total = 0
    total = add_item(total, 40)
    total = add_item(total, 25)
    total = add_item(total, 15)

    print(f"Items added. Cart total: {total}")
    print(f"With 5% tax: {apply_tax(total):.2f}")

if __name__ == "__main__":
    main()
