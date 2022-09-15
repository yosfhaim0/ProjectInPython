import arrenmentString


def file2string(location):
    file1 = open(location, encoding="utf8")
    t = file1.readlines()
    p = ""
    for i in t:
        p += i
    p = p.replace("\n", " ")
    file1.close()
    return p


def handlUrl(location):
    # import module
    import requests
    from bs4 import BeautifulSoup

    # link for extract html data
    def getdata(url):
        r = requests.get(url)
        return r.text

    htmldata = getdata(location)
    soup = BeautifulSoup(htmldata, 'html.parser')
    data = ''
    res = ""
    for data in soup.find_all("p"):
        res += data.get_text()
    return res


def creatFileFromString(location, textWhitTrans):
    t = location.split(".")
    file1 = open(t[0] + "arrengment." + t[1], "w", encoding="utf-8")
    # \n is placed to indicate EOL (End of Line)
    file1.writelines(textWhitTrans)
    file1.close()  # to change file access modes


def handlImage(location):
    pass


def handlDicOfJpg(location):
    pass


location = input("please inter the location(url or path) :")
x = input("a - input is location of txt file \n"
          "b - input is url\n"
          "c - input is location of image\n"
          "d - input is location of dic whit png file for translate\n"
          "e - input string of text\n"
          "  - input in test.txt file\n")
if x == "a":
    string = file2string(location)
    arr = string.split(" ")
    textWhitTrans = arrenmentString.turnArrStringToTextWhitTranslate(arr)
    # Program to show various ways to read and
    # write data in a file.
    creatFileFromString(location, textWhitTrans)
if x == "b":
    text = handlUrl(location)
    textWhitTrans = arrenmentString.turnArrStringToTextWhitTranslate(arr)
    creatFileFromString("test.txt", textWhitTrans)

if x == "c":
    handlImage(location)
if x == "d":
    handlDicOfJpg(location)
if x == "e":
    arr = location.split(" ")
    textWhitTrans = arrenmentString.turnArrStringToTextWhitTranslate(arr)
    creatFileFromString("test.txt", textWhitTrans)

if x=="":
    arr = file2string("test.txt").split(" ")
    textWhitTrans = arrenmentString.turnArrStringToTextWhitTranslate(arr)
    creatFileFromString("test.txt", textWhitTrans)