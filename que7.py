#write a program which contains one function that accept one number from user and returns true if number is divisible by  otherwise return false.


def Divisible():
    print("Enter number:")
    no=int(input())

    if(no%5==0):
        print("True")
    else:
        print("False")

if __name__=="__main__":
    Divisible()