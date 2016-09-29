__author__ = 'paulsalvatore57'
# Difficulty: 35%

# QUESTION:

    # By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively,
    # we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions,
    # the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram
    # word pair and specify further that leading zeroes are not permitted, neither may a different letter have
    # the same digital value as another letter.
    #
    # Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand
    # common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an
    # anagram of itself).
    #
    # What is the largest square number formed by any member of such a pair?
    #
    # NOTE: All anagrams formed must be contained in the given text file.

# FINISHED

# WHAT I LEARNED:

    # The value of helper functions.
    # I was having the problem of not being able to get out of loops when I wanted to,
    # When I realized that I could make a helper function and return None whenever I wanted to break the loop, this task became trivial.















# What we are looking for are numbers that you can replace a letter with and these numbers read as is (in the word) will be a square number

# For instance the word: HEDGEHOG can be 12342154, or alternatively it can be 98768956, however for it to be a square anagram these numbers must be perfect squares.

# This means what must happen is I must iterate through every possible combination of letters until I get a perfect square.
# Rather, it may be easier to find the longest length word and find all of the perfect squares up to that length of digits.

# Caveats to remember are that the leading entry may not be a 0 and that words tha tuse the same letter multiple times have the same value.
# Furthermore, no two different letters may have the same value.

import string, pickle, time

def loadWords(file):
    """
    This function reads the word list and returns a list of the words.
    """
    data = open(file, 'r')
    for line in data:
        line = line.replace(',', ' ')
        line = line.replace('"', ' ')
        dataLine = string.split(line)
    return dataLine


def findAnagrams():
    words = loadWords('98_words.txt')

    anagrams = []
    wordsDictList = []

    #This assigns a dictionary to each word comprised of the number of times each letter occurs.
    for word in words:
        dict = {}
        for letter in word:
            if letter.lower() not in dict:
                dict[letter.lower()] = 1
            else:
                dict[letter.lower()] += 1
        wordsDictList.append((dict, word))

    #This checks for identical dictionaries-denoting anagrams-and adds the anagram pairs to the anagram list.
    for i in wordsDictList:
        for j in wordsDictList:
            if i[0] == j[0] and i[1] != j[1] and (j[1], i[1]) not in anagrams:
                anagrams.append((i[1], j[1]))

    #Loads the list of square number pairs that are anagrams to each other (share the same digits).
    anaSqDict = pickle.load(open('Anagramic square pairs, sorted by number of digits'))

    #Checks each pair in the anagrams with the correspondence function to see if they are square anagrams.
    sqAnas = []
    for pair in anagrams:
        try:
            squares = anaSqDict[len(pair[0])]
            for square in squares:
                ans = correspondence(pair, square)
                if ans != None:
                    sqAnas.append(ans)
        except:
            KeyError
            continue

    #Searches the anagramic squares for the one with the highest value.
    highest = None
    for sqA in sqAnas:
        if highest == None:
            highest = sqA
        elif int(sqA[0]) > int(highest[0]):
            highest = sqA

    print '\nHighest:', highest



def correspondence(pair, square):
    """
    Takes a pair of anagrams, and a square number that has an anagramic square.
    Assigns numeric value to each letter of the first element of the pair, and checks if the second word will result in an anagramic number with these bindings.
    Returns None if a number must be bound twice to separate letters.
    """

    for q in range(2):
        newWord = ''
        letterDict = {}

        for i in range(len(pair[0])):

            #This line is important for ensuring that the same number cannot be bound to different letters.
            for let in letterDict:
                if letterDict[let] == str(square[q])[i] and let != pair[0][i]:
                    return None

            letterDict[pair[0][i]] = str(square[q])[i]

        #Builds the new digit based on the dictionary built directly above this line of code.
        for i in range(len(pair[0])):
            newWord += letterDict[pair[1][i]]

        #The only square numbers that could occur are the ones inputted into the function (since they are anagramic squares),
        #Therefore checks if the 'newWord' or rather new number is equal to one of these. If so this is an anagramic square.
        if int(newWord) == square[0] or int(newWord) == square[1]:
            return (newWord, square, pair)

        else:
            return None

findAnagrams()






#Current issue is multiple letters being bound to the same number



# I know have all of the combinations of anagrams in a list, what I need to do now is find the combinations of numbers that will make perfect squares
# I can do this two ways, I can either try a random approach, or I can try to iterate through every possibility.
# The big problem I need to work around is having multiple copies of the same letter (which must be identical in numeric value), as well as no repeating numbers.


# Think I need to find the anagramic squares before I can continue, must go up to 9 digits.


def findAnagramicSquares():
    """
    I needed to get all of the possible square number answer, however this takes a relatively long time to do,
    Therefore I did it all at once and saved the pairs before trying to find anagrams that fit the square anagram requirement.
    """

    #Creates a list of all square numbers less than 10 digits in length.
    anagramicSquares = {}
    hold = 0
    squares = []
    i = 1
    while True:
        if i**2 < 1000000000:
            squares.append(i**2)
            i += 1
        else:
            break

    #Assigns a dictionary of the frequency of each digit to the square number, as was done for the words
    squaresDictList = []
    for square in squares:
        dict = {}
        for dig in str(square):
            if dig not in dict:
                dict[dig] = 1
            else:
                dict[dig] += 1
        squaresDictList.append((dict, square))

    #Used to find numbers with identical dictionaries, meaning they are anagrams.
    #Simultaneously removes the numbers from the list such that the operation may proceed more rapidly (it is a large job).
    passNum = []
    for i in squaresDictList:
        if i in passNum:
            continue
        for j in squaresDictList:
            if i[0] == j[0] and i[1] != j[1]:

                if len(str(i[1])) not in anagramicSquares:
                    anagramicSquares[len(str(i[1]))] = [(i[1], j[1])]
                else:
                    anagramicSquares[len(str(i[1]))] += [(i[1], j[1]),]

                passNum += [j,]
                squaresDictList.pop(squaresDictList.index(j))

        squaresDictList = squaresDictList[squaresDictList.index(i):]

        #Monitors progress
        if len(squaresDictList)%1000 == 0:
            print 'Items in list:', len(squaresDictList), 'Time:', time.clock() - hold
            hold = time.clock()
            # t0 = time.clock()

    pickle.dump(anagramicSquares, open('Anagramic square pairs, sorted by number of digits', 'wb'))

# findAnagramicSquares()


