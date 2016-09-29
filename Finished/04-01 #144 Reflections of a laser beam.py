__author__ = 'paulsalvatore57'
# Difficulty: 50%

# QUESTION:

    # In laser physics, a "white cell" is a mirror system that acts as a delay line for the laser beam.
    # The beam enters the cell, bounces around on the mirrors, and eventually works its way back out.
    #
    # The specific white cell we will be considering is an ellipse with the equation 4x2 + y2 = 100
    #
    # The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing, allowing the light to enter
    # and exit through the hole.

#FINISHED

# WHAT I LEARNED:

    # This problem had a high difficulty but was actually one of the easier problems I've done.
    # I think the gif in the question and the concept of lasers and angles off-put people, but the question was actually relatively straightforward.
    # This provides a lesson in attempting seemingly difficult problems and deciding their difficulty for myself.
    # When I broke the problem down into it's components there were no surprises, and by careful algebra and working out angles I got the answer.
    # So a main take-away from this problem is to give hard problems a shot, carefully breaking them down into more manageable tasks - divide and conquer.

    # As an interesting aside from the forums a relevant question based on this is how long the light stays in the chamber.
    # To answer this question I would need to keep a running tally of the distance it travels and divide by the speed of light (c).







#An ellipse is given by the equation: 4*(x**2) + (y**2) = 100

#A section is missing in the ellipse from -0.1 <= x <= 0.1

#A beam enters the ellipse at (0, 10.1) and impacts the ellipse at (1.4, -9,6)

#Recall that angle of incidence equals angle of reflection, and angle of incidence can be figured using the slope of the tangent line.
    #For the given ellipse, the slope at any given point is given by: m = -4x/y

#The question wants to know how many times the beam hits the internal surface until it leaves.


#These are attributes of the ellipse in the form x**2/a**2 + y**2/b**2 = 1:
    # a, b = 5, 10



#1) Compute an angle of the tangent with respect to the x axis
#2) Compute an angle of the the beam with respect to the x axis
#3) Use the "z-pattern" to compute the angle of incidence, and therefore the angle of reflection
    #Angle of incidence is equivalent to 2) - 1)
#4) Find where the equation of the ellipse and the equation of the beam intersect
#5) Repeat this pattern until the ellipse and the beam intercept at the hole (NOTE: the hole is only at the top)



import math



def angleFromVector(x, y):
    """Returns the angle that the vector [x, y] forms with the x axis."""
    deg = math.degrees((math.atan(float(y)/x)))
    if deg < 0:
        return 180 + deg
    else:
        return deg



def findB(x, y):
    """Returns the b value of the line representing the tangent at the point x, y."""
    slope = -4.0*x/y
    return y - (slope*x)



def buildVector(start, end):
    """Converts a start and end point into a vector."""
    return [end[0] - start[0], end[1] - start[1]]



def QuadFormula(a, b, c):
    """
    Because I never want to have to type this shit into a calculator again.
    """
    if (b**2 - 4*a*c) < 0:
        answer = str(-b/(2.0*a)) + " +/- " + str((-(b**2.0 - 4.0*a*c))**0.5/(2.0*a)) + " * i"
        print '\nAnswer is a complex number:', answer, '\n                Under root:', b**2.0 - 4.0*a*c
        return None
    answer1 = (-b + (b**2.0 - 4.0*a*c)**0.5)/(2.0*a)
    answer2 = (-b - (b**2.0 - 4.0*a*c)**0.5)/(2.0*a)
    return [answer1, answer2]



def findIntersection(angle, start):
    """Finds the equation of the line at the starting point start with a given angle to the positive x axis.
    Returns the point of intersection."""

    m = math.tan(math.radians(angle))
    b = m*(-start[0]) + start[1]


    # print '\nStarting angle:   ', angle
    # print 'Starting position:', start
    # print 'Calculated slope: ', m


    possibleX = QuadFormula(m**2 + 4, 2*b*m, b**2 - 100)

    if abs(possibleX[0] - start[0]) < 0.00001:
        x = possibleX[1]
    else:
        x = possibleX[0]

    y = m*x + b

    print '\nFound equation: y = ' + str(m) + '*x + ' + str(b)
    return [x, y]


def main():
    """Finds when the laser beam will exit the narrow slit."""
    start = [0, 10.1]
    end = [1.4, -9.6]
    count = 0
    while True:

        if -0.01 <= end[0] <= 0.01 and end[1] > 0:
            print '\nNumber of reflections:', count
            return count
        count += 1
        # print count

        vectorBeam = buildVector(start, end)
        vectorTangent = buildVector([0, findB(end[0], end[1])], end)

        beamAngle = angleFromVector(vectorBeam[0], vectorBeam[1])
        tangentAngle =angleFromVector(vectorTangent[0], vectorTangent[1])

        incident = beamAngle - tangentAngle

        start = end[:]

        newAngle = 180 - incident + tangentAngle

        end = findIntersection(newAngle, start)
        # print 'New point of intersection:', end



main()


