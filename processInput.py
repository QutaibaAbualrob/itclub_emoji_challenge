
import re

# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('stopwords')


from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

from spellchecker import SpellChecker


#print(stopwords.words("english"))



#Function for specllcheck
def spellCorrection(word):
    spell = SpellChecker()
    return spell.correction(word)



# To filter . / , an and so on
def removePunctions(sentences):
    for index, sentence in enumerate(sentences):
        text = re.sub(r"[^a-zA-Z0-9]", ' ', sentence)
        sentences[index] = text
    return sentences


# To split into words and return a string
def tokenizeListOfString(sentences):
    sentences_NoPunctions = removePunctions(sentences)
    words = "".join(sentences_NoPunctions)
    # print(words)
    wordsTokenized = word_tokenize(words)
    return wordsTokenized


# To remove unesseary words like he him I was etc
def removeStopWords(tokenizedWords):
    words_Tokenized_NoStopWords = []
    for word in tokenizedWords:
        temp = word.lower()
        if temp not in stopwords.words('english'):
            words_Tokenized_NoStopWords.append(temp)
    return words_Tokenized_NoStopWords


# This is not used because its not applicaple, it reudces words into smaller forms
def wordStemmer(words_Tokenized_NoStopWords):

    words_Tokenized_NoStopWords_Stemmed = []
    portstem = PorterStemmer()

    for word in words_Tokenized_NoStopWords:
        words_Tokenized_NoStopWords_Stemmed.append(portstem.stem(word))
    return words_Tokenized_NoStopWords_Stemmed


# It make words in a simple form, like cars into car
def wordLemmatizer(words_Tokenized_NoStopWords):
    lemma = WordNetLemmatizer()
    words_Tokenized_NoStopWords_Lemmated = []

    for word in words_Tokenized_NoStopWords:
        words_Tokenized_NoStopWords_Lemmated.append(lemma.lemmatize(word))
    return words_Tokenized_NoStopWords_Lemmated


def mainFunction(inputTextList):
    sentences = sent_tokenize(inputTextList)
    tokenizedWords = tokenizeListOfString(sentences)
    words_Tokenized_NoStopWords = removeStopWords(tokenizedWords)
    words_Tokenized_NoStopWords_Lemmated = wordLemmatizer(words_Tokenized_NoStopWords)
    final = words_Tokenized_NoStopWords_Lemmated
    
    return final

text = "I went to the bathroom and brushed my teeth. I went to the kitchen and I eat an apple and a banana. I drived my car to the gym to lift weights. I went home and I slept on my bed"
#print(mainFunction(text))


