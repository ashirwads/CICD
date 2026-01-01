def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    else: 
        return a / b
    

    #def get_weather(temp):
#    if temp > 20:
#        return "hot" 
#    else:
#       return "cold"
    

#def is_even(n):
#    return n % 2 == 0

#def reverse_string(s):
#    return s[::-1]
