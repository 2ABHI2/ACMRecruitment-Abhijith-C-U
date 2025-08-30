for kid in range(1, 101):  
    if kid % 3 == 0 and kid % 5 == 0:
        print("FizzBuzz")  
    elif kid % 3 == 0:
        print("Fizz")       
    elif kid % 5 == 0:
        print("Buzz")    
    else:
        print(kid) 