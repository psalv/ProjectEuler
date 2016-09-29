__author__ = 'paulsalvatore57'
# Difficulty: 15%

# QUESTION:

    # By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
    # By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers,
    # yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
    # Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

#FINISHED

# WHAT I LEARNED:

    # I got the answer by pure brute force: (121313, ['222323', '323333', '424343', '525353', '626363', '828383', '929393'])
    # I was gearing up to try and speed my code up but I guess it wasn't necessary in this situation.









#Find the smallest digit for which replacing any of the digits with the same digit yields eight prime possibilities:
    #Ex 1: *3 has six possibilities: 13, 23, 43, 53, 73, 83.
    #Ex 2: 56**3 hss seven possibilities: 56003, 56113, 56333, 56443, 56663, 56773, 56993.

    #The digits replaced need not be adjacent.

#Things that I know:
    #Primes must end in 1, 3, 7, or 9.
    #This greatly reduces how many iterations I need to do, since the last digit will always be one of these numbers.

#Helpful code:
    #A code that returns a list containing every possible star combination,
        #What will be input is: the end digit, the length of the digit.
    #Code the finds if a number is prime.


def isPrime(number):
    for i in xrange(2, number / 2 + 2):
        if number%i == 0:
            return False
    return True




#My over-complication of the problem:
    # I need a a list of numbers that end in 1, 3, 7, or 9 and are the same number of digits long as the input.
    # The list will have every possibility of r (replace) and f (fixed) in the remaining digits, besides every digit fixed.
        # So for two digits I will have: [r1, r3, r7, r9]
        # For three digits I will have: [[rr1, rf1, fr1], [rr3, rf3, fr3], [rr7, rf7, fr7], [rr9, rf9, fr9]]

    #Once I find a prime, I am replacing any digits that are duplicates,
    #However I may not replace the last digit because I will never get  that way (waste of time).




#Very crude brute force algorithm:
def primePerm(max, p = 8):

    for num in xrange(111000, max):

        if num%1000 == 0:
            print num

        if isPrime(num):

            possible = str(num)[:-1]
            possibleEnd = str(num)[-1]

            for letter in possible:
                primes = 1
                pr = []

                for n in xrange(10):

                    if (10 - n) - (p - primes) < 0:
                        continue

                    if str(n) != letter:
                        new = possible.replace(letter, str(n)) + possibleEnd
                    else:
                        continue

                    if new[0] == '0':
                        continue

                    if isPrime(int(new)):
                        primes += 1
                        pr += [new,]
                        if primes == p:
                            return num, pr


        # print 'Primes:', primes, 'Number:', num

#The answer is over 100000, which begins to take a long time with this code.

print primePerm(200000)