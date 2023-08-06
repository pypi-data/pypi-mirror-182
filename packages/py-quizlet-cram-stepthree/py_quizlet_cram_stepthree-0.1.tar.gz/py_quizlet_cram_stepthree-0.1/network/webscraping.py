def url_quizlet(topic):
	assert type(topic) == str, "Error: topic must be a string."
	allowedchars = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	assert set(topic).issubset(allowedchars), "Please enter only letters."
	topicF = topic.replace(" ", "-")
	url = "https://quizlet.com/search?query=" + topicF + "&type=sets&page=1&creator=teacher" #&useOriginal=
	return url


def url_cram(topic):
	assert type(topic) == str, "Error: topic must be a string."
	allowedchars = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	assert set(topic).issubset(allowedchars), "Please enter only letters."
	topicF = topic.replace(" ", "+")
	url = "https://www.cram.com/search?query=" + topicF + "&search_in%5B%5D=title&search_in%5B%5D=body&search_in%5B%5D=subject&search_in%5B%5D=username&image_filter=exclude_imgs&period=any"
	return url



def webscrape_quizlet(url=None, setNum=1, override=None):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    import time

    if (override==None):
	    try:
	        import translation
	    except:
	        from . import translation
	    translation.speed_warning()

	    ###search page
	    driver = webdriver.Firefox()
	    driver.get(url)

	    try:
	        cardset = WebDriverWait(driver, 15).until(EC.visibility_of_all_elements_located(('xpath', "//*[@class='SearchResultsPage-result' and @data-page-depth='" + str(setNum) + "']//*[@class='AssemblyLink AssemblyLink--medium AssemblyLink--title']")))

	        cardseturl = None
	        cardseturl = cardset[0].get_attribute('href')

	        driver.quit()
	    except NoSuchElementException:
	        driver.quit()
	        print("No quizzes found for user topic.")
	        return

	    except:
	        driver.quit()
	        print("Request timed out.")
	        return
    else:
        cardseturl = override


    ###card set page
    driver = webdriver.Firefox()
    driver.get(cardseturl)

    time.sleep(2)
    html = driver.find_element('tag name', 'html')
    html.send_keys(Keys.PAGE_DOWN)

    questionlist = WebDriverWait(driver, 45).until(EC.visibility_of_all_elements_located(('xpath', "//*[@class='SetPageTerms-term' and @aria-label='Term']//*[@class='SetPageTerm-side SetPageTerm-smallSide']//*[@class='TermText notranslate lang-en']")))

    answerlist = WebDriverWait(driver, 45).until(EC.visibility_of_all_elements_located(('xpath', "//*[@class='SetPageTerms-term' and @aria-label='Term']//*[@class='SetPageTerm-side SetPageTerm-largeSide']//*[@class='TermText notranslate lang-en']")))

    QAdataframe = dataframe_builder(questionlist, answerlist)

    driver.quit()

    print("Done.")

    return QAdataframe

    #can delete later
    #attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', cardset[0])
    #print(attrs)







def webscrape_cram(url=None, setNum=1, override=None):
	from selenium import webdriver
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.common.by import By
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.common.keys import Keys
	import time
	import pandas as pd


	if (override==None):
		try:
			import translation
		except:
			from . import translation
			translation.speed_warning()

		###search page
		driver = webdriver.Firefox()
		driver.get(url)


		try:
			cardset = WebDriverWait(driver, 45).until(EC.visibility_of_all_elements_located(('xpath', "//*[@class='searchResults']//*[@class='info']/h3/a")))

			cardseturl = cardset[setNum-1].get_attribute('href')

			driver.quit()

		except NoSuchElementException:
			driver.quit()
			print("No quizzes found for user topic.")
			return

		except:
			driver.quit()
			print("Request timed out.")
			return
	else:
		cardseturl = override


	###card set page
	driver = webdriver.Firefox()
	driver.get(cardseturl)

	time.sleep(2)
	html = driver.find_element('tag name', 'html')
	html.send_keys(Keys.PAGE_DOWN)

	from selenium.webdriver.support.ui import Select
	select = Select(driver.find_element('id', 'tablePagination_rowsPerPage'))
	select.select_by_visible_text('100')

	questionlist = driver.find_elements('xpath', "//*[@class='flashCardsListingTable']//*[@class='front_text card_text']")

	answerlist = driver.find_elements('xpath', "//*[@class='flashCardsListingTable']//*[@class='back_text card_text']")

	#questionlist = WebDriverWait(driver, 60).until(EC.visibility_of_all_elements_located(('xpath', "//*[@class='flashCardsListingTable']//*[@class='front_text card_text']")))

	#answerlist = WebDriverWait(driver, 60).until(EC.visibility_of_all_elements_located(('xpath', "//*[@class='flashCardsListingTable']//*[@class='back_text card_text']")))

	QAdataframe = dataframe_builder(questionlist, answerlist)

	driver.quit()

	print("Done.")

	return QAdataframe





def dataframe_builder(col1, col2):
    import pandas as pd

    questiontext = []
    answertext = []


    for i in range(len(col1)):
        if col1[i].text:
            questiontext.append(col1[i].text)
        else:
            questiontext.append("<image>")

    for i in range(len(col2)):
        if col2[i].text:
            answertext.append(col2[i].text)
        else:
            answertext.append("<image>")

    #creating dataframe for export
    questions = []
    answers = []


    QAdataframe = pd.DataFrame({'questions': questiontext, 'answers': answertext})
    return QAdataframe
