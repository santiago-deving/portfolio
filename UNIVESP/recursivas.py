def countdown(num):
    if (num < 0):
        print("Lançar!!!")
    
    else:
        print(num)
        countdown(num - 1)

def fibon(num):
    if (num<=1):
        return 1
    else:
        return fibon(num-1) + fibon(num-2)
        
def func(n): 
    if n <= 1: 
        return 1 
    else: 
        return n * func(n - 1) 
