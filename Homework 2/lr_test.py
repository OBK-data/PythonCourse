import unittest
from lr import *
import numpy as np

class lregtest(unittest.TestCase):

    def test_wrongentry(self): #wrong variable name entry
        aa = np.array( [3, 4, 3.53 ,3])
        bb = np.random.rand(4,1)
        with self.assertRaises(NameError):
            lregress(ab, ba)

    def test_runerror(self): #ensures that code raises errors except with arrays
        with self.assertRaises(AttributeError):
            lregress(np.random.default_rng(10), np.random.default_rng(10))

    def test_inverror(self): #raised when a singular matrix is used
        ex = np.array([(1,2), (1,2)])
        with self.assertRaises(np.linalg.LinAlgError):
            lregress(np.random.rand(1,2), ex)

    def test_dmismatch(self):#checks dimension mismatch
        with self.assertRaises(ValueError):
            lregress(np.random.rand(1,10), np.random.rand(5,5))


if __name__ == '__main__':
    unittest.main()
