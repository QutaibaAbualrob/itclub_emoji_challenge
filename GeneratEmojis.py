
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import json


from fromHexToUnicodeEmoji import *

def readHtmlFile(emojiHtmlFile):
    try:
        with open(emojiHtmlFile, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            print("Reading the html file is sucessful")
            #print(soup.prettify())
        return soup
    except FileNotFoundError:
        print("\nError while trying to open the HTML file in EmojiOnlyDict.py\n")  
    

def saveAsJson(dict, fileName):
    with open(fileName +'.json', 'w') as json_file:
        json.dump(dict, json_file)

def saveAsTextFile(dict, fileName):
    with open(fileName +'.txt', 'w') as file:
        json.dump(dict, file, indent=4)

def loadJson(fileName):
    with open(fileName +".json", 'r') as file:
        data = json.load(file)
    return data

# First 3 are null and the rest is flags that are shown as text like BZ
# so basicly if you want to include these just remove the uppoer bound



def emoji_Hexcode_Name(emojiHtmlFile):
    soup = readHtmlFile(emojiHtmlFile)
    rowsRaw = soup.find_all('tr')
    rows = rowsRaw[3:1649]

    #           Dictionry structure
    #
    #   key is Name of the emoji which is td with td index 8
    #   value is the hex value of the emoji which is td index 1

    dict = {}
    i = 0
    for tr in rows:
        trTdList = tr.find_all('td')
        #print("This trTdList dude", trTdList)
        #print("\n\n\n\n")

        index = 0
        value = ""
        attr = ""
        textContent = ""
        key = ""
        for td in trTdList:
            
            attr = td.attrs
            textContent = td.getText()

            if index == 1:
                value = textContent
            
            if index == 8:
                key =  textContent
            #print(f"index {index} textContent:", textContent)
            #print("Attributes:", attr)
            index +=1
        # print(f"key:", key)
        # print("value:", value)
        dict[key] = value
        # if i == 3:
        #     break
        # i +=1
    return dict

def emoji_Hexcode_Name_V2(emojiHtmlFile):

    # Wait for the page to completely load then press CTRL + S
    # to save the page as an HTML file to extract the emojis from it
    # This functions is made to read from this page
    # URL = "https://unicode.org/emoji/charts/emoji-list.html"

   
    soup = readHtmlFile(emojiHtmlFile)
    rowsRaw = soup.find_all('tr')
    rows = rowsRaw[3:1649]

    #           Dictionry structure
    #
    #   key is Name of the emoji which is td with  index 1
    #   value is the literal EMOJI value which is td index 4
    #

    dict = {}
    i = 0
    for tr in rows:
        trTdList = tr.find_all('td')
        #print("This trTdList dude", trTdList)
        print("\n\n\n\n")

        index = 0
        value = ""
        attr = ""
        textContent = ""
        key = ""

        for td in trTdList:
            
            #attr = td.attrs
            textContent = td.getText()


            if index == 1:
                value = textContent
            
            if index == 4:
                key =  textContent
            #print(f"index {index} textContent:", textContent)
            #print("Attributes:", attr)
            index +=1
        key = key.split(" | ")
        key = " ".join(key)
        print(f"key:", key)
        print("value:", value)
        dict[key] = value
        
        # if i == 11:
        #     break
        # i +=1
    return dict

def emoji_Hexcode_Name_SingleWordKey(emojiHtmlFile):
    # Wait for the page to completely load then press CTRL + S
    # to save the page as an HTML file to extract the emojis from it
    # This functions is made to read from this page
    # URL = "https://unicode.org/emoji/charts/full-emoji-list.html"

   
    soup = readHtmlFile(emojiHtmlFile)
    rowsRaw = soup.find_all('tr')
    rows = rowsRaw[3:1649]

    #           Dictionry structure
    #
    #   key is Name of the emoji which is td with  index 1
    #   value is the literal EMOJI value which is td index 4
    #

    dict = {}
    i = 0
    for tr in rows:
        trTdList = tr.find_all('td')
        #print("This trTdList dude", trTdList)
        #print("\n\n\n\n")

        index = 0
        value = ""
        attr = ""
        textContent = ""
        key = ""

        for td in trTdList:
            
            #attr = td.attrs
            textContent = td.getText()


            if index == 1:
                value = textContent
            
            if index == 8:
                key =  textContent
            #print(f"index {index} textContent:", textContent)
            #print("Attributes:", attr)
            index +=1
        key = key.split()
        if len(key) > 1 or key == "":
            continue
        key = " ".join(key)
        print(f"key:", key)
        print("value:", value)
        
        dict[key] = value
        
        # if i == 11:
        #     break
        # i +=1
    return dict
# This the var that contains the html file name
# Make sure the HTML file is the in the same directory
# Converting the values from Hex to Emojis charcters
# The reasulting dictionary will contain HEX values


# htmlFile = "emoji.html"
# dict = emoji_Hexcode_Name_SingleWordKey(htmlFile)
# dict = fromHexToUnicodeEmoji.dict_hex_to_emoji(dict)
# saveAsJson(dict, "FinalDataSingleWords")
# print(dict)




#            IMPORTANT NOTE !!!!!!!!!!!!!!!!!!!!!!!!!
#
#  iF the emoji
#  is showing up as \U0001fae0 or not displaying
#  correctly its just a display issue, if you try to print
#  it directly like this: print(dict['melting face'])
#  it will show up normally
#