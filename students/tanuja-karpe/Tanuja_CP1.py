def average_of_three(m1,m2,m3):
 result=(m1+m2+m3)/3
 return(result)
def classify_result(result):
    if(result>=75):
        return("destination")
    elif(result>=35):
         return("pass")
    else:
        return("fail")
def grade(result):
    if(result>=90):
         return("A")
    elif(result>=80):
           return("B")
    elif(result>=70):
         return("C")
    elif(result>=60):
          return("D")
    else: 
          return("F")
def format(m1,m2,m3):
        return(f"{m1},{m2},(m3}")
 
    
