def hello_world():
    print("Hello World!")
    
hello_world()

def sum(num1,num2):
    print(num1+num2)
sum(2,3)

def multiply(num3,num5):
    return num3 * num5

total=multiply(6,5)
print(total)

def sum(num1=0, num2=0):
    if(type(num1)is not int or type(num2)is not int):
        return 0
    return num1+num2

total = sum("ty",9)
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("cats","dogs","fish","rats")    

def numerous_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

numerous_items(first="Cats",Second="Dogs")