set={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
c=0
for x in set:
    if x not in ('a','e','i','o','u'):
         c=c+1
print(c)
