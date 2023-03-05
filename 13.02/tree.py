def tree(width):
    if width % 2 != 0:
        for i in range(1, width + 1):
            for j in range(width - i):
                print(" ", end="")
            for j in range(2 * i - 1):
                print("*", end="")
            print()
    else:
        print("Width must be odd:")
        
width = int(input("Enter the width: "))
tree(width)

# def pyfunc(r):
#     for x in range(r):
#         print(' '*(r-x-1)+'*'*(2*x+1))
# pyfunc(9)
