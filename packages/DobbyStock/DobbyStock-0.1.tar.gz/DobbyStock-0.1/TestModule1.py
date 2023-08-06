import unittest
from mod1 import addition as md1


class TestAdd(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(md1(1,2),3)
        self.assertEqual(md1(1,5),6)
     
unittest.main()