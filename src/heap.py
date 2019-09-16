from io import StringIO

class Heap:
    
    def __init__(self, data=[]):
        self.__data = data
        self.data = data
    
    def __str__(self):
        res = StringIO()
        level=1
        for i, v in enumerate(self.__data):
            if (i == 2**(level)-1):
                # new level
                level += 1
                res.write('\n')
            res.write(str(v) + ' ')
                
        return res.getvalue()

    def add(self, val):
        self.__data.append(val)
        added_idx = len(self.__data)-1
        self._popUp(added_idx, val)

    def _popUp(self, added_idx, added_val):
        parent_idx = self._getParentIdx(added_idx)
        parent_val = self.__data[parent_idx]
        if (parent_val < added_val):
            self._swap(parent_idx, added_idx)
            self._popUp(parent_idx, parent_val)
        
        
    def _swap(self, i, j):
        tmp = self.__data[i]
        self.__data[i] = self.__data[j]
        self.__data[j] = tmp
    
    def _getParentIdx(self, idx) -> int:
        return (idx-1)//2
    
    def _getChilderenIdxs(self, idx):
        return (2*idx+1, 2*idx+2)
        
    def pop(self):
        size = len(self.__data)
        if (size == 0):
            return None
        res = self.__data[0]
        self.__data[0] = self.__data.pop()
        self.__sinkDown(0)
        return res
    
    def __sinkDown(self, idx):
        max_idx = -1
        elem_at_right_place = True
        for i in self._getChilderenIdxs(idx):
            if (i > len(self.__data)-1):
                break;
            
            if self.__data[i] > self.__data[idx]:
                elem_at_right_place = False
                
            if max_idx == -1 or self.__data[max_idx] < self.__data[i]:
                max_idx = i
                
        if elem_at_right_place:
            return
                
        if max_idx == -1:
            #end of heap
            return
        
        self._swap(max_idx, idx)
        self.__sinkDown(max_idx) 
        
    
heap = Heap( [100, 19, 36, 17, 3, 25, 1, 2, 7])
print (heap)
print()
for i, elem in enumerate(heap.data):
    print ("%s -> %s"%(elem, heap.data[heap._getParentIdx(i)]))
    
heap.add(8)

print (heap)
heap.add(4)
print (heap)
print (heap.pop())
print (heap)

        
    
    