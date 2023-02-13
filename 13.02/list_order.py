def lst_order(arr):
    sorted_arr = arr[:]
    sorted_arr.sort()
    if arr == sorted_arr:
        return "Ascending"
    if sorted_arr == arr[::-1]:
        return "Descending"
    else:
        return "Neither"
        
arr = [1,5,2,3,7]
print(lst_order(arr))