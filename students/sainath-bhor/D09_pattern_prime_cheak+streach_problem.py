#1
def stars_tri():
    n=int(input("enter number of rows -->"))
    symbol=str(input("enter symbol -->"))
    for a in range(1,n+1):
        print(symbol*a) #sai
stars_tri()

#2
def prime_cheak():
    n=int(input("enter number to chek prime or not -->"))
    for a in range(2,n):
        if n%a==0: #sai
            print(n," is not prime number")
            return
    print(n," is prime number")
prime_cheak()

#streach_problem😉
def primes_():
    n=int(input("enter highest number -->"))
    for x in range(2,n+1):
        isprime=True #sai
        for a in range(2,x):
            if x%a==0:
                isprime=False
                break
        if isprime:
            print(x)
primes_()
