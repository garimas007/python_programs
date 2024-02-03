#search of product based on diff criteria
#product - Unique ID(key) and attributes(value)
#product_search - name, category and price_range

products = {
    1 : {'name':'eyecream',
         'category':'cosmetic',
         'price':600},
    2 : {'name':'diary',
         'category':'books',
         'price':1000},
    3 : {'name':'TV',
         'category':'electronics',
         'price':400}
}

def product_search(**kwargs):
    matching_product = []

    for p_id, attributes in products.items():
        if all(attributes.get(key) == value for key, value in kwargs.items()):
            matching_product.append((p_id, attributes))
    return matching_product

result = product_search(price=1000)
for p_id, attributes in result:
    print("product id:", p_id)
    print("name:", attributes['name'])
    print("category:", attributes['category'])
    print("price:", attributes['price'])
    print()