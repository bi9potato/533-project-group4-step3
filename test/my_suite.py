import unittest
from TestAdmin import TestAdmin
from TestJobseeker import TestJobseeker
from TestCompany import TestCompany
from TestMenu import TestMenu

def my_suite():
    
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    
    suite.addTest(unittest.makeSuite(TestAdmin))
    suite.addTest(unittest.makeSuite(TestJobseeker))
    suite.addTest(unittest.makeSuite(TestCompany))
    suite.addTest(unittest.makeSuite(TestMenu))
    
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()