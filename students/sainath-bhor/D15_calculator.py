def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error: cannot divide by zero"
    return a/b
def mod(a,b):
    if b==0: #sai
        return "Error: cannot divide by zero"
    return a%b

def calculator():
    while True:
        a=float(input("enter first number --> "))
        o=input("enter operator (+ - * / %) --> ")
        b=float(input("enter second number --> "))
        if o=="+":
            result=add(a,b)
        elif o=="-": #sai
            result=subtract(a,b)
        elif o=="*":
            result=multiply(a,b)
        elif o=="/":
            result=divide(a,b)
        elif o=="%":
            result=mod(a,b)
        else:
            print("Unknown operator:",o)
            return
        print(f"{a} {op} {b} = {result}")
        print("="*40)
calculator()
