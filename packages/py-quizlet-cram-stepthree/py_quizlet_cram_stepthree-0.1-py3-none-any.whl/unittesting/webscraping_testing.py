#unittesting for webscraping.py functions
import unittest

import pandas as pd


#url_builders
class url_builders(unittest.TestCase): # test class

    #trying to import package
    import sys
    import os
    import re
    packagepath = os.path.abspath(__file__)
    packagepath = re.sub(r'\/[^\/]*\/{1}[^\/]*(\.).*', '', packagepath)
    if not packagepath in sys.path:
        sys.path.append(packagepath)

    from network import webscraping



    #set up and tear down
    def setUp(self):
        #print("setup")
        self.topic1 = 'cell'
        self.topic2 = 'cell bio'
        self.topic3 = 'not allowed 9'
        self.expected1_quizlet = 'https://quizlet.com/search?query=cell&type=sets&page=1&creator=teacher'
        self.expected1_cram = 'https://www.cram.com/search?query=cell&search_in%5B%5D=title&search_in%5B%5D=body&search_in%5B%5D=subject&search_in%5B%5D=username&image_filter=exclude_imgs&period=any'
        self.expected2_quizlet = 'https://quizlet.com/search?query=cell-bio&type=sets&page=1&creator=teacher'
        self.expected2_cram = 'https://www.cram.com/search?query=cell+bio&search_in%5B%5D=title&search_in%5B%5D=body&search_in%5B%5D=subject&search_in%5B%5D=username&image_filter=exclude_imgs&period=any'

    def tearDown(self):
        #print("teardown")
        del self.topic1
        del self.topic2
        del self.topic3
        del self.expected1_quizlet
        del self.expected1_cram
        del self.expected2_quizlet
        del self.expected2_cram

    #url_builders function
    def test_url_builders(self): # test case
        self.assertEqual(self.webscraping.url_quizlet(self.topic1), self.expected1_quizlet)
        self.assertEqual(self.webscraping.url_quizlet(self.topic2), self.expected2_quizlet)
        self.assertEqual(self.webscraping.url_cram(self.topic1), self.expected1_cram)
        self.assertEqual(self.webscraping.url_cram(self.topic2), self.expected2_cram)
    def error_url_builders(self):
        self.assertRaises(AssertionError, self.webscraping.url_quizlet, self.topic3)
        self.assertRaises(AssertionError, self.webscraping.url_cram, self.topic3)
unittest.main(argv=[''], verbosity=2, exit=False)





#webscraping functions....
class webscraping_funcs(unittest.TestCase): # test class
    import pandas as pd

    #trying to import package
    import sys
    import os
    import re
    packagepath = os.path.abspath(__file__)
    packagepath = re.sub(r'\/[^\/]*\/{1}[^\/]*(\.).*', '', packagepath)
    if not packagepath in sys.path:
        sys.path.append(packagepath)

    from network import webscraping



    #set up and tear down
    def setUp(self):
        #print("setup")
        import pandas as pd
        self.url_quizlet = 'https://quizlet.com/751206399/the-easy-quiz-flash-cards/'
        self.url_cram = 'https://www.cram.com/flashcards/easy-11264076'
        self.expected_quizlet = pd.DataFrame({'questions':['Ball', 'Ball', 'Ball', 'Ball', 'Ball', 'Ball', 'Ball', 'Ball', 'Ball'], 'answers':['Ball', 'Ball', 'Ball', 'Ball', 'Ball', 'Ball', 'Ball', 'Ball', 'Ball']})
        self.expected_cram = pd.DataFrame({'questions':['What', 'No', 'Blue'], 'answers':['Is', 'Say', 'Man']})

    def tearDown(self):
        #print("teardown")
        del self.url_quizlet
        del self.expected_quizlet
        del self.url_cram
        del self.expected_cram

    #url_builders function
    def test_webscraping_quizlet(self): # test case
        #issue here is that the websites change all the time, so must use override command to get specific card set
        self.assertEqual(None, self.pd.testing.assert_frame_equal(self.webscraping.webscrape_quizlet(override=self.url_quizlet), self.expected_quizlet))
    def test_webscraping_cram(self):
        self.assertEqual(None, self.pd.testing.assert_frame_equal(self.webscraping.webscrape_cram(override=self.url_cram), self.expected_cram))
unittest.main(argv=[''], verbosity=2, exit=False)
