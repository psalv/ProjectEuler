__author__ = 'paulsalvatore57'
#All are 5% difficulty.

#Something I learned from these comes from the primes list up to 50 million that I generated for #187.
#Although this took long to generate, I have now used it multiple times, saving me a significant amount of work.

#In this I can see that there are circumstances where taking longer to get set up will be useful in the long run.




#1 FINISHED
def multiples3and5():
    """Sums all multiples of 3 or 5 up to 1000"""
    total = 0
    for i in xrange(1000):
        if i%3 == 0 or i%5 == 0:
            total += i
    print total
# multiples3and5()



#2 FINISHED
def fib(last, current):
    return last + current

def evenFib():
    """Computes fibonacci numbers and sums the even ones"""
    total = 0
    last = 1
    current = 1
    while current < 4*10**6:
        if current%2 == 0:
            total += current
        next = fib(last, current)
        last, current = current, next
    print total
# evenFib()



#3 FINISHED
def isPrime(n):
    """Returns True if n is prime"""
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i, w = 5, 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def pFactors(num = 600851475143):
    """Finds the largest prime number that is a factor of num"""
    for i in xrange(2, num/2):
        pos = float(num)/i
        if pos % 1 == 0:
            print pos
            if isPrime(pos):
                return pos
# print pFactors()



#4 FINISHED
def isPalin(num):
    """Returns true if num is a palindrome"""
    num = str(num)
    if len(num) <= 1:
        return True
    if num[0] == num[-1]:
        ans = isPalin(num[1:-1])
    else:
        ans = False
    return ans

def bruteFind():
    """Iterates through all products of three digits numbers, returns the largest palindrome"""
    ans = None
    for i in xrange(100, 1000):
        for j in xrange(100, 1000):
            if isPalin(i*j):
                if ans == None:
                    ans = i*j
                elif ans < i*j:
                    ans = i*j
        print i
    print ans
# bruteFind()



#5 FINISHED
def areFactors(n):
    """Returns true if all of the numbers from 1 - 20 are factors"""
    for i in xrange(2, 21):
        if (float(n)/i)%1 != 0:
            return False
    return True

def smallestOnetoTwenty():
    """Iterates through every possible number, returns one that has 1-20 as factors"""
    n = 20
    # n = 232700000
    while True:
        if areFactors(n):
            return n
        else:
            n += 20
            if n%100000 == 0:
                print n
# print smallestOnetoTwenty()



#6 FINISHED
def difNatural():
    """Returns the difference between (the sum of the first 100 natural numbers)**2 and the sum of the first one hundred square numbers."""
    sumNumSq = 0
    sumNum = 0
    for i in xrange(1, 101):
        sumNumSq += i**2
        sumNum += i
    print sumNum**2 - sumNumSq
# difNatural()



#7 FINISHED
# import pickle
def find10001():
    """Uses a precomputed list of 50 million primes to find the 100001st"""
    primes = pickle.load(open('/Users/paulsalvatore57/PycharmProjects/General/Project Euler/Finished/Primes up to fifty million'))
    print primes[10000]
# find10001()



#8 FINISHED
def readLargeNum():
    """Reads text file of large numbers, makes into a single string"""
    numFile = open('longnumber.txt', 'r')
    num = ''
    for line in numFile:
        num += line[:-1]
    return num

def product(string):
    """Returns the product of each digit in a string of numbers"""
    total = int(string[0])
    for i in string[1:]:
        total *= int(i)
    return total

def greatestProduct():
    """Iterates through every 13 digit frame in the number, returns largest product of digits"""
    num = readLargeNum()
    n, m = 0, 13
    highest = None

    while m <= len(num) + 1:
        pos = product(num[n:m])
        print pos
        if highest == None:
            highest = pos
        elif pos > highest:
            highest = pos
        m += 1
        n += 1

    return highest
# print greatestProduct()



#9 FINISHED
#a**2 + b**2 = c**2, a, b and c are a natural numbers.
#a + b + c = 1000

def findTriplets():
    """Finds three numbers wherein a**2 + b**2 == c**2 and a + b + c == 1000"""
    a = 3
    b = 4
    while True:
        c = (a**2 + b**2)**0.5
        if c%1 == 0 and a + b + c == 1000:
            return a*b*c

        if a + b > 1000*(2.0/3):
            a += 1
            b = a + 1
        else:
            b += 1
# print findTriplets()



#10 FINISHED
# import pickle
def sumPrimes():
    """Sums all primes under two million"""
    primes = pickle.load(open('/Users/paulsalvatore57/PycharmProjects/General/Project Euler/Finished/Primes up to fifty million'))
    summ = 0
    for i in xrange(len(primes)):
        if primes[i] < 2*10**6:
            summ += primes[i]
        else:
            break
    print summ
# sumPrimes()



