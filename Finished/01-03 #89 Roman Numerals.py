__author__ = 'paulsalvatore57'
# Difficulty: 20%

# QUESTION:

    # For a number written in Roman numerals to be considered valid there are basic rules which must be followed.
    # Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way
    # of writing a particular number.
    #
    # For example, it would appear that there are at least six ways of writing the number sixteen:
    #
    # IIIIIIIIIIIIIIII
    # VIIIIIIIIIII
    # VVIIIIII
    # XIIIIII
    # VVVI
    # XVI
    #
    # However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be
    # the most efficient, as it uses the least number of numerals.
    #
    # The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers
    # written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive
    # rules for this problem.
    #
    # Find the number of characters saved by writing each of these in their minimal form.
    #
    # Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

# FINISHED

# WHAT I LEARNED:

    # This was pretty easy but got me thinking about different ways to implement things.
    # In this case just going through the effort to create dictionaries was worth it.

    # After looking at other people's solutions I see that I accomplished this in a wildly inefficient way.
    # The key was in the wording and understanding the properties of what I was working with.

    # So my take away from this exercise is to understand what I'm working with: what's possible, what isn't?
    # Look for invariants that I can use to my advantage.

    # I have been working recently with prime numbers and discovered a useful property they have, the same logic applies here.

    # This is also the first time I've looked in detail at other people's code and it ended up teaching me something.
    # Therefore this exercise also showed me the value in reading other people's code.








#Roman numerals:

    #   I = 1
    #   V = 5
    #   X = 10
    #   L = 50
    #   C = 100
    #   D = 500
    #   M = 1000


    # D, L, and V can only appear once
    # Must be descending order of size.

        #This allows the subtractive rule, so IV = 4
        #Can only subtract by I, X, or C, for instance VX is invalid but XC is valid.


        #Only subtractives:

            #IV
            #XL or XC
            #CD or CM

    # C, C, and M cannot be equally by smaller denominations.
    #Use highest denominations possible (minimize letters)




#The roman numerals I have are all valid but not minimal.

#What I am thinking is to check what number each is, while noting the length, and then construct the minimal, noting the change in length.



def findNumber(numeral):
    val = 0
    values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    n = 0

    while n < len(numeral):

        try:
            if values[numeral[n+1]] > values[numeral[n]]:
                val += values[numeral[n+1]] - values[numeral[n]]
                n += 2

            else:
                val += values[numeral[n]]
                n += 1

        except:
            val += values[numeral[n]]
            n += 1

    return val


def shortestBuilder(number):
    numeral = ''

    hundreds = {1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'}
    tens = {1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'}
    ones = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}

    master = {1:hundreds, 2:tens, 3:ones}

    t = 0
    if number >= 1000:
        t = 1
        for i in xrange(int(str(number)[0])):
            numeral += 'M'

    n = 1
    if number < 100:
        n = 2
    if number < 10:
        n = 3

    for digit in str(number)[t:]:
        if digit == '0':
            n += 1
            continue
        numeral += master[n][int(digit)]
        n += 1

    return numeral


def findDifference():
    dif = 0
    numerals = open('romans.txt', 'r')
    for numeral in numerals:
        dif += len(numeral.split()[0]) - len(shortestBuilder(findNumber(numeral.split()[0])))
        # print '\n', (numeral.split()[0])
        # print (shortestBuilder(findNumber(numeral.split()[0])))
        # print findNumber(numeral.split()[0])
    return dif

print findDifference()













# Here is a really interesting code that someone posted in the forum:

    # import re
    # count = 0
    # for s in open('/Users/paulsalvatore57/PycharmProjects/General/Project Euler/Finished/romans.txt','r'):
    # 	l = len(s)
    # 	s = re.sub('IIII','IV',s)
    # 	s = re.sub('IIII','IV',s)
    # 	s = re.sub('XXXX','XL',s)
    # 	s = re.sub('CCCC','CD',s)
    # 	s = re.sub('VIV','IX',s)
    # 	s = re.sub('LXL','XC',s)
    # 	s = re.sub('DCD','CM',s)
    # 	count += l - len(s)
    # print count

#So what he is doing is replacing every possible inefficiency with the correct one.
#He can do this since we know the numbers are in valid form so these are the only ways to be inefficient.

#He used the "re" library, however the replace(old, new) function works exactly the same.