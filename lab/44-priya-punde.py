x=0
while<10:
  x=x+1
print(x)
#problem 2
a=2
b=26
c=37
l=[a,b,c]
for x in l:
  if x%2==0:
    print("even")
  else:
    print("odd")
#problem 3
a=4
b=9
c=19
M=[a,b,c]
for x in M:
  if x%3==0:
    print("division")
  else:
    print("divisiable")
#problem 4
q=[1,2,3]
def number(q):
  for x in q:
    print(x)
number(q)
#problem 5
l=[1,2,3,4,5,6]
l.pop(4)
l.pop(2)
l.pop(0)
print(l)
#problem 6
d=["ram":30,"vijay":40,"radha":60]
print(d["vijay"])
