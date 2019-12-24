import unittest
from validator import PasswordValidator

class PasswordValidatorTest(unittest.TestCase):
    def test_valid_password_length(self):
        passObj = PasswordValidator("Wel@1234")
        self.assertTrue(passObj.check_length())

    def test_invalid_password_length(self):
        passObj = PasswordValidator("abcd12")
        self.assertFalse(passObj.check_length())

    def test_atleast_one_uppercase_character(self):
        passObj = PasswordValidator("Wel@1234")
        self.assertTrue(passObj.check_uppercase())

    def test_no_uppercase_character(self):
        passObj = PasswordValidator("wel@1234")
        self.assertFalse(passObj.check_uppercase())

    def test_atleast_one_alphanumeric_character(self):
        passObj = PasswordValidator("Wel@1234")
        self.assertTrue(passObj.check_alphanumeric())

    def test_no_alphanumeric_character(self):
        passObj = PasswordValidator("!@#$%^")
        self.assertFalse(passObj.check_alphanumeric())

    def test_atleast_one_special_character(self):
        passObj = PasswordValidator("Wel@1234")
        self.assertTrue(passObj.check_special_character())

    def test_no_special_character(self):
        passObj = PasswordValidator("wel12345")
        self.assertFalse(passObj.check_special_character())

    def test_no_whitespace_character(self):
        passObj = PasswordValidator("Wel@1234")
        self.assertTrue(passObj.check_whitespace_character())

    def test_atleast_one_whitespace_character(self):
        passObj = PasswordValidator("wel 12345")
        self.assertFalse(passObj.check_whitespace_character())

if __name__ == '__main__':
    unittest.main()