def perimeter(length, breadth):
    p=2*(length+breadth)
    return p
    
def area(length,bredth):
    a=length*breadth
    return a

l=int(input('Enter the length : '))
b=int(input('Enter the breadth : '))

print(perimeter(l,b))
print(area(l,b))

