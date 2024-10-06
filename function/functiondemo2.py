def add_num(n1,n2):
    result=n1+n2
    return result

def cube(n):
    result=n**3
    return result

print(add_num(100,200))

print(cube(3))



#create a function is even that take one parameter num and return True if num is even else return False
def is_even(n):
    return True if n%2==0 else False
print(is_even(20))

#create a function max_two that takes  two parameter n1,n2 and return largest number
# pep snake case

def max_two(n1,n2):
    return n1 if n1>n2 else n2
print(max_two(10,20))

# create afunction last_digit_max_num that takes two parameter n1,n2 return n1
# n1=257
# n2=480
# 257

def last_digit_max(n1,n2):
    n1_last_digit=n1%10
    n2_last_digit=n2%10

    return n1 if n1_last_digit>n2_last_digit else n2

print(last_digit_max(257,450))

# create a function nth_power takes two parameter number,exp return exponent of number


def nth_power(num,exp):
    return num**exp

print(nth_power(10,5))

# create a function max_two that takes two parameter n1,n2 and return largest number

# create a function smart_sub()

def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1

print(smart_sub(10,2))

# def_armstrong(num) return True if num is amstrong else return False
def is_armstrong(num):

    digit_count=len(str(num))
    original=num
    result=0
    while(num!=0):
        digit=num%10
        exp=digit**digit_count
        result=result+exp
        num =num //10
    return original==result
    
print(is_armstrong(151))    
    



