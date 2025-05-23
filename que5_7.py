def main():
    print("Enter the values")
    length = float(input( "Enter the length"))
    width  = float(input( "Enter the width"))

    area = length * width 
    perimeter =( length +  width) * 2

    print("Area of rectangle :",area)
    print("Perimeter of rectangle:",perimeter)


if __name__=="__main__":
    main()
