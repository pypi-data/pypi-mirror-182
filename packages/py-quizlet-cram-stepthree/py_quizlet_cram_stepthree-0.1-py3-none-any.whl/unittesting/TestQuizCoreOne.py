import sys
import os
import re
packagepath = os.path.abspath(__file__)
packagepath = re.sub(r'\/[^\/]*\/{1}[^\/]*(\.).*', '', packagepath)
if not packagepath in sys.path:
	sys.path.append(packagepath)

from core import quiz_methods_testcopy as methods
from core import quiz_main_testcopy
from core import quiz_main_testcopy as main

import unittest
import pandas as pd
import random as rand

class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #Generate a bank of questions/topics to assign to quiz objects
        self.wordlst = ["Question/Topic One", "Question/Topic Two", "Question/Topic Three", "Question/Topic Four",
                        "Question/Topic Five"]
    def setUp(self):
        #Generate random integers (sample without replacement) to randomly pick two different questions or topics
        #to assign to quiz objects for testing.
        self.lst = [0, 1, 2, 3]
        self.nums = rand.sample(self.lst, 4)
        self.numOne = self.nums[0]
        self.numTwo = self.nums[1]
        self.numThree = self.nums[2]
        self.numFour = self.nums[3]



    def test_Quiz(self):
        quizObj = main.Quiz()
        #Assert instantiating quiz object creates quiz type instance object
        self.assertEqual(type(quizObj), quiz_main_testcopy.Quiz)

        #Assert that instantiating quiz object contains attributes of topic, languageDict, etc...
        self.assertEqual(" ".join(vars(quizObj).keys()), "topic languageDict site setNum language results")

        #Assert that instantiating quiz object will have default attribute values of biology, etc...
        self.assertEqual(str(vars(quizObj).values()), "dict_values(['Biology', {'english': 'en', 'chinese': 'zh-tw', 'french': 'fr'}, 'quizlet', 1, 'en', 'on'])")

        #Assert that constructors with arguments will modify quiz instance attributes (assigning random topics/questions)
        quizObjOne = main.Quiz(self.wordlst[self.numOne])
        quizObjTwo = main.Quiz(self.wordlst[self.numTwo])

        #Two quiz objects with two different random questions aren't equal to each other
        self.assertNotEqual(quizObjOne.topic, quizObjTwo.topic)

        #Assigning value in constructor argument changes default attribute to one specified in argument
        self.assertNotEqual(quizObjOne.topic, "Biology")
        self.assertEqual(quizObjOne.topic, self.wordlst[self.numOne])
    def test_QA(self):
        qaObjOne = main.QA(self.wordlst[self.numOne], self.wordlst[self.numTwo], "Topic")
        qaObjTwo = main.QA(self.wordlst[self.numThree], self.wordlst[self.numFour], "Topic")

        #Assert QA object instantiates correctly
        self.assertEqual(qaObjOne.question, self.wordlst[self.numOne])
        self.assertEqual(type(qaObjOne), quiz_main_testcopy.QA)
        #Assert instantiates with attributes of question, etc.
        self.assertEqual(" ".join(vars(qaObjOne).keys()), "question answer topic mark")

        #Assert different QA objects containing two different random questions/topics are different to each other
        self.assertNotEqual(qaObjOne.question, qaObjTwo.question)

        #Assert that we can modify QA questions/answers by simple assignment statements
        qaObjOne.question = "Modified first question"

        self.assertEqual(qaObjOne.question, "Modified first question")
        self.assertNotEqual(qaObjOne.question, self.wordlst[self.numOne])
    def tearDown(self):
        #Delete random generated numbers after each function call
        self.lst, self.nums, self.numOne, self.numTwo, self.numThree, self.numFour = None, None, None, None, None, None
    @classmethod
    def tearDownClass(self):
        #Delete bank of questions and topics after testing is done
        self.wordlst = None

    unittest.main(argv=[''], verbosity = 2, exit=False)
