import urllib.request

from bs4 import BeautifulSoup


def urlToText(param):
    # import module
    import requests
    from bs4 import BeautifulSoup

    # link for extract html data
    def getdata(url):
        r = requests.get(url)
        return r.text

    htmldata = getdata(param)
    soup = BeautifulSoup(htmldata, 'html.parser')
    data = ''
    res=""
    for data in soup.find_all("p"):
        res+=data.get_text()
    return res


def t():
    # providing url
    url = "https://www.geeksforgeeks.org/how-to-automate-an-excel-sheet-in-python/?ref=feed"

    # opening the url for reading
    html = urllib.request.urlopen(url)

    # parsing the html file
    htmlParse = BeautifulSoup(html, 'html.parser')

    # getting all the paragraphs
    for para in htmlParse.find_all("p"):
        print(para.get_text())

def t2():
    import urllib.request

    fp = urllib.request.urlopen("https://www.tennis.com/news/articles/dominic-thiem-ramping-up-schedule-starting-at-rennes-challenger")
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    print(mystr)


if __name__ == '__main__':

    text=urlToText("https://techcrunch.com/2022/09/14/google-cancels-half-the-projects-at-its-internal-rd-group-area-120/")
    import arrenmentString
    arrenmentString.g(text,{})