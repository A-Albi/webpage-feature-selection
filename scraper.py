from BeautifulSoup import BeautifulSoup
import urllib2
import re


def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

# Extracts data at the website specified by the url and returns a vector with corresponding features.

def extract(url):
    # socket.setdefaulttimeout(1.0)

    absolute = 0
    relative = 0
    https = 0
    inlinks = 0
    outlinks = 0
    avgslashes = 0
    preloaded = 0
    misspelt = 0
    avgsentence = 0
    badgrammar = 0
    avgwordlen = 0
    wordsperpage = 0

    base = "yourwebsite"
    if "www." in url:
        base = url.split(".")[1]
    else:
        base = url.split("//")[1].split(".")[0]

    site = "http://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol=JPASSOCIAT&fromDate=1-JAN-2012&toDate=1-AUG-2012&datePeriod=unselected&hiddDwnld=true"
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    req = urllib2.Request(url, headers=hdr)

    html_page = urllib2.urlopen(req)
    soup = BeautifulSoup(html_page)

    data = soup.findAll(text=True)

    visible_texts = filter(visible, data)

    result = []

    # print(visible_texts)

    for string in visible_texts:
        if string != u'\n':
            string = string.replace("-", " ")
            string = string.replace("/", " ")
            result.append("".join([x for x in string if x.isalpha() or x in [" ", "'", ".", ","]]))

    # do grammar check
    # for line in result:
    #  for sentence in line.split("."):
    #    if len(tool.check(sentence)):
    #      badgrammar += 1

    # spell check
    words = set([x.lower() for x in open("words.txt", "r").read().split("\n")])
    for line in result:
        for word in line.split(" "):
            if word == "":
                continue
            clean = "".join([x for x in word if x.isalpha()])
            if clean.lower() not in words:
                misspelt += 1

    # average sentence length
    total = 0
    num = 0
    for line in result:
        for sentence in line.split("."):
            total += len(sentence.split(" "))
            num += 1
    avgsentence = total * 1.0 / num

    total = 0
    num = 0

    # average word length
    for line in result:
        for word in line.split(" "):
            word = "".join([x for x in word if x.isalpha()])
            if len(word) > 0:
                total += len(word)
                num += 1
                wordsperpage += 1

    avgwordlen = total * 1.0 / num

    # URL stuff
    parsed_links = []
    links = soup.findAll('a', href=True)

    totalslashes = 0

    for link in links:
        if link['href'] != u'#':
            parsed_links.append(link['href'])
        if "https" in link['href']:
            https += 1
        if "http" in link['href']:
            absolute += 1
            if base in link['href']:
                inlinks += 1
            else:
                outlinks += 1
        else:
            inlinks += 1
            relative += 1
        totalslashes += link['href'].count("/")
    avgslashes = totalslashes * 1.0 / len(links)

    preloaded = len(soup.findAll('img'))

    return [absolute, relative, https, inlinks, outlinks, avgslashes, preloaded, misspelt, avgsentence, badgrammar,
            avgwordlen, wordsperpage]
