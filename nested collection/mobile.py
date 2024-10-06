
products=[
    {"code":100,"name":"redminote13","brand":"redmi","price":30000,"network":"5g"},
    {"code":101,"name":"iphone15","brand":"apple","price":130000,"network":"5g"},
    {"code":102,"name":"samsunga18","brand":"samsung","price":20000,"network":"4g"},
    {"code":103,"name":"redminote12","brand":"redmi","price":30000,"network":"4g"},
    {"code":104,"name":"s23ultra","brand":"samsung","price":150000,"network":"5g"},
    {"code":105,"name":"motoedge","brand":"motorola","price":24000,"network":"5g"},
    {"code":106,"name":"oneplus9r","brand":"oneplus","price":30000,"network":"5g"},

]


#q1 total number of products
print(len(products))

#q2 apple product prices
# for dictionary in products:
#    if dictionary.get("brand")=="apple":
#       print(dictionary.get("price"))

              # or
apple_prices=[p.get("price")for p in products if p.get("brand")=="apple"]      
print(apple_prices)

# q3 mobile avialiable u der 20k-25k
price_filter=[p.get("name") for p in products if p.get ("price") in range(20000,25001)]
print(price_filter)

#q4 costly brand
def get_price(dictionary):
   return dictionary.get("price")

costly_product=max(products,key=get_price)
print(costly_product.get("brand"))

cheapest_product=min(products,key=get_price)
print(cheapest_product)

# q5 print all 5g network phones
fiveg_phones=[p.get("name") for p in products if p.get("network")=="5g"]
print(fiveg_phones)

# q6 brand:3,redmi:3
all_brands=[p.get("brand") for p in products]

wc={b:all_brands.count(b) for b in set (all_brands)}
print(wc)