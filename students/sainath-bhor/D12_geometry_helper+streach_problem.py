def rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

def circle(radius, pi=3.14159):
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

# Test the functions
print(rectangle(5, 3))
print(circle(7))

def box(length, width, height):
    volume = length * width * height
    surface_area = 2 * (length * width + length * height + width * height)
    return volume, surface_area
