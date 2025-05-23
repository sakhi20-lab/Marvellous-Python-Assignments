def main():
    print("Enter the temperature in Celsius")
    C= float(input()) #temperature in celsius

    F = ( C * 9/5) + 32
     
    print(" Temperature in Fahrenheit:",F)

if __name__=="__main__":
    main()