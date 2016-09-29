__author__ = 'paulsalvatore57'
# Difficulty: 15%

# QUESTION:

    # Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number;
    # for example, 134468.
    #
    # Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
    #
    # We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
    #
    # Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below
    # one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first
    # reaches 50% is 538.
    #
    # Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of
    # bouncy numbers is equal to 90%.
    #
    # Find the least number for which the proportion of bouncy numbers is exactly 99%.

#FINISHED

# WHAT I LEARNED:

    # So I did not need to do this problem dynamically, a BF search method was sufficient.
    # I had hoped to gain some insight on how to do the next problem but the BF search algorithm has not helped.






#A digit is increasing if each digit is proceeded by a digit larger or equal to itself: 13577
#A digit is decreasing if each digit is preceeded by a digit smaller or equal to itself: 74420
#A digit is bouncy if it does not fulfill the requirements of the above: 13527

#No bouncy numbers exists below 100, by definition.
#There are 525 bouncy numbers under 1000
#The smallest number for which the proportion of bouncy numbers:all numbers is 0.5 is 538
#When n = 21780 the proportion is 0.9

#What is the smallest number for which the proportion is 0.99?


#I am going to solve this problem dynamically.
#A number is bouncy independently of the total sample space, therefore solutions for sub-problems can be used.
#Memoization is going to be helpful for this problem.


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


def propBouncy(p = 0.99):
    """Finds the first number to have p proportion of bouncy numbers beneath it by a BF search."""
    i = 100
    n = 0.0
    while n/i != p:
        i += 1
        if isBouncy(i):
            n += 1
    return i

print propBouncy(0.99)