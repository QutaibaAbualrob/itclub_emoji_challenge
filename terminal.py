import main as main


# import GeneratEmojis
import os
from os import system

def newLiner():
    print("\n")
mainKey = 0

def greeter():
    try:
        caseKey = int(input('''
Input options:
                        
1) String to Emoji
8) Clear console               
9) Exit\n
    '''))
        return caseKey
    except:
        print("\nPlease enter a number from the following list: \n")
        greeter()

def clearConsole():
    # nt for windows
    # clear for MacOS / Linux terminals
    system("cls" if os.name == "nt" else "clear")

while mainKey != -1:
    try:
        caseKey = greeter()
    except:
        print("Error in terminal")
        
    match caseKey:
        case 1:
            newLiner()
            case1Key = 0
            while case1Key != 1:
                stringInput = input("Input the string Or enter 1 to return: ")
                if stringInput == "1":
                    break
                if len(stringInput) > 2:
                    resault = main.searchDictionary_V3(stringInput)
                    print(resault)
                else:
                    print("Input is shorter than 2 characters !\n")
        case 2:
            newLiner()
            print("Case 2")
            url = input("G")
            newLiner()
            
        case 8:
            clearConsole()
        case 9:
            newLiner()
            mainKey = -1
            print('Exiting!')
            newLiner()
            break
        case _:
            newLiner()
            print("Deafult")
            
