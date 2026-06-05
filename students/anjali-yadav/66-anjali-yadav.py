i=0
sum=0
while i<=10:
    sum=sum+1
    i=i+1
print(sum)
#problem 2
a=4
b=9
c=19
def number(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
number(a)
number(b)
number(c)
#problem 3
a=4 
b=9 
c=19
def number(n):
    if n%3==0:
        print("divisible by 3")
    else:
        print("not divisible")
number(a)
number(b)
number(c)
#problem 4
a=[1,2,3]
def print_list(list):
 for x in list:
     print(x)
print_list(a)
#problem 5
i=0
L=[1,2,3,4,5,6]
L.pop(0)
L.pop(1)
L.pop(2)
print(L)
#problem 6
i=0
L=[1,2,3,4,5,6]
L.pop(4)
L.pop(2)
L.pop(0)
print(L)
