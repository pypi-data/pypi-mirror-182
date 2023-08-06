import sys
import os
import re
packagepath = os.path.abspath(__file__)
packagepath = re.sub(r'\/[^\/]*\/{1}[^\/]*(\.).*', '', packagepath)
if not packagepath in sys.path:
	sys.path.append(packagepath)

from core import quiz_methods_testcopy as methods
from core import quiz_main_testcopy
import unittest
import pandas as pd
import random as rand

class TestMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #Generate a question bank of random questions and answers to test quiz functions on
        self.data = [
            ["Central Processing Unit (CPU)", "Brain of the computer that performs instructions defined by software"],
            ["Software", "Set of instructions that tells the hardware what to do. It is what guides the hardware and tells it how to accomplish each task."],
            ["Operating System (OS)", "Software used to control the computer and its peripheral equipment."],
            ["Test Question", "TestQuestionWithOneWordAnswer"]
                ]

        self.QADataFrame = pd.DataFrame(self.data, columns = ["questions", "answers"])


    def setUp(self):
        #Sample random numbers (without replacement), used to randomly assign questions/answers to quiz objects and test functions
        #For example, quizObjectOne assigned random question 1 should be different than quizObjectTwo asisgned random question 2

        self.lst = [0, 1, 2, 3]
        self.nums = rand.sample(self.lst, 4)
        self.numOne = self.nums[0]
        self.numTwo = self.nums[1]

    def test_QA_constructor(self):
        ##Assert conversion from dataframe to array works.
        self.assertEqual(type(methods.QA_constructor(self.QADataFrame, "Computer Science")), list)
        self.assertNotEqual(type(methods.QA_constructor(self.QADataFrame, "Computer Science")), type(self.QADataFrame))

        #Assert array contains QA types
        self.assertEqual(type(methods.QA_constructor(self.QADataFrame, "Computer Science")[1]), quiz_main_testcopy.QA)

        #Assert that the questions and answers from the dataframe input are correctly converted
        self.assertEqual(methods.QA_constructor(self.QADataFrame, "Computer Science")[1].question, "Software")
        self.assertEqual(methods.QA_constructor(self.QADataFrame, "Computer Science")[1].answer, "Set of instructions that tells the hardware what to do. It is what guides the hardware and tells it how to accomplish each task.")

        #Assert that two (random) different answers in the QA array are not duplicates (i.e. same as each other)
        self.assertNotEqual(methods.QA_constructor(self.QADataFrame, "ComputerScience")[self.numOne].answer, methods.QA_constructor(self.QADataFrame, "Computer Science")[self.numTwo].answer)
        self.assertNotEqual(methods.QA_constructor(self.QADataFrame, "ComputerScience")[self.numOne].question, methods.QA_constructor(self.QADataFrame, "Computer Science")[self.numTwo].question)


    def test_hints(self):
        #Assert that output for hints is different than input, where input is random answers from the answers column in dataframe
        self.assertNotEqual(methods.hints(self.QADataFrame.iloc[self.numOne, 1]), methods.hints(self.QADataFrame.iloc[self.numOne, 1]))

        #Assert that output for hints for sentences is different from input for sentences
        self.assertNotEqual(methods.hints(self.QADataFrame.iloc[2, 1]), methods.hints(self.QADataFrame.iloc[2, 1]))

        #Assert that output for hints for single words is different from input for single words
        self.assertNotEqual(methods.hints(self.QADataFrame.iloc[3, 1]), methods.hints(self.QADataFrame.iloc[3, 1]))

        #Assert that hint will print out at least one underscore
        self.assertGreater(str.count(methods.hints(self.QADataFrame.iloc[self.numOne, 1]), "_"), 0)



    def tearDown(self):
        #Delete random generated numbers after each function call and generate new ones
        self.lst, self.nums, self.numOne, self.numTwo = None, None, None, None

    @classmethod
    def tearDownClass(self):
        #Delete question/answer dataframe after testing is done
        self.data, self.QADataFrame = None, None
    unittest.main(argv=[''], verbosity = 2, exit=False)
