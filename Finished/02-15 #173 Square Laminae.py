__author__ = 'paulsalvatore57'
# Diffculty: 30%

# QUESTION:

    # We shall define a square lamina to be a square outline with a square "hole" so that the shape
    # possesses vertical and horizontal symmetry. For example, using exactly thirty-two square tiles
    # we can form two different square laminae:
    #
    # With one - hundred tiles, and not necessarily using all of the tiles at one time, it is possible
    # to form forty - one different square laminae.
    #
    # Using up to one million tiles how many different square laminae can be formed?

# FINISHED

# WHAT I LEARNED:

# The problem was I had a > where I should have had a >=, showing that it was an error of carelessness.
# To solve this problem I went back over the examples given in the question and found that my program
# could not solve one of the cases. This taught me that making a test handle to test these known cases would have
# saved me a lot of time and energy. I am happy I finished this relatively straight forward problem.








#Using up to 1 million tiles how many square laminae can be formed,
#That is squares that have hollow squares in the middle.

#There are going to be two different sets that I have to work with here, ones with odd and even lengths.
#The smallest length of the holes may either be 3x3 or 4x4.
#I do not necessarily have to use all of the laminae at once make my answer much larger.

#What I want to find first is the biggest square I can make that is one thick.
#I need to account for the corners so the total will equal 2x + 2(x-2) where x represents the length of each side.
    #total = 4x - 4

#The maximum sized square that I can make is 250,001 x 250,001 using 1,000,000 tiles.
#This means that I can make every single square smaller than it.

#What I want to find is that from 250,001 on each side to 3 on each side:
    #How many tiles are left over?
    #How many rows smaller can I make?

    #The summation of how many smaller rows I can make will be the answer to this question.


def findLaminae():
    ways = 0
    for lngth in xrange(250001, 2, -1):
        ways += 1
        total = 1000000 - 4*lngth + 4
        next = 4*(lngth - 2) - 4
        while total >= next and next > 4:
            ways += 1
            total -= next
            next -= 8
    return ways

print findLaminae()
