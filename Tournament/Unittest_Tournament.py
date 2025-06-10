import unittest
import Tournament

class TestTournament(unittest.TestCase):
    def test_isPowerOfTwo(self):
        self.assertTrue(isPowerOfTwo(2))
        self.assertTrue(isPowerOfTwo(4))
        self.assertTrue(isPowerOfTwo(5))
        self.assertTrue(isPowerOfTwo(-6))
        self.assertTrue(isPowerOfTwo(0))
        self.assertTrue(isPowerOfTwo(12))
        self.assertTrue(isPowerOfTwo(-2))

   def test_IsLengthEight(self):
       self.assertTrue(IsLengthEight(8))
       self.assertTrue(IsLengthEight(0))
       self.assertTrue(IsLengthEight(-5))
       self.assertTrue(IsLengthEight(25))

    def test_chefmatch(self):
        self.assertEqual(chefmatch('A', 'B'),['A','B'])