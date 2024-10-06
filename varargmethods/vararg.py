# def add_numbers(n1,n2):
#     return n1+n2

def add_numbers(*args):
    return sum(args)
    

print(add_numbers(10,20))
print(add_numbers( 10,20,30,40))

# args=>
# kwargs=>key word arguments

def display_student(**kwargs):
    print(kwargs.get("name"))

display_student(id="400",name="vijay",total="550",course="mca")   
# # #
def display_mobile_detail(**kwargs):
    print(kwargs.get("name"))

display_mobile_detail(name="redminote13pro",brand="redmi",price=23000)  

#  #  #
text="longest word"

words=text.split(" ")

def get_length(word):
    return len(word)

# longest_word=max(words,key=get_length)
# print(longest_word)

# shortest_word=min(words,key=get_length)
# print(shortest_word)


def get_min_max_word(text,is_max=True):
    words=text.split(" ")
    if is_max==True:
        longest_word=max(words,key=get_length)
        return longest_word
    else:
        shortest_word=min(words,key=get_length)
        return shortest_word
    
print(get_min_max_word(text))
print(get_min_max_word(text,is_max=False))

