from io import StringIO

class BitMap:
    
    def __init__(self, cols, rows):
        self.__cols = cols
        self.__rows = rows
    
        plain_length = cols*rows
        self.__bytes = bytearray([0]*(plain_length//8 if plain_length%8==0 else plain_length//8+1))
        
    def __str__(self):
        res = StringIO()
        for i in range(self.__cols):
            for j in range(self.__rows):
                res.write("1 " if self.getVal(i, j) else "0 ")
            res.write('\n')
            
        return res.getvalue()
        
    def __getPlainIdx(self, col_idx, row_idx):
        return self.__cols*row_idx+col_idx
    
    def getVal(self, col_idx, row_idx):
        plain_idx = self.__getPlainIdx(col_idx, row_idx)
        byte_idx = plain_idx // 8
        bit_idx = plain_idx % 8
        byte = self.__bytes[byte_idx]
        return (byte & (1 << bit_idx)) != 0
    
    def setVal(self, col_idx, row_idx, val: bool):
        plain_idx = self.__getPlainIdx(col_idx, row_idx)
        byte_idx = plain_idx // 8
        bit_idx = plain_idx % 8
        byte = self.__bytes[byte_idx]
        if (val):
            self.__bytes[byte_idx] = byte | (1 << bit_idx)
        else:
            self.__bytes[byte_idx] = (~(1 << bit_idx)) & byte
            
            
def testBit(int_type, offset):
    mask = 1 << offset
    return(int_type & mask)

