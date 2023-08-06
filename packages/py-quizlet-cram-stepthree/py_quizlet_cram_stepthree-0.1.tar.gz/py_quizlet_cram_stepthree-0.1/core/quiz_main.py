class Quiz():
	#importing stuff
	import sys
	import os
	import re
	packagepath = os.path.abspath(__file__)
	packagepath = re.sub(r'\/[^\/]*\/{1}[^\/]*(\.).*', '', packagepath)
	if not packagepath in sys.path:
		sys.path.append(packagepath)
	try:
		from py_quizlet_cram.network import webscraping
		from py_quizlet_cram.network import translation
	except:
		from network import webscraping
		from network import translation

	from . import quiz_methods

	#checking internet connection
	if translation.internet_checker():
		print("Internet connection confirmed.")
	else:
		raise Exception("Internet connection is required!")

	def __init__(self, topic="", site = "Quizlet", setNum = 1, language = "english", results = "on"):
		self.topic = input("\nPlease enter a topic that you want to be quizzed on: ")
		self.languageDict = {"english": "en", "chinese": "zh-tw", "french": "fr"}
		self.site = site.lower()
		self.setNum = setNum #up to a max of 8
		self.language = self.languageDict[language]
		self.results = results.lower()

		#user_control
		user_control(self)






def quiz_create(theQuiz):
	if theQuiz.site == "quizlet":
		theQuiz.url = theQuiz.webscraping.url_quizlet(theQuiz.topic)
		try:
			theQuiz.__array = theQuiz.webscraping.webscrape_quizlet(theQuiz.url, theQuiz.setNum)
		except:
			print("Sorry, no quizzes were found for: ", theQuiz.topic)
	elif theQuiz.site == "cram":
		theQuiz.url = theQuiz.webscraping.url_cram(theQuiz.topic)
		try:
			theQuiz.__array = theQuiz.webscraping.webscrape_cram(theQuiz.url, theQuiz.setNum)
		except:
			print("Sorry, no quizzes were found for: ", theQuiz.topic)
	else:
		raise Exception("Not a valid site name. Please enter either \'Quizlet\' or \'Cram\'. Default is \'Quizlet\'.")

	#translate
	if theQuiz.language != 'en':
		from py_quizlet_cram.network import translation
		translation.translate(theQuiz.__array, theQuiz.language)

	theQuiz.quiz_length = len(theQuiz.__array.index)
	theQuiz.QAs = theQuiz.quiz_methods.QA_constructor(theQuiz.__array, theQuiz.topic)







class QA():
	def __init__(self, question, answer, topic):
		self.question = question
		self.answer = answer
		self.topic = topic
		self.mark = None

	def set_mark(value):
	#0 for wrong, 1 for correct
		self.mark = value






def user_control(theQuiz):
	import py_quizlet_cram.core.quiz_methods as quiz_methods
	from IPython.display import clear_output
	theInput = ""

	#main loop
	while theInput.lower() != "exit":
		clear_output(wait=True)
		theInput = input("You are about to start a quiz on " + theQuiz.topic + " from the site " + theQuiz.site
	                   + ".\nPlease choose from the following options: \n   Start (starts the quiz!)"
	                   + "\n   Settings (change settings)\n   Exit (quit)\n")
		if theInput == "start":
	        	quiz_create(theQuiz)
	        	quiz_methods.take_the_quiz(theQuiz)
	        	theInput = "exit"
		if theInput.lower() == "settings":
			while theInput.lower() != "exit":
				clear_output(wait=True)
				theInput = input("What options do you want to change? \n   Topic (Quiz topic on "
	                             + theQuiz.topic + ")\n   Language (" + theQuiz.language + ")\n   Site (" + theQuiz.site
	                             + ")\n   Set (question bank number " + str(theQuiz.setNum) + ")\n   Results (Display results " + theQuiz.results + ")\n   Back\n   Exit\n")
				if theInput.lower() == "back":
					break;
				elif theInput.lower() == "topic":
					theInput = input("Enter topic you want to be quizzed on: \n")
					theQuiz.topic = theInput
				elif theInput.lower() == "language":
					theInput = input("Language options are: " + " ".join(['{0}'.format(k, v) for k, v in theQuiz.languageDict.items()]).title() + "\n")
					while theInput not in ["chinese", "english", "french"]:
						theInput = input("Please enter: " + " ".join(['{0}'.format(k, v) for k, v in theQuiz.languageDict.items()]).title() + "\n")
					if theInput.lower() == "english":
						theQuiz.language = theQuiz.languageDict[theInput]
					elif theInput.lower() == "chinese":
						theQuiz.language = theQuiz.languageDict[theInput]
					elif theInput.lower() == "french":
						theQuiz.language = theQuiz.languageDict[theInput]
				elif theInput.lower() == "results":
					theInput = input("Please specify \'on\' to display results, or \'off\' to not display results.\n")
					while theInput not in ["on", "off"]:
						theInput = input("Please enter either \'on\' or \'off\'.\n")
					theQuiz.results = theInput
				elif theInput.lower() == "site":
					theInput = input("Enter the website you want questions from (Quizlet or Cram):\n")
					while theInput not in ["quizlet", "cram"]:
						theInput = input("Please enter either Quizlet or Cram.\n")
					if theInput.lower() == "quizlet":
						theQuiz.site = "quizlet"
					elif theInput.lower() == "cram":
						theQuiz.site = "cram"
				elif theInput.lower() == "set":
					theInput = input("Please choose a question set number from 1 to 8.\n")
					while str(theInput) not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
						theInput = input("Please only specify question bank values from 1 to 8.\n")
					theQuiz.setNum = int(theInput)
