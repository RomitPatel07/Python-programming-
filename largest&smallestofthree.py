def arith():
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=int(input("Enter c:"))
    if a<b and c<b:
         print("b is largest ")
    elif a>b and a>c:
        print("a is largest")
    else:
        print("c is largest")
arith()        
