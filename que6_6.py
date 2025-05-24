def triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

triangle(5)
if __name__=="__main__":
    triangle()