# global variable- we have to declare the variables out side of the function

a = 10 
b = 20  
result = a + b
result = a - b
def add():
    print(a+b)
    print(result)
def sub():
    print(b-a)
    print(a-b)
    print(result)
def mul():
    print(a*b)
    print(a*a)
    print(b*b)
def div():
    print(a/b)
    print(b/a)
add()
sub()
mul()
div()