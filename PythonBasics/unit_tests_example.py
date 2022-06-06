import unittest
import python_unittest_cap


class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = python_unittest_cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_word(self):
        text = 'monty python'
        result = python_unittest_cap.cap_text(text)
        self.assertEqual(result, 'Monty python')

if __name__=="__main__":
    unittest.main()
