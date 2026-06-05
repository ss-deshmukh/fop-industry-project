s = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",  "k", "l", "m", "n", "o", "p", "q", "r", "s",  "t", "u", "v", "w", "x", "y", "z"}

v = 0
c= 0

vowels = "aeiou"

for x in s:
    if x in vowels:
        v = v + 1  
    else:
        c = c+ 1  

print("Total Vowels:", v)
print("Total Consonants:", c)
