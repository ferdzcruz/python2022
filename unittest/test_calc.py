import unittest
import math_operation as calc
from vars import *


class testCalc(unittest.TestCase):

    def test_add(self):
        #results = calc.add(10,5) this can work like this or 
        self.assertEqual(calc.add(10,5), 15)# like this
        self.assertEqual(calc.add(num_x,num_y), 25) 
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
    
    def test_divide(self):
        self.assertEqual(calc.divide(5,1),5)
        self.assertRaises(ValueError, calc.divide, 10,0) # this has been raised in math_operation.py

        with self.assertRaises(ValueError):
            calc.divide(10,0)




if __name__ == '__main__':
    unittest.main()


"""notes
1. import unittest - this is builtin modules.
2. import math_operation as calc module where your computation
3. function should start with test always. Otherwise it will result to 0 ex : test_add.
4. if __name__ == '__main__': use this so you can test inside your module file.
3. If not, you test your code like this : python -m unittest test_calc.py
4. https://www.youtube.com/watch?v=6tNS--WetLI

"""