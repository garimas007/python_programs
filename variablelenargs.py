#calculate_average - using *args
#o/p - avg of provided numbers

def calculate_average(*args):
    """
    An example of variable length arguments
    """
    total = sum(args)
    average = total / len(args)
    return average

print(calculate_average(2,4,6))
print(calculate_average(1,2,3,4,5))
