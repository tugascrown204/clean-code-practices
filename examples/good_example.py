# Good Example of Clean Code

def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    """
    import math
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    radius = 5
    area = calculate_area(radius)
    print(f'Area of circle with radius {radius} is: {area}')