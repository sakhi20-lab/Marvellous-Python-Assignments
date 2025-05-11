#write a program which contains one function named as Add()which accepts two number from user and return addition of that two numbers

def Add(no1,no2):
    print("Inside the function")
    sum=no1+no2
    return sum

print("Enter First number:")
value1=int(input())

print("Enter second number:")
value2=int(input())

result=Add(value1,value2)
print("The addition of two numbers is:",result)

