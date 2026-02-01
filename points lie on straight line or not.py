def arith():
    x1=int(input("Enter a x1:"))
    y1=int(input("Enter a y1:"))
    x2=int(input("Enter a x2:"))
    y2=int(input("Enter a y2:"))
    x3=int(input("Enter a x3:"))
    y3=int(input("Enter a y3:"))

    area=1/2*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
    if area ==0:
         print("Points lies on straight line")
    else:
        print("Points does not lie on straight line")
arith()        
