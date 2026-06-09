s = {'a', 'b', 'c', 'd'}

s.update({'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z'})

print(s)
#problem 

s = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
     'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u',
     'v', 'w', 'x', 'y', 'z'}

c = 0

for x in s:
    if x == 'a':
        c = c + 1
    elif x == 'e':
        c = c + 1
    elif x == 'i':
        c = c + 1
    elif x == 'o':
        c = c + 1
    elif x == 'u':
        c = c + 1
    else:
        continue

print("Number of vowels =", c)
#problem 
s = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
     'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u',
     'v', 'w', 'x', 'y', 'z'}

c = 0

for x in s:
    if x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u':
        c = c + 1

print("Number of consonants =", c)
#problem 
letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z'}

vowels = set()
consonants = set()

for ch in letters:
    if ch in {'a', 'e', 'i', 'o', 'u'}:
        vowels.add(ch)
    else:
        consonants.add(ch)

print("Vowels Set =", vowels)
print("Consonants Set =", consonants)
#problem
num = 10
guess = int(input("Guess a number 1 to 10: "))

if guess == num:
    print("Correct guess")
elif guess < num:
    print("Too low")
else:
    print("Too high")


