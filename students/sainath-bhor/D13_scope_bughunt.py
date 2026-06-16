total=0
def add_item(price):
    global total
    total=total+price
    return total
def apply_tax():
    n=int(input("enter % of tax"))
    global t
    t=total*n/100
    return t
def main(): #sai
    add_item(40)
    add_item(25)
    add_item(15)
    print("price :",total)
    print("tax :",apply_tax())
    print("total :",total+t)
main()
