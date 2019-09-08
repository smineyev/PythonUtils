from BitMap import BitMap
import unittest 

class BitMapTest (unittest.TestCase):
        
    def testEmptyness(self):
        bm = BitMap(5, 3)
        self.assertFalse(bm.getVal(1, 2))
        self.assertFalse(bm.getVal(1, 2))

    def testGetSetVal(self):
        bm = BitMap(5, 3)
        
        bm.setVal(1, 2, True)        
        self.assertTrue(bm.getVal(1, 2))
        bm.setVal(1, 2, False)
        self.assertFalse(bm.getVal(1, 2))
        
if __name__ == '__main__':
    unittest.main()