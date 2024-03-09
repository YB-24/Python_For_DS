import unittest
import Capital
import Title

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text= 'python' 
        result = Capital.capital(text)
        self.assertEqual(result,'Python')

    def test_multiple_word(self):
        text= 'harry python' 
        result = Title.title(text)     #if Capital.capital(text) was used then it will fail the test case
        self.assertEqual(result,'Harry Python')

if __name__ == '__main__':
    unittest.main()