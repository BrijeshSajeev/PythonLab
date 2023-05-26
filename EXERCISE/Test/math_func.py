# import time

# for i in range(1, 13):
#     for j in range(0, 61):
#         for k in range(0, 61):
#             print(str(i) + ":" + str(j) + ":" + str(k))
#             time.sleep(0.12)
import math


def math_functions_example():
    x = -4.3
    y = 2
    numbers = [1, 5, 9, 2, 7]

    # Absolute value
    abs_x = abs(x)
    print(f"Absolute value of {x}: {abs_x}")

    # Exponentiation
    pow_result = pow(x, y)
    print(f"{x} raised to the power of {y}: {pow_result}")

    # Rounding
    rounded_x = round(x)
    print(f"Rounded value of {x}: {rounded_x}")

    # Maximum and minimum
    max_value = max(numbers)
    min_value = min(numbers)
    print(f"Maximum value in the list: {max_value}")
    print(f"Minimum value in the list: {min_value}")

    # Sum
    sum_result = sum(numbers)
    print(f"Sum of the list: {sum_result}")

    # Square root
    sqrt_result = math.sqrt(y)
    print(f"Square root of {y}: {sqrt_result}")

    # Floor and ceil
    floor_x = math.floor(x)
    ceil_x = math.ceil(x)
    print(f"Floor value of {x}: {floor_x}")
    print(f"Ceil value of {x}: {ceil_x}")

    # Trigonometric functions
    angle = math.pi / 4  # 45 degrees in radians
    sin_result = math.sin(angle)
    cos_result = math.cos(angle)
    tan_result = math.tan(angle)
    print(f"Sine of {angle} radians: {sin_result}")
    print(f"Cosine of {angle} radians: {cos_result}")
    print(f"Tangent of {angle} radians: {tan_result}")


# Call the function to run the program
math_functions_example()
