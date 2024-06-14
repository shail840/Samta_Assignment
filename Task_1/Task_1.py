def calculate_area(length, width):
    if length == width:
        return ("This is a square!")
    else:
        return length * width

def main():
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        result = calculate_area(length, width)
        print(result)
    except ValueError:
        print("Please enter valid numerical values for length and width.")


main()
