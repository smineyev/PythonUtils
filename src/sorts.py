
def mergeSort(array):
    if len(array) == 1:
        return array
    
    mid_idx = len(array) // 2
    left_array = mergeSort(array[:mid_idx]) 
    right_array = mergeSort(array[mid_idx:])
    
    l_idx = 0
    r_idx = 0
    idx = 0
    for idx in range(len(array)):
        if (r_idx >= len(right_array) or l_idx < len(left_array) 
            and left_array[l_idx] < right_array[r_idx]):
                array[idx] = left_array[l_idx]
                l_idx += 1 
        else:
                array[idx] = right_array[r_idx]
                r_idx += 1
        idx += 1
        
    return array


def __swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def __partition(array, start_idx: int, end_idx: int):
    print ("start with:        "+str(array[start_idx : end_idx+1]))
    pivot = array[end_idx]
        
    i = start_idx
    for j in range(start_idx, end_idx):
        if array[j] <= pivot:
            __swap(array, i, j)
            i += 1
            
    __swap(array, i, end_idx)

    print("pivot=%d, i=%d, j=%d"%(pivot, i, i), end=': ')
    print (str(array[start_idx : end_idx+1]))        
    return i,i
        

def __quickSort(array, start_idx: int, end_idx: int):
    if end_idx <= start_idx:
        return
    
    i, j = __partition(array, start_idx, end_idx)
    __quickSort(array, start_idx, i-1)
    __quickSort(array, j+1, end_idx)
    
def quickSort(array):
    __quickSort(array, 0, len(array)-1)    
    
            
            
    
array=[4, 2, 7, 9, 3, 2, 1, 8, 5, 1, 5]

print ("Original: "+str(array))
quickSort(array)
print ("Result: "+str(array))
        