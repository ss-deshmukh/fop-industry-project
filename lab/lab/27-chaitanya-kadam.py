x=0
total=0
while x<10:
    x=x+1
    total=total+x
 print(total)

#problem 2
def even_odd(number):
    if number%2==0:
        return "even"
    else:
        return "odd"
a=4
b=9
c=19
print("a",even_odd(a))
print("b",even_odd(b))
print("c",even_odd(c))
