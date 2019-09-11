
INT_SIZE = 4

def writeInt(f, v):
    return f.write(int(v).to_bytes(INT_SIZE, 'big', signed=True))

def readInt(data):
    return int.from_bytes(data, 'big', signed=True)


class DataItem:
    
    def __init__(self, key: int, val: bytes):
        self.__key = key
        self.__val = val
        
    def getKey(self):
        return self.__key
    
    def getVal(self):
        return self.__val
    
    def __str__(self):
        return "{0}: {1}".format(self.__key, self.__val)
    
def writeDataItem(f, data_item: DataItem):
    writeInt(f, data_item.getKey())
    writeInt(f, len(data_item.getVal()))
    f.write(data_item.getVal())
    
    
def readDataItem(f) -> DataItem:
    raw_bytes = f.read(INT_SIZE)
    if raw_bytes:
        key = readInt(raw_bytes)
        raw_bytes = f.read(INT_SIZE)
        if not raw_bytes:
            raise IOError("Unexpected EoF")
        val_size = readInt(raw_bytes)
        raw_bytes = f.read(val_size)
        if not raw_bytes:
            raise IOError("Unexpected EoF")
        val = raw_bytes
        return DataItem(key, val)
    else:
        return None

def sortFile(filename: str):
    with open(filename, 'rb') as f:
        while True:
            data_item = readDataItem(f)
            if data_item :
                print(data_item)
            else:
                break;
            
            

