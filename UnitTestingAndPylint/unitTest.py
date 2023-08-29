import unittest
import cap


class TextCap(unittest.TestCase):

    def test_one_word(self):
        test = 'python'
        result = cap.cap_test(test)
        self.assertEqual(result, 'Python')
    
    def test_multiple_word(self):
        test = 'shubham python'
        result = cap.cap_test(test)
        self.assertEqual(result, 'Shubham Python')
        
if __name__ == '__main__':
    unittest.main()