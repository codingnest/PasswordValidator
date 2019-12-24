import argparse, logging, re, textwrap, sys

class PasswordValidator:

    def __init__(self, password):
        self.password = password

    def check_length(self):
        '''
        Method checks for required password length
        return: None
        '''
        if len(self.password) < 8:
            logging.error("Password {} length is less than at-least 8 characters".format(self.password))
            return False
        else:
            return True

    def check_uppercase(self):
        '''
        Method checks for at-least one uppercase character
        return: None
        '''
        match = re.search('[A-Z]+', self.password)
        if not match:
            logging.error("Password {} should contain at-least one uppercase character".format(self.password))
            return False
        else:
            return True

    def check_alphanumeric(self):
        '''
        Method checks for at-least one alphanumeric character
        return: None
        '''
        match = re.search('\w+', self.password)
        if not match:
            logging.error("Password {} should contain at-least one alphanumeric character".format(self.password))
            return False
        else:
            return True

    def check_special_character(self):
        '''
        Method checks for at-least one special characters from ~!@#$%^&*
        return: None
        '''
        match = re.search('[~!@#$%^&*]+', self.password)
        if not match:
            logging.error("Password {} should contain at-least one special characters ~!@#$%^&*".format(self.password))
            return False
        else:
            return True

    def check_whitespace_character(self):
        '''
        Method checks for any whitespace character present in Password
        return: None
        '''
        match = re.search('\s+', self.password)
        if match:
            logging.error("Password {} shouldn't contain any whitespace character".format(self.password))
            return False
        else:
            return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog = 'validator',
        formatter_class = argparse.RawDescriptionHelpFormatter,
        description = textwrap.dedent('''\
        Password Validator Tool
        Following Rules to be followed:
        1. Length of password should be of at-least 8 characters
        2. At-least one uppercase character
        3. At-least one alpha-numeric character
        4. No whitespace character is allowed
        '''))

    requiredNamed = parser.add_argument_group('Required Named Argument.')
    requiredNamed.add_argument('-p', '--p', dest = 'password',
                               help = 'Please enter the Password', required = True)
    args = parser.parse_args()

    #Logger
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt = '%d-%b-%y %H:%M:%S')
    fileHandler = logging.FileHandler(filename = 'app.log') #Relative Path
    fileHandler.setFormatter(formatter)
    logger.setLevel(level = logging.INFO) #Logging Level

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)

    logging.info("Password entered by User: {}".format(args.password))

    logger.debug("Creating Password Validator Object")
    pObj = PasswordValidator(args.password)

    logger.debug("Checking for whitespace character")
    if not pObj.check_whitespace_character():
        sys.exit(1)

    logger.debug("Checking for Password Length")
    if not pObj.check_length():
        sys.exit(1)

    logger.debug("Checking for uppercase character")
    if not pObj.check_uppercase():
        sys.exit(1)

    logger.debug("Checking for alpha-numeric character")
    if not pObj.check_alphanumeric():
        sys.exit(1)

    logger.debug("Checking for Special character")
    if not pObj.check_special_character():
        sys.exit(1)

    logger.info("Valid Password, All checks done!!")