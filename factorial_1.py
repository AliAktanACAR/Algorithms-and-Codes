def factorial(a):
    result = 1
    for i in range (1, a+1):
        result *= i
    return result
    
a = 14
print(factorial(a))
