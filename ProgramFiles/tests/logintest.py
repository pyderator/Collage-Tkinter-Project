# Importing Modules to import files from another directory
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

# Importing Login file to test it
from files import login
import unittest
from tkinter import *
class LoginTest(unittest.TestCase):
    def test_login(self):
        root = Tk()
        test = login.LoginPage(root)
        root.mainloop()
        print(test.username,test.password)
        self.assertEqual(type(test.username),'as')


# LoginTest().login_test()
# LoginTest().login_test()
unittest.main()
