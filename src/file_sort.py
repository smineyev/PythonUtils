
INT_SIZE = 4

def writeInt(f, v):
    return f.write(int(v).to_bytes(INT_SIZE, 'big', signed=True))

def readInt(data):
    return int.from_bytes(data, 'big', signed=True)


class DataItem:
    
    def __init(self, key: int, val: bytes):
        self.__key = key
        self.__val = val
        
    def getKey(self):
        return self.__key
    
    def getVal(self):
        return self.__val
    
def readDataItem(self, f) -> DataItem:
    
    
    pass

def sortFile(filename: str):
    with open(filename, 'rb') as f:
        while True:
            data_item = readDataItem(f)
            if data_item :
                break;
            
            

