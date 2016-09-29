__author__ = 'paulsalvatore57'
# Difficulty: 30%

# QUESTION:

    # Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number;
    # for example, 134468.
    #
    # Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
    #
    # We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
    #
    # As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers
    # below one-million that are not bouncy and only 277032 non-bouncy numbers below 1010.
    #
    # How many numbers below a googol (10100) are not bouncy?

#FINISHED.

# WHAT I LEARNED:

    # Using a BF algorithm to check lower solutions was precisely the tool I needed to solve this problem.
    # I relied heavily on my own pattern recognition to solve this problem, and found writing out the problem to be immensely helpful.
    # I wanted to give up on this problem yet I knew I was very close therefore I am happy I persevered.
    # My main takeaway from this problem was using pattern recognition and easy to compute (via BF) test cases to assess my answer.












#A digit is increasing if each digit is proceeded by a digit larger or equal to itself: 13577
#A digit is decreasing if each digit is preceeded by a digit smaller or equal to itself: 74420
#A digit is bouncy if it does not fulfill the requirements of the above: 13527

#Non-bouncy below 10**6: 12951
#Non-bouncy below 10**10: 277032

#The question is to find the number of non-bouncy below 10**100.



#My initial strategy to build the answer is by using the characteristics of increasing (INC) and decreasing (DEC) digits.
    #If a 9 occurs in an INC digit, it can only be proceeded by 9.
    #If an 8  occurs in an INC digit, it can only be proceeded by 8 and 9.


#The part that is stumping me right now is how to account for adjacent numbers being allowed to be equal to one another.
#This creates the problem that 123 is INC, as is 1233, 12333, 12233, etc.
#This creates a huge number of possibilities and I'm not quite sure how to handle them.

#What I need is a generating function.



def isBouncy(d):
    """Returns True is a number is bouncy, returns False if a number is not bouncy (i.e. increasing or decreasing)."""
    d, inc, dec = str(d), False, False
    for i in xrange(len(d)):

        try:

            if d[i] == d[i + 1]:
                continue

            if d[i] > d[i + 1]:
                if dec:
                    return True
                inc = True
            else:
                if inc:
                    return True
                dec = True

        except IndexError:
            break

    return False

def findNonBouncyBF(n = 6):
    n = 10**n
    tot = 0
    for i in xrange(n):
        if not isBouncy(i):
            tot += 1
            # print i
    return tot


# print 'BF solve:', findNonBouncyBF(10), '\n'


def computeINC(numDigits):
    """Gives the number of increasing numbers that exist underneath 10**numDigits
    So, if numDigits = 3, then the answer will yield all increasing numbers up to 1000"""
    assert numDigits > 0

    if numDigits == 1:
        return 9

    tots = []

    start = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    spot = 2
    while spot < numDigits:
        tots.append(sum(start))
        spot += 1
        next = []
        for i in xrange(10):
            next.append(sum(start) - sum(start[:i]))
        start = next[:]
        # print next
    return sum(start + tots)



def computeDEC(numDigits):
    """Gives the number of decreasing numbers that exist underneath 10**numDigits
    So, if numDigits = 3, then the answer will yield all decreasing numbers up to 1000"""
    assert numDigits > 0

    if numDigits == 1:
        return 0

    start = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    spot = 2
    while spot < numDigits:
        spot += 1
        next = []
        for i in xrange(10):
            next.append(sum(start) - sum(start[i + 1:]))
        start = next[:]
        # print next
    return sum(start)


def findOverlap(numDigits):
    return 9 * (numDigits - 1)


def googolFinder(n=100):
    inc = computeINC(n)
    dec = computeDEC(n)
    ovr = findOverlap(n)
    print '\nIncreasing:', inc
    print 'Decreasing:', dec
    print 'Overlap:', ovr
    print inc + dec - ovr
    if n == 6:
        if inc + dec - ovr != 12951:
            print '\nDoes not pass 6 digit test case.'
    elif n == 10:
        if inc + dec - ovr != 277032:
            print '\nDoes not pass 10 digit test case.'


googolFinder()

