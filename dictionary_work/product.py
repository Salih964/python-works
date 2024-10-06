
# product
product={"code":1000,"name":"scooby","category":"bag","price":250,}
print(product["name"])

# color:blue
product["color"]="blue"
print(product)

# update product price as 300
product["price"]=300
print(product)

# chk offer key is present or not
print("offer" in product)

# add offer as 300 if offer key is not present else update offer as 250

if "offer" in product:
    product["offer"]=250
else :
    product["offer"]=300

print(product) 

