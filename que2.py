#write a program which contains one function named as Cheksum which accept one paramter as a number. If number is even then it should display
#"Even Number" otherwise display "Odd Number"on console.

def ChkNum():
    print("Enter the number")
    no=int(input())
  
    if(no%2==0):
        print("The number is even")
  
    else:
        print("The number is odd")

if __name__=="__main__":
    ChkNum()
