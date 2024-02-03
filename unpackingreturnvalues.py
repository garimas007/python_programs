"""
unpacking returned values into seperate variables using assignment
"""

def calculate_powers(number):
    square = number ** 2
    cube = number ** 3

    return square, cube

n_square, n_cube = calculate_powers(5)
print(f"the square is : {n_square}")
print(f"the cube is : {n_cube}")