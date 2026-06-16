def rectangle():
    l=int(input("enter length of rectangle -->"))
    b=int(input("enter breadth of rectangle -->"))
    area=l*b
    perimeter=2*(l+b)
    return area,perimeter
def circle():
    r=int(input("enter radius of circle -->"))
    pi=3.142
    area=pi*r*r
    circumference=2*pi*r
    return area,circumference
def box():
    while True:
        l=int(input("enter length of box -->"))
        w=int(input("enter width of box -->"))
        h=int(input("enter height of box -->"))
        if (h==0 or w==0 or l==0):
            print("this shape is not cube, enter again")
        else:
            break
    volume=l*w*h
    surf_area=2*(l*w+l*h+w*h)
    return volume,surf_area
def main(): #sai
    x=input("your shape is(rectangle/circle/cube) -->")
    while True:
        if x=="rectangle":
            area,perimeter=rectangle()
            print("area : ",area)
            print("perimeter : ",perimeter)
            break
        elif x=="circle":
            area2,circumference=circle()
            print("area : ",area2)
            print("circumference : ",circumference)
            break #sai
        elif x=="cube":
            volume,surf_area=box()
            print("volume : ",volume)
            print("surface area : ",surf_area)
            break
        else:
            x=input("type correctly(rectangle/circle/cube) -->")
main()
            
