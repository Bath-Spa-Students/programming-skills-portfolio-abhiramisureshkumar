#Area of a circle

def area(radius):
    area = 3.14*radius**2
    return area

radius = float(input("enter the radius of the circle: "))
print("the area of the circle is: ",area(radius))