#problem 
#greet name
def greet():
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    print("Hi",name+"!Next year you will be", age+1)
greet()


#problem 
#while number 
num=10
while True:
    uinp=int(input("1,2,3,4,5,6,7,8,9,10"))
    if uinp!=num :
         print("incorrect")
    else:
         print("correct")
         break
