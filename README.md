CSE 5820 - Group 3
April 29, 2018

Instructions:

For this project, the legit.txt, fake_checked-Copy.txt, words.txt, and fake.txt text files must be present. This program utilizes Python 2.7 and uses the BeautifulSoup, urllib2, re, sklearn, and warnings libraries.

To run this project, just run the dataset_testrun.py file, where when running the console, the lists of features by order of priority will be printed first. Then, below those three lists for Information Gain, PCA, and Chi-Squared, is the accuracy statistics.

dataset_testrun.py is the main file. It utilizes the scraper.py file to extract data that it obtains by going through the lists of websites. Then, after it does that, it accesses the calculations.py file to perform Chi-Squared, Information, and PCA calculations. Using those calculations, the calculations.py file uses them to select features to test on the Support Vector Machine.

calculations.py as mentioned before, performs the computations. It utilizes python's sklearn library. An interesting thing about this file is that for Information Gain, in order to utilize the data as discrete values, sklearn clusters the data points first into two groups and then performs the computation.

scraper.py takes in a given url, goes to that link, and begins the web scraping. It performs HTML parsing to get the respective values.

The other two python files, sitelistbuilder.py and checker.py were not utilized in the main computation, but utilized scraper.py to traverse a list of websites to compile a dataset of urls.