##Network subpackage demonstration
#Jonah Edmundson

#run this file in the terminal as:
#python network_demonstration.py

import pandas as pd


#################
# webscraping module
import webscraping as ws
################

#url_quizlet
print("url_quizlet")
print("pass a topic as a string, and a quizlet URL is returned")
testing = ws.url_quizlet("cell bio")
print(testing)


#url_cram
print("\n\nurl_cram")
print("same as url_quizlet, but for cram")
testing2 = ws.url_cram("python practice")
print(testing2)


#webscrape_quizlet
print("\n\nwebscape_quizlet")
print("pass a URL and optional set number, returns a dataframe of questions and answers from quizlet")
df = ws.webscrape_quizlet(testing, setNum=5)
print(df)
print('\n\nOVERRIDE URL')
alt = ws.webscrape_quizlet(override = 'https://quizlet.com/751206399/the-easy-quiz-flash-cards/')
print(alt)


#webscrape_cram
print("\n\nwebscape_cram")
print("pass a URL and optional set number, returns a dataframe of questions and answers from quizlet")
df2 = ws.webscrape_cram(testing2, setNum=5)
print(df2)



#dataframe_builder
print("\n\ndataframe_builder")
print("takes in 2 arrays of website objects with text attributes, returns a single pandas dataframe of the text attributes")
print("since it is difficult to get these text-containing web objects, i will not demonstrate it directly here. this function can therefore only be called from within webscrape_quizlet or webscrape_cram. note the proper syntax below:")
print("lst = dataframe_builder(questionlist, answerlist)")


################
# translation module
import translation as tl
###############

#internet_checker
print("\n\ninternet_checker")
print("returns true if an internet connection exists, otherwise returns false")
print("Do we have internet? -->", tl.internet_checker())


#speed_warning
print("\n\nspeed_warning")
print("prints a speed warning for the webscraping functions")
tl.speed_warning()


#translate
print("\n\ntranslate")
print("takes in a 2 column dataframe labelled \'questions\' and \'answers\' and returns the same dataframe with translated text. also takes in the language to translate to")
print("translating to french....")
print(tl.translate(df, 'fr'))
