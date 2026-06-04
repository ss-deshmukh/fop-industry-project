x=0
while x<10:
    x=x+1
print(x)
# problem 2
a=4
b=9
c=19
def number(n):
    if n % 2==0:
      print("even")
    else:
        print("odd")
number(a)
number(b)
number(c)
#problem3
a=4
b=9
c=19
def number(n):
    if n%3==0:
        print("devisible by 3")
    else:
        print("not divisible by 3")
number(a)
number(b)
number(c)
#problem4
a=[1,2,3]
def element(list):
    for x in list:
        print(x)
element(a)
#problem5
l=[1,2,3,4,5,6]
l.pop(0)
l.pop(1)
l.pop(2)
print(l)
#problem6
l=[1,2,3,4,5,6]
l.pop(4)
l.pop(2)
l.pop(0)
print(l)


