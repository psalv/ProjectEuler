__author__ = 'paulsalvatore57'
# Difficulty: 25%

# QUESTION:

    # A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.
    #
    # There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors:
    # 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.
    #
    # How many composite integers, n < 108, have precisely two, not necessarily distinct, prime factors?

# FINISHED

# WHAT I LEARNED:

    # I have learned in this process that when working with numbers it is invaluable to understand their properties.
    # I did not know that all primes are either of the form (6k - 1) or (6k + 1) for some int k.
    # This provides valuable shortcuts that one can take.

    # Furthermore, I achieved completion of this question by using a recursive binary search technique to iterate through the prime list faster.
    # This shows me that I need to be actively searching for ways to apply the techniques I already have, I don't have to reinvent the wheel.









#Semiprimes are composite primes, numbers that contain at least two prime factors.
    #For instance, 15 has two prime factors, 3 and 5.

#The ten numbers under thirty that have precisely two prime factors are:
    #4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

#We want to know how many numbers under  10**8 have precisely two prime factors.

#What I will do is create a list with all the prime numbers in it from 0 - (10**8)/2, since the largest factor a number cna have is half of it.

#I will then find the modulus of each number from 0 - 10**8 and if there are >2 I will skip the number.

import pickle

#This code is much faster than the prime code I wrote (mine actually may have been the slowest possible).
#What this code takes advantage of is that every prime is of one of two forms: (6k - 1) or (6k + 1) for all natural numbers of k.

def isPrime(n):
    """
    NOT MY CODE
    Returns True if n is a prime number, false if it is not.
    """
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    #w will oscillate between being 2 and 4 which will be added to check both sides of every multiple of six.
        #For instance 5 = 6 - 1 gets two added to it so 7 = 6 + 1
        #Next 7 gets four added to it so 11 = 6*2 - 1, which will then get two added so 13 = 6*2 + 1.
        #Checks to see if any of these primes are factors, if they are not factors than the number must be prime.
    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True



#Once I have all of the primes leading up to (10**8)/2 here are the properties I have been able to ascertain about the composite primes I am looking for:
    #Every prime under one half of the limit will yield a composite prime with two factors (which I will refer to as 2COMs) after multiplication with 2.
        #2COMs += len(primes)
    #If the square of prime < 10**8, it will be a 2COM
    #One prime multiplied by another prime will always yield a 2COM.

    #My challenge now is to find out the number of primes that each prime can be multiplied with and stay underneath 10**8.
    #For instance I know that 2 can be multiplied with every element in the list, so I would add the length of the entire list.
    #3, however, cannot be multiplied by anything below 10**8/3, so I would add the length of the list up to the first term larger than this.
        #To speed this process I believe I can shorten the list as I go.
        #If I do it this way then I will not need to add the 2COMs I listed above because they will be included already.




def BFScomposites(max = 10**8):
    """
    Uses a brute force method to find composites, is not efficient for this problem.
    """
    compCount = 0
    track = []

    for possible in xrange(2, max + 1):

        if possible in track:
            track = track[1:]
            continue

        if isPrime(possible):
            continue

        fact = None

        for factor in xrange(2, possible/3 + 2):

            if fact == factor:
                continue

            if possible%factor == 0 and isPrime(factor) and isPrime(possible/factor):

                if fact == None:
                    fact = possible/factor
                else:
                    continue

        if fact != None:
            print possible, 'Fact:', fact
            compCount += 1
            track += [possible*2,]

    return compCount



def PrimeList(max = 10**8):
    """
    Generates a list of prime numbers up to 1/2 the max, which is the max factor that could be in the max.
    """
    primes = []
    # notPrimes = []
    for i in xrange(2, max/2 + 1):

        if isPrime(i):
            primes += [i,]
            # notPrimes += [i*2,]

        if i%10000 == 0:
            print len(primes), 'i:', i

    pickle.dump(primes, open('Primes up to fifty million', 'wb'))

# print PrimeList()


def countComposites(maxNum = 10**8):
    """
    Takes a premade list of prime numbers.
    Sums and returns the number of primes that each prime can multiply with within the max,
    which giving number of two factor composites within the maxNum
    """
    total = 0
    primes = pickle.load(open('Primes up to fifty million'))
    for prime in primes:

        maxPrime = searchPrimes(prime, primes, maxNum)
        # print maxPrime

        try:
            primes = primes[:primes.index(maxPrime) + 1]
            total += len(primes)
            primes = primes[1:]

        except:
            return total



#I can do a binary search to reduce the amount of time that it takes to find the largest prime,
#with which I can multiply the given prime to still achieve a product under 10**8.

def searchPrimes(prime, primelist, maxNum = 10**8):
    """
    Uses a recursive binary search method,
    Returns the max number in the primelist with which the product with the prime will be less than the maxNum.
    """

    if len(primelist) <= 3:
        maxPrime = None
        for p in primelist:
            if p * prime < maxNum:
                maxPrime = p
        return maxPrime

    if prime * primelist[len(primelist)/2] <= maxNum:
        ans = searchPrimes(prime, primelist[len(primelist)/2:], maxNum)

    else:
        ans = searchPrimes(prime, primelist[:len(primelist)/2], maxNum)

    return ans

# testList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27]
# print searchPrimes(3, testList, 10)




print countComposites()



