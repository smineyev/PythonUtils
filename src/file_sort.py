import os

INT_SIZE = 4
MAX_TMP_FILES=5

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
    

def sortFile(filename: str, data_item_compare_func) -> str:
    global MAX_TMP_FILES
    res_filename = None
    tmp_filenames = []
    data_item_1 = None
    with open(filename, 'rb') as f:
        while True:
            if not data_item_1:
                data_item_1 = readDataItem(f)
            if not data_item_1 :
                if len(tmp_filenames) == 1:
                    res_filename = "{0}.res".format(filename)
                    os.rename(tmp_filenames[0], res_filename)
                    break
                else:
                    raise RuntimeError("there should be only one tmp file left after we finish. Instead there are "+str(len(tmp_filenames)))
            
            while len(tmp_filenames) < MAX_TMP_FILES:
                if not data_item_1 :
                    break;
                tmp_filename = "{0}.{1}.tmp".format(filename, len(tmp_filenames))
                tmp_filenames.append(tmp_filename)
                with open(tmp_filename, "wb+") as tmp_f:
                    writeDataItem(tmp_f, data_item_1)
                    while True:
                        data_item_2 = readDataItem(f)
                        if not data_item_2 :
                            break;
                        if data_item_compare_func(data_item_1, data_item_2) > 0:
                            break
                        writeDataItem(tmp_f, data_item_2)
                        data_item_1 = data_item_2
                data_item_1 = data_item_2
            
            res_filename = "{0}.res".format(filename)  
            with open(res_filename, "wb+") as res_file:
                tmp_files = [None] * len(tmp_filenames)
                curr_datas = [None] * len(tmp_filenames)
                try:
                    for i, tmp_filename in enumerate(tmp_filenames):
                        tmp_files[i] = open(tmp_filename, "rb")
                        curr_datas[i] = readDataItem(tmp_files[i])
                        
                    while True:
                        min_idx = -1
                        for i, data_item in enumerate(curr_datas):
                            if not data_item:
                                continue
                            if min_idx == -1 or data_item_compare_func(curr_datas[min_idx], data_item) > 0:
                                min_idx = i
                            
                        if min_idx == -1: # we processed all tmp file, exit
                            break                     
                            
                        writeDataItem(res_file, curr_datas[min_idx])
                        curr_datas[min_idx] = readDataItem(tmp_files[min_idx])
                    
                finally:
                    for tmp_file in tmp_files:
                        if tmp_file:
                            tmp_file.close()
            tmp_filenames.clear()
            tmp_filename0 = "{0}.{1}.tmp".format(filename, 0)
            tmp_filenames.append(tmp_filename0)
            os.rename(res_filename, tmp_filename0)
    return res_filename       
            
            

