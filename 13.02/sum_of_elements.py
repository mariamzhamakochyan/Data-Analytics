def sum(A, IND):
    sum = 0 
    if len(A) > max(IND):
        for i in A:
            for j in IND:
                if i > 0 and j >= 0:
                    sum += A[j]
            return sum
    else:
        return "Len A must be greater than the maximum IND argument. "
A = [1,2,3,4,5]
IND = [0,3,3,2]
print(sum(A, IND))

