import unittest

#importing stuff
import sys
import os
import re
packagepath = os.path.abspath(__file__)
packagepath = re.sub(r'\/[^\/]*\/{1}[^\/]*(\.).*', '', packagepath)
if not packagepath in sys.path:
	sys.path.append(packagepath)

#import all test classes
from unittesting import translation_testing
from unittesting import webscraping_testing
from unittesting import TestQuizCoreOne
from unittesting import TestQuizCoreTwo


#run everything
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()

    #here is where you add your tests
    suite.addTest(unittest.makeSuite(translation_testing.translation))
    suite.addTest(unittest.makeSuite(translation_testing.testing_speed_warning))
    suite.addTest(unittest.makeSuite(webscraping_testing.url_builders))
    suite.addTest(unittest.makeSuite(TestQuizCoreTwo.TestMethods))
    suite.addTest(unittest.makeSuite(TestQuizCoreOne.TestMain))
    suite.addTest(unittest.makeSuite(webscraping_testing.webscraping_funcs))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
