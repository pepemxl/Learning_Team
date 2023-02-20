import unittest
import math



class test_class(unittest.TestCase):
    def setUp(self):        
        self.num_a = 9
        self.num_b = 16
        self.num_c = 25
    
    def test_sqrt(self):
        self.assertEqual(math.sqrt(self.num_a), 3)

    def test_sqrt16(self):
        self.assertEqual(math.sqrt(self.num_b), 4)

    def test_sqrt25(self):
        self.assertEqual(math.sqrt(self.num_c), 5)

if __name__ == '__main__':
    unittest.main()