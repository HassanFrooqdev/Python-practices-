#1. Write a function to calculate the area of a circle given its radius.
def Area_circle(radius):
    pi = 3.14 
    area= pi*(r*r)
    return area

r= float(input("Enter the radius: "))
print(Area_circle(r))
