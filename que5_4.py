def main():
    print("Enter three numbers")
    
    a = int(input( "enter first number"))
    b = int(input( "enter second number"))
    c = int(input( "enter third  number"))

    if(a>=b):
        if(a>=c):
            return a
        else:
            return c
    else:
        if (b>=c):
            return b
        else:
            return c
         

largestnum = main()
print("largest number is:",largestnum)


if __name__=="__main__":
    main()
