import unittest
import os
from random import shuffle
from random import randint
from file_sort import INT_SIZE
from file_sort import readInt
from file_sort import writeInt

class FileSortTest (unittest.TestCase):
    test_filename = "/Users/smineyev/Downloads/index.dat"
    
    def setUp(self):
        global INT_SIZE
        
        keys=[i for i in range(1, 10)]
        shuffle(keys)
        vals=[None]*len(keys)
        for i in range(len(keys)):
            vals[i] = [keys[i]] * randint(1, 10)
        
        with open(self.test_filename, 'w+b') as f:
            for i in range(len(keys)):
                key = int(keys[i])
                val = vals[i]
                writeInt(f, key)
                writeInt(f, len(val)*INT_SIZE)
                for v in val:
                    writeInt(f, int(v))
                

    def testFile(self):
        global INT_SIZE
        
        print ("test array from file:")
        keys = list()
        vals = list()
        with open(self.test_filename, 'rb') as f:
            while True:
                bytes = f.read(INT_SIZE)
                if bytes:
                    key = readInt(bytes)
                    keys.append(key)
                    bytes = f.read(INT_SIZE)
                    if not bytes:
                        raise IOError("Unexpected EoF")
                    val_size = int(readInt(bytes) / INT_SIZE)
                    val = [None] * val_size
                    for i in range(val_size):
                        bytes = f.read(INT_SIZE)
                        if not bytes:
                            raise IOError("Unexpected EoF")
                        val[i] = readInt(bytes)
                        
                    vals.append(val)
                else:
                    break
                
                
        print ("size: %d"%len(keys))
        for i in range(len(keys)):
            print(keys[i], end=' :')
            for v in vals[i]:
                print(v, end=' ')
            print()
            
    def tearDown(self):
        str(os.remove(self.test_filename))

    def testFileSort(self):
        pass
