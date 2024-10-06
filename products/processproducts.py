from json import load

f=open("C:\\Users\\2\\OneDrive\\Desktop\\mypython works\\products\\data.json","r",encoding="UTF-8")

data=load(f)

print(len(data))

product_names=[p.get("title") for p in data]
# print(product_names)

all_categories=[p.get("category") for p in data]
print(set(all_categories))

# print all product name available under rs 50
price_filter=[p.get("title") for p in data if p.get("price")<=50]
# print(price_filter)

# print all jewellery product names
category_filter=[ p.get("title") for p in data if p.get("category")=="jewelery"]
# print(category_filter)

# costly product
def get_price(dictionary):
    return dictionary.get("price")

costly_product=max(data,key=get_price)
# print(costly_product.get("title"),costly_product.get("price"))

# cheapest product
cheapest_product=min(data,key=get_price)
# print(cheapest_product.get("title"),cheapest_product.get("price"))

# product title,rating count
review_count=[(p.get("title"),p.get("rating").get("count")) for p in data]
# print(review_count)

def get_rating_count(dictionary):
    return dictionary.get("rating").get("count")

top_review_product=max(data,key=get_rating_count)
print(top_review_product.get("title"))
