import asyncio
import re

from flask import Flask
from googletrans import Translator
from pymongo import MongoClient


def findIfInCommon(d: set, param):
    if param in d:
        return False
    if param.endswith("ing"):
        if param[:-3] in d:
            return False
    if param.endswith("s"):
        if param[:-1] in d:
            return False
    if param.endswith("ed"):
        if param[:-2] in d:
            return False
    for i in d:
        if i in param and len(i) > len(param) - 2 or param in i and len(param) > len(i) - 2:
            return False
    return True


def findInDomain(arr, param):
    domain = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    for index, j in enumerate(param):
        assciVal = ord(j) - 97
        if assciVal >= 0 and assciVal <= 26:
            domain[assciVal] = index
    maxMatch = -1
    for i in arr:
        numOfMatch = 0
        for index, j in enumerate(i):
            if j == domain[index] and j != -1:
                numOfMatch += 1
        if numOfMatch > maxMatch:
            maxMatch = numOfMatch

    if maxMatch > len(param) - 3:
        return True


def buildDomain(d):
    domain = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    arr = []
    for i in d:
        dom = domain.copy()
        for index, j in enumerate(i):
            assciVal = ord(j) - 97
            if assciVal >= 0 and assciVal <= 26:
                dom[assciVal] = index
        arr += [dom]


def g(sourc, d, d2={}, nf="test.txt", whitLines=False):
    if not d:
        d = handleCommonWordEnglish("commonWordsEnglish.txt")
    arr = buildDomain(d)

    textWhitTrans = ""
    findAllReady = set()
    numOfTranslate=0
    if isinstance(sourc, str):
        sourc=sourc.split(" ")
    try:
        for i in sourc:
            textWhitTrans += i
            if not i in findAllReady:
                regex = r'\b[A-Za-z_|\'|\-]+\b'
                arstr = re.findall(regex, i)
                if arstr and not arstr[0][0].isupper() and len(arstr[0]) > 2 and findIfInCommon(d, arstr[
                    0]) and findIfInCommon(d2, arstr[0]):
                    translate = traslate_word(arstr[0])
                    if translate and not i == translate and len(translate) > 2:
                        textWhitTrans += "= " + str(translate)
                        findAllReady.add(i)
                        numOfTranslate+=1
            textWhitTrans += " "
            if whitLines:
                textWhitTrans += "\n"
    finally:
        # Program to show various ways to read and
        # write data in a file.
        t = nf.split(".")
        file1 = open(t[0] + "arrengment." + t[1], "w", encoding="utf-8")

        # \n is placed to indicate EOL (End of Line)
        file1.writelines(textWhitTrans)
        file1.close()  # to change file access modes
        print("num Of Translate word : ",numOfTranslate)
        return textWhitTrans


def find_in_db(english):
    return db["EnglishHebrew"].find_one({'english': english})


async def insert_one(english, hebrew):
    db["EnglishHebrew"].insert_one({'english': english, 'hebrew': hebrew})


def traslate_word(word):
    res = find_in_db(word)
    if res:
        return res["hebrew"]
    else:
        translate = translator.translate(word, dest='he')
        asyncio.run(insert_one(word, translate.text))
        return translate.text


def handelTextFile(f):
    file1 = open(f, encoding="utf8")

    t = file1.readlines()
    p = ""
    for i in t:
        p += i
    p = p.replace("\n", " ")
    p = p.split(" ")

    file1.close()
    return p


def handleCommonWordEnglish(cwe):
    file1 = open(cwe, "r+")
    regex = r'\b\w+\b'
    fileOrder = re.findall(regex, str(file1.readlines()))
    s = set()
    for i in fileOrder:
        s.add(i)
    return s


def writeSetInFile(fileName, s):
    f = open(fileName, "w")
    for i in sorted(s):
        f.write(i)
        f.write("\n")
    f.close()


app = Flask(__name__)
client = MongoClient(port=27017)
database_name = "EnglishHebrew"
db = client[database_name]
translator = Translator()
# input = sys.argv[1]
# output = g(input)
# sys.stdout.flush()

if __name__ == "__main__":
    htf = handelTextFile("test.txt")
    hcwe = handleCommonWordEnglish("commonWordsEnglish.txt")
    ncwe = handleCommonWordEnglish("tenKcommonWord.txt")
    g(htf, hcwe, ncwe, "test.txt")
