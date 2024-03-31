# global variable- we have to declare the variables out side of the function
num1 = 10 
num2 = 20  
num3 = 30
num4 = 40
num5 = 50
def add():
    result = num1 + num2
    print(result)
def sub():
    result= num2 - num1
    result1 = num3 - num2
    result2 = num4 - num3
    result3 = num5 - num4
    print(result)
    print(result1)
    print(result2)
    print(result3)
def mul():
    result= num2 * num1
    result1 = num3 * num2
    result2 = num4 * num3
    result3 = num5 * num4
    print(result)
    print(result1)
    print(result2)
    print(result3)
def div():
    result= num2 / num1
    result1 = num3 / num2
    result2 = num4 / num3
    result3 = num5 / num4
    print(result)
    print(result1)
    print(result2)
    print(result3)
add()
sub()
mul()
div()