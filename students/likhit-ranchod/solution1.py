x=0
total=0
while x<10:
  x=x+1
  total=total+1
  print(total)

#problem 2

def even_odd(num):
    if num %2==0:
        return "even"
    else:
        return"odd"
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
print("c",div_3(c))

#problem 4

a=[1,2,3]
def print_fun(a):
  i=0
  for x in a:
    i=i+1
    print(i)
    
print_ele(a)    

#problem5

l=[1,2,3,4,5,6]
l.pop(0)
print(l)
l.pop(1)
print(l)
l.pop(2)
print(l)

#problem6

l=[1,2,3,4,5,6]
l.pop(4)
print(l)
l.pop(2)
print(l)
l.pop(0)
print(l)

  
