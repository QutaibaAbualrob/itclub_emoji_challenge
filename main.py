import processInput
import GeneratEmojis
import spellchecker

#pip install nltk pyspellchecker beautifulsoup4 requests playwright fromHexToUnicodeEmoji
#playwright install

# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# dict = GeneratEmojis.emoji_Hexcode_Name("emoji.html")
# print(dict)




# Early version 
def searchDictionary_V1(textInput):
    ans = ""
    processed_Input = processInput.mainFunction(textInput)
    dict = GeneratEmojis.loadJson("emojiProject/data/finalDataV2")

    for word in processed_Input:
        temp = ""
        index = -99
        for key, value in dict.items():
            # if key.startswith(word):
            #     temp = word + ' ' +key + ' ' +  value + ' '  
            if word in key:
                if len(key) == len(word):
                    #temp = word + ' ' + key + ' ' + value + ' '
                    temp = value + ' '
                    break
                else:
                    keySplit = key.split()
                    if word in keySplit:
                        #temp = word + ' ' + key + ' ' + value + ' '
                        temp = value + ' '
                        break
                        
        ans += temp        
    return ans

# Early version 
def searchDictionary_V2(textInput):
    ans = ""
    processed_Input = processInput.mainFunction(textInput)
    dict = GeneratEmojis.loadJson("emojiProject//data/finalData")
    
    for word in processed_Input:
        temp = ""
        index = -99
        for key, value in dict.items():
            # if key.startswith(word):
            #     temp = word + ' ' +key + ' ' +  value + ' '  
            if word in key:
                if len(key) == len(word):
                    #temp = word + ' ' + key + ' ' + value + ' '
                    temp = value + ' '
                    break
                else:
                    keySplit = key.split()
                    for i, split in enumerate(keySplit):
                        if word in split and len(word) == len(split):
                            #temp = word + ' ' + key + ' ' + value + ' '
                            temp = value + ' '
                            break
                            index = i
        ans += temp        
    return ans



#   Made sure that the searching process is efficient as I spilt the data into two dictionaries
#	one dictionary with that contain simple keys like "Cat". these single word elements allow for 
#	fast look up.

def searchDictionary_V3(textInput):
    ans = ""
    processed_Input = processInput.mainFunction(textInput)
    dict = GeneratEmojis.loadJson("emojiProject/data/FinalDataSingleWords")
    dict2 = GeneratEmojis.loadJson("emojiProject/data/FinalDataV2")

    for word in processed_Input:
        temp = ""
        index = -99
        word = processInput.spellCorrection(word)
        if word in dict:
            #temp = word + ' ' + key + ' ' + value + ' '
            temp = dict[word] + ' '
            ans += temp 
            continue
        for key, value in dict2.items():
                # if key.startswith(word):
                #     temp = word + ' ' +key + ' ' +  value + ' '  
                if word in key:
                    if len(key) == len(word):
                        #temp = word + ' ' + key + ' ' + value + ' '
                        temp = value + ' '
                        break
                    else:
                        keySplit = key.split()
                        if word in keySplit:
                            #temp = word + ' ' + key + ' ' + value + ' '
                            temp = value + ' '
                            break
        ans += temp        
    return ans

TestCases = [
    "The sun is shining brightly today.", #0
    "I love eating pizza with my cats.",
    "She adopted a cute little dog.",
    "The fire in the fireplace keeps us warm.",
    "He gave her a red rose on Valentine's Day.",
    "The cat is sleeping on the windowsill.", #5
    "I’m feeling so happy right now!",
    "Let’s go to the beach and watch the waves.",
    "The airplane flew high above the clouds.",
    "I enjoy reading books in my free time.",
    "The baby is laughing at the funny clown.", #10
    "We saw a rainbow after the rain stopped.",
    "The clock struck midnight, and the party began.",
    "She loves to drink coffee in the morning.",
    "The tree is full of ripe, juicy apples.",
    "He bought a new car and drove it home.", #15
    "The moon is glowing in the night sky.",
    "I’m craving a slice of chocolate cake.",
    "The dog barked loudly at the stranger.",
    "She wore a beautiful dress to the party.",
    "The train arrived at the station on time.", #20
    "He sent her a heart emoji in the text.",
    "The kids are playing with a soccer ball.",
    "I’m so tired after running a marathon.",
    "The teacher wrote on the chalkboard.",
    "The phone rang, but no one answered.", #25
    "The bird is singing a sweet melody.",
    "I’m excited to travel to a new country.",
    "The movie was so sad, it made me cry.",
    "The stars are twinkling in the dark sky." #29
]


# TestCases2 = ["I love eating pizza with my friends."]
# i = 0
# for sentence in TestCases:
#     ans = searchDictionary_V3(sentence)
#     print(i, ans, '\n')
#     i+=1
