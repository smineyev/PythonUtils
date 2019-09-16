
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
    
def __pushTailUp(a, end_idx):
    if end_idx == 0:
        #at the root
        return
    v = a[end_idx]
    parent_idx = (end_idx-1)//2
    parent_val = a[parent_idx]
    if parent_val<v:
        a[end_idx] = a[parent_idx]
        a[parent_idx] = v
        __pushTailUp(a, parent_idx)
        

def __sinkHeadDown(a, node_idx, end_idx):
    min_idx = -1
    left_child_idx = 2*node_idx+1
    if left_child_idx > end_idx:
        return
    right_child_idx = 2*node_idx+2
    if right_child_idx > end_idx:
        if a[left_child_idx] > a[node_idx]:
            min_idx = left_child_idx
    else:
        if a[left_child_idx] > a[right_child_idx]:
            if a[left_child_idx] > a[node_idx]:
                min_idx = left_child_idx
        else:
            if a[right_child_idx] > a[node_idx]:
                min_idx = right_child_idx
                
    if not min_idx == -1:
        __swap(array, min_idx, node_idx)
        __sinkHeadDown(a, min_idx, end_idx)
    


def heapSort(a):
    #build heap
    for i in range(1, len(a)):
        __pushTailUp(a, i)
    print(a)
    for i in range(len(a)-1, 0, -1):
        __swap(a, 0, i)
        print(a)
        __sinkHeadDown(a, 0, i-1)
        print(a)
    #peak from heap
    
            
            
    
array=[4, 2, 7, 9, 3, 2, 0, 8, 5, 1]
# array=[4, 2, 7, 9]

print ("Original: "+str(array))
heapSort(array)
print ("Result: "+str(array))

# for i, elem in enumerate(array):
#     print ("%s -> %s"%(elem, array[(i-1)//2]))

