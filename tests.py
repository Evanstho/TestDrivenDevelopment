import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    
    def test_empty_string(self):
        input = ""
        self.assertFalse(check_pwd(input))

    def test_nodigits(self):
        input = "asdASDads!"
        self.assertFalse(check_pwd(input))

    def test_symbol(self):
        input = "aaDDFG13f"
        self.assertFalse(check_pwd(input))


if __name__ == '__main__':
    unittest.main()