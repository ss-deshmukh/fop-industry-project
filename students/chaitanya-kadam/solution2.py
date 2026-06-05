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

s={"a", "b", "c", "d", "e", "f", "g", "h","i","k" "m", "n", "o", "p" "s", "t", "u", "v", "w", "x", "y", "z"}
total_vowels = 0
total_consonants = 0
vowels_ref = "aeiou"
for letter in s:
    if letter in vowels_ref:
        total_vowels = total_vowels + 1
    else:
        total_consonants = total_consonants+1
print("Total Vowels:", total_vowels)
print("Total Consonants:", total_consonants)
