#write a program which accept number from user and check whether that number is positive or negative or zero.


def NUM():
    print("Enter a number:")
    no=int(input())

    if(no>0):
        print("The number is positive")

    elif(no<0):
        print("The number is negative")

    else:
        print("The number is zero")

if __name__=="__main__":
        NUM()