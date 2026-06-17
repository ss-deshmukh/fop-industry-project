#problem 1
PASS_MARK = 35
DISTINCTION_MARK = 75

def classify_result(average):
    if average < PASS_MARK:
        return "FAIL"
    elif average >= DISTINCTION_MARK:
        return "DISTINCTION"
    else:
        return "PASS"

print(classify_result(84.3))  
print(classify_result(55.0))  
print(classify_result(31.0))  

#problem2
def x(a):
    if a >= 90:
        print ("A")
    elif a >= 80:
        print ("B")
    elif a >= 70:
        print ("C")
    elif a >= 60:
        print ("D")
    else:
        print ("F")

print(x(84.3))  
print(x(55.0))  
print(x(92.0)) 


#problem3
def x(a, b, c):
    return f"{a}, {b}, {c}"

print(x(85, 90, 78))  
print(x(30, 28, 35))
