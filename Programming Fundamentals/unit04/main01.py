# use the math.sqrt() function to compute the final result.
import math

# Mani function that accepts two arguments, returns a placeholder value.
def hypotenuse(a, b):
    #  add logic to square both legs of the triangle
    a_squared = a ** 2
    b_squared = b ** 2
    # add the step to compute the sum of the squared legs 
    sum_squares = a_squared + b_squared
    result = math.sqrt(sum_squares)
    return result

print(hypotenuse(5,6))