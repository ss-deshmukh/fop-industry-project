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

#problem 3

def div_3(num):
    if num %3==0:
        return("divisible by 3")
    else:
        return("not divisible by 3")
a=4
b=9
c=19
print("a",div_3(a))
print("b",div_3(b))
print("C",div_3(C))
        
