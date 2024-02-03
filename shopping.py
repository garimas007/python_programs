#add_to_cart - item, quantity
#return item and quantity

def add_to_cart(item, quantity):
    """
    this is an example to show positional args and keyword args
    """
    print(f"items - {item} and no. of item - {quantity}")

add_to_cart("apple", 5)                     
add_to_cart(item="banana", quantity=12)