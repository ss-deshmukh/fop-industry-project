#1
def cd():
    n=int(input("number of seconds to countdown -->"))
    while n>0: #sai
        print(n)
        n=n-1
    print("liftoff!")
cd()

#2
def first_multiple():
    x=int(input("enter number which is multiplying -->"))
    n=int(input("enter lowest multiple number you want -->"))
    while True:
        if n%x==0:
            print(n)
            break
        else: #sai
            n=n+1
first_multiple()

#streach problem😉
def count_steps():
    n=int(input("enter number to find steps -->"))
    steps=0
    while True:
        if n==1:
            break
        elif n%2==0:
            n=n/2
            steps=steps+1
        else: #sai
            n=(3*n)+1
            steps=steps+1
    print(steps)
count_steps()
