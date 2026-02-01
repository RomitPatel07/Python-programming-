def arith():
    a=int(input("Enter a length:"))
    b=int(input("Enter a breadth:"))
    if a*b>2*(a+b):
         print("Area of rectangle is than its perimeter")
    else:
        print("Perimeter is greater than area of rectangle")
arith()        
