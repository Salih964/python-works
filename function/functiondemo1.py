# function without return value

def add(n1,n2):
    result=n1+n2
    print(result)

def sub(n1,n2):
    result=n1-n2
    print(result)



def cube(n1):
    result=n1**3
    print(result)

cube(3)

add(100,200)

# function with return value

def max_two(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
    
out=max_two(100,200)
print(out)
