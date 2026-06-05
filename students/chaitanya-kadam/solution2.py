#problem 1
s={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
count=0
for x in s:
    if x=='a':
        count=count+1
    elif x=='e':
        count=count+1
    elif x=='i':
        count=count+1
    elif x=='o':
        count=count+1
    elif x=='u':
        count=count+1
    else:
        continue
print(count)

#problem 2
s={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
count=0
v={'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
for x in s:
    if x in v:
        count=count+1
print(count)

#problem 3
