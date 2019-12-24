Problem Statement:-

Write a Python Program to generate a logic for Password Validator.

1. Using Classes and Objects
2. Log all the Events
3. Write Positive and Negative Unit TestCases.

Steps:-
1. We have to take the input from user using ArgParse Module
2. Create Logging Configuration object for saving the Events.
3. Create PasswordValidator Class
4. Define all the methods - check_length(), check_uppercase(), check_alphanumeric(), check_special_character, check_whitespace_character()
5. Call all the methods for checking for Valid Password String.
6. Write all the Positive and Negative Test Cases for each of the methods defined.

Help File:-
(base) C:\Users\admin\PycharmProjects\PasswordValidator>python validator.py -h
usage: validator [-h] -p PASSWORD

Password Validator Tool
Following Rules to be followed:
1. Length of password should be of at-least 8 characters
2. At-least one uppercase character
3. At-least one alpha-numeric character
4. No whitespace character is allowed

optional arguments:
  -h, --help            show this help message and exit

Required Named Argument.:
  -p PASSWORD, --p PASSWORD
                        Please enter the Password

Execution:-
(base) C:\Users\admin\PycharmProjects\PasswordValidator>python validator.py -p Wel@1234
24-Dec-19 22:21:35 - Password entered by User: Wel@1234
24-Dec-19 22:21:35 - Valid Password, All checks done!!

Test Case Execution:-
(base) C:\Users\admin\PycharmProjects\PasswordValidator>python -m unittest test_validator.py -v
test_atleast_one_alphanumeric_character (test_validator.PasswordValidatorTest) ... ok
test_atleast_one_special_character (test_validator.PasswordValidatorTest) ... ok
test_atleast_one_uppercase_character (test_validator.PasswordValidatorTest) ... ok
test_atleast_one_whitespace_character (test_validator.PasswordValidatorTest) ... ERROR:root:Password wel 12345 shouldn't contain
any whitespace character
ok
test_invalid_password_length (test_validator.PasswordValidatorTest) ... ERROR:root:Password abcd12 length is less than at-least 8
 characters
ok
test_no_alphanumeric_character (test_validator.PasswordValidatorTest) ... ERROR:root:Password !@#$%^ should contain at-least one
alphanumeric character
ok
test_no_special_character (test_validator.PasswordValidatorTest) ... ERROR:root:Password wel12345 should contain at-least one spe
cial characters ~!@#$%^&*
ok
test_no_uppercase_character (test_validator.PasswordValidatorTest) ... ERROR:root:Password wel@1234 should contain at-least one u
ppercase character
ok
test_no_whitespace_character (test_validator.PasswordValidatorTest) ... ok
test_valid_password_length (test_validator.PasswordValidatorTest) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.014s

OK
