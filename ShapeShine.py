def area_rectangle(length, breadth):
    return length * breadth

def area_circle(radius):
    import math
    return math.pi * (radius ** 2)

def area_triangle(base, height):
    return 0.5 * base * height

def main():
    print("Select the shape to find the area:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    
    choice = input("Enter the number of the shape (1/2/3): ")
    
    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        print(f"The area of the rectangle is: {area_rectangle(length, breadth)}")
    
    elif choice == '2':
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {area_circle(radius)}")
    
    elif choice == '3':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {area_triangle(base, height)}")
    
    else:
        print("Invalid choice. Please select a number between 1 and 3.")

if __name__ == "__main__":
    main()
