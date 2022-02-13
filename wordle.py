import random

def start():
    lettersRemaining = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lettersRemaining = "".join(lettersRemaining)
    firstTurn(lettersRemaining)
    
def firstTurn(lettersRemaining):
    turn = 1
    print("Wordle")
    print("=======")
    print("Try to guess what the word is!")
    answer = wordGen()
    guess = input()
    if len(guess) > 5 or len(guess) < 5:
        print("Not a valid word")
        startTurn(turn, answer, lettersRemaining)
    elif (guess in words) == False:
        print("Not in word list")
        startTurn(turn, answer, lettersRemaining)
    else:
        turn += 1
        checkWord(guess,turn,answer, lettersRemaining)

def wordGen():
    with open("sortedwords.txt", "r") as file:
        allWords = file.read()
        global words
        words = list(map(str, allWords.split()))
        answer = random.choice(words)
        return answer

def checkWord(guess, turn, answer, lettersRemaining):
    newanswer = answer
    wordList = []
    guess = guess.lower()
    if guess == answer:
        endGame(True, turn)
    else:
        for i in range(5):
            if guess[i] == newanswer[i]:
                wordList.append("✓")
                templist = list(newanswer)
                templist[i] = "."
                newanswer = "".join(templist)
            elif guess[i] in newanswer and newanswer[newanswer.index(guess[i])] != guess[newanswer.index(guess[i])]:
                wordList.append("•")
                templist = list(newanswer)
                templist[newanswer.index(guess[i])] = "."
                newanswer = "".join(templist)
            else:
                wordList.append("✕")
                if guess[i] in lettersRemaining and guess[i] not in newanswer:
                    lettersRemaining = list(lettersRemaining)
                    lettersRemaining[lettersRemaining.index(guess[i])] = ""
                    lettersRemaining = "".join(lettersRemaining)
        wordList = "".join(wordList)
        print(wordList)
        print("Letters Remaining: " + lettersRemaining)
        startTurn(turn, answer, lettersRemaining)

def startTurn(turn, answer, lettersRemaining):
    if turn > 6:
        endGame(False)
    else:
        guess = input()
        if len(guess) > 5 or len(guess) < 5:
            print("Not a valid word")
            startTurn(turn, answer, lettersRemaining)
        elif (guess in words) == False:
            print("Not in word list")
            startTurn(turn, answer, lettersRemaining)
        else:
            turn +=1
            checkWord(guess, turn, answer, lettersRemaining)
 
def endGame(victory, turn):
    if victory == True:
        print("You won in " + str(turn-1) + " turns!")
    else:
        print("Better luck next time!")
        
start()
