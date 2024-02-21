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

    def test_lowercase(self):
        input = "ASDSG123!@$"
        self.assertFalse(check_pwd(input))

    def test_uppercase(self):
        input = "asdfg!@#32132"
        self.assertFalse(check_pwd(input))

    def test_20_plus(self):
        input = "123456789012345678902"
        self.assertFalse(check_pwd(input))

    def test_20(self):
        input = "123456!@asDfa!@lkjgs"
        self.assertTrue(check_pwd(input))

    def test_8(self):
        input = "asd12!@A"
        self.assertTrue(check_pwd(input))

    def test_8_orless(self):
        input = "1!aB"
        self.assertFalse(check_pwd(input))

    def test_correct_password(self):
        input = "as!@DF12a"
        self.assertTrue(check_pwd(input))

    def test_alldigit(self):
        input = "1234567890"
        self.assertFalse(check_pwd(input))

    def test_alllower(self):
        input = "asdfghjkl"
        self.assertFalse(check_pwd(input))

    def test_allupper(self):
        input = "ASDFGHJKLASDFGHJKLASDFGGHSADKJ"
        self.assertFalse(check_pwd(input))

    def test_allsymbols(self):
        input = "!@#$%^&*()!@"
        self.assertFalse(check_pwd(input))

    def test_over20_all(self):
        input = "123asdASDgjhka!@#asdg+"
        self.assertFalse(check_pwd(input))


if __name__ == '__main__':
    unittest.main()