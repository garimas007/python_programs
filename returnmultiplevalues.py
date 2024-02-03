"""
Returns multiple values (as a tuple)
Unpacked as seperate variables
"""
def calculate_rectangle(lenght, width):
    area = lenght * width
    perimeter = 2*(lenght+width)

    return area, perimeter

r_area, r_perimeter = calculate_rectangle(4,5)
print(f"area is : {r_area}")
print(f"perimetr is : {r_perimeter}")