def division(x,y):
    try:
        div = x/y
        print(f"{x}/{y}={div}")
    except ZeroDivisionError as e:
        print("Exception occured!:",e)
    except Exception as e:
        print("Exception occured!:",e)
a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
division(a,b)
        
