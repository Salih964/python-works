addition =lambda n1,n2: n1+n2

subtract=lambda n1,n2: n1-n2

cube=lambda n:n**3

maxtwo=lambda n1,n2: n1 if n1>n2 else n2

is_even= lambda n:True if n%2==0 else False
print(is_even(20))


# last_digit_max
last_digit_max=lambda n1,n2: n1 if n1%10>n2%10 else n2
print(last_digit_max(125,532))

# nth_power
nth_power=lambda num,exp:num**exp
print(nth_power(2,4))


# leap year
is_leap_year=lambda year:True if (year %100==0 and year %400==0)|(year%100!=0 and year %4==0) else False
print(is_leap_year(2025))

# smart_sub
smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
print(smart_sub(5,10))

# prime number
is_prime= lambda n:not any([n%i==0 for i in range (2,n)])
print(is_prime(12))


