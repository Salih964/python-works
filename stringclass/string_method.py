# string sequence of characters

data ="this is a string"
data2="this is another string"
data3="""
    this
     is
      also
       a string
"""       
print(data3)

name="hello python"
print(name.capitalize())

name="hELLO PyThon"
print(name.casefold())


name="12"
print(name.isdigit())

name="salih"
print(name.isalpha())

name="salih123"
print(name.isalnum())

name="hellopython"
#     0123456
print(name.index("py"))

name="hello"
print(name.startswith("he"))

name="hellon"
print(name.endswith("on"))

name="hello,python,welcome"
#     0123456
words=name.split(",")
print(words)

name="hello,python,welcome"
print(name.count("o"))

name="$hello$"
print(name.strip("$")) 

# remove left strip
name="$hello$"
print(name.rstrip("$")) 

# remove right strip
name="$hello$"
print(name.lstrip("$")) 


