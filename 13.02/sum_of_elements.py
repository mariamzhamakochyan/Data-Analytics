def sum(A, IND):
    sum = 0 
    N = len(A)
    M = len(IND)
    if 0 < M < N:
        for i in IND:
            sum += A[i]
        return sum
    else:
        return "len IND must be less than len A: "
A = [1,2,3,4,5]
IND = [0,3,3,2]
print(sum(A, IND))

