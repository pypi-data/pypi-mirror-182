def QA_constructor(QAdataframe, topic):
	import pandas as pd
	from . import quiz_main_testcopy
	array = []
	for i in range(len(QAdataframe.index)):
		temp = quiz_main_testcopy.QA(QAdataframe.loc[i, "questions"], QAdataframe.loc[i, "answers"], topic)
		array.append(temp)

	return array





def take_the_quiz(quiz):
	from py_quizlet_cram.core import quiz_main_testcopy
	import time
	from IPython.display import clear_output
	assert isinstance(quiz, quiz_main_testcopy.Quiz)

	length = quiz.quiz_length
	array = quiz.QAs

	print_options(quiz)


	theInput = None
	for i in range(quiz.quiz_length):
		print("Question " + str(i + 1) + " of " + str(quiz.quiz_length) + ": " + quiz.QAs[i].question +
		"\nPress enter for the answer, hint for hints, or exit to exit. \n")
		while theInput not in ["", "exit"]:
			theInput = input()
			if theInput == "hint":
				print(hints(quiz.QAs[i].answer))
		if theInput == "":
			print("Answer:")
			print(quiz.QAs[i].answer)
			if quiz.results == "on":
				rightwrong = input("Did you understand this concept? (Y/N). \n").lower()
				while not ((rightwrong == "y") or (rightwrong == "n")):
					rightwrong = input("Please specify Y or N. \n").lower()
				array[i].mark = rightwrong
				if rightwrong == "y" or rightwrong == "n":
					clear_output(wait=False)
					theInput = "placeHolder"

			else:
				theInput = input()
				if theInput != "exit":
					clear_output(wait=False)
					theInput = "placeHolder"
				elif theInput == "exit":
					break
		elif theInput == "exit":
			break

	print("\nWell done! Quiz is finished. \n")

	#call plotting methods
	if quiz.results.lower() == "on":
		results_plot(quiz)




def print_options(quiz):
	import time
	print("You are about to start the quiz with the following options...:")
	time.sleep(2)
	print("Your topic:", quiz.topic)
	time.sleep(1)
	print("With questions from:", quiz.site)
	time.sleep(1)
	print("Using question bank number:", quiz.setNum)
	time.sleep(1)
#	print("Total number of questions:", quiz.quiz_length)
	time.sleep(1)
	print("Language:", quiz.language)
	time.sleep(1)
	print("With results:", quiz.results)
	time.sleep(1)
	print("Good luck!")



def results_plot(quiz):
	import matplotlib.pyplot as plt

	array = []
	length = quiz.quiz_length
	for i in range(length):
		array.append(quiz.QAs[i].mark)

	if (quiz.results == "off"):
		print("Cannot print results if results was set to \'off\'. \n")
		return
	if array.count('y') + array.count('n') == 0:
		pass
	else:

		plotting = [array.count('y'), array.count('n')]

		print("Right:", plotting[0])
		print("Wrong:", plotting[1])
		print("Grade:", round(plotting[0]/length * 100), "%")

		plt.pie(plotting, labels = ['Right', 'Wrong'])
		plt.show()





def hints(word):
	import random
	from IPython.display import clear_output
	hintAnswer = []
	if len(word.split(" ")) != 1:
		randomLister = []
		splitSentence = word.split(" ")
		for i in range(len(splitSentence)):
			randHint = random.randint(0, len(splitSentence))
			randomLister.append(randHint)
		for j in range(len(splitSentence)):
			appendWord = splitSentence[j]
			if j in randomLister:
				hintAnswer.append(appendWord)
			if j not in randomLister:
				theWord = splitSentence[j]
				for k in range(len(theWord)):
					theWord = theWord.replace(theWord[k], "_")
				hintAnswer.append(theWord)
	elif len(word.split(" ")) == 1:
		randList = []
		theWord = word
		for l in range(len(theWord)):
			randHint = random.randint(0, len(theWord))
			randList.append(randHint)
		for m in range(len(theWord)):
			if m not in randList:
				theWord = theWord.replace(theWord[m], "_")
		hintAnswer.append(theWord)
	return " ".join(hintAnswer)
