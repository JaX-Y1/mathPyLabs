from sympy import *
import numpy as np
import math as math

def part1A():
    top= 4*(log(1.29,10)+log(11.1,math.e))
    bottom = 2027 - 12**3
    print((top/bottom).evalf())
def part1B():
    approx = sin((11*pi)/12)*cos(rad(75)) + cos(rad(165))*sin((5*pi)/12)
    print(f"Appoximation: {approx.evalf()}")
    exact = S("sin((11*pi)/12)*cos(rad(75)) + cos(rad(165))*sin((5*pi)/12)")
    print(f"Exact: {exact}")
def part2A():
    x=symbols("x")
    identity1 = sin(x)**2
    identity2 = S("(1/2)*(1-cos(2*x))")
    print("when x=pi/3")
    print(identity1.subs(x,(pi/3)))
    print(identity2.subs(x,(pi/3)))   
def part2B():
    x=symbols("x")
    identity1 = sin(x)**2
    identity2 = S("(1/2)*(1-cos(2*x))")
    print("when x=2.13")
    print(identity1.subs(x,(2.13)))
    print(identity2.subs(x,(2.13)))
def part3A():
    a= np.array([2,3])
    b = np.array([-1,5])
    print(f"a+b: {a+b}")
    print(f"a-b: {a-b}")
    print(f"3a-5b: {3*a-5*b}")
def part3B():
    a= np.array([2,3])
    angle = atan(a[1]/a[0])
    print(f"Angle: {angle} radians")
def part3C():
    a= np.array([2,3])
    b = np.array([-1,5])
    c = 3*a - 5*b
    cMag = sqrt(np.dot(c,c))
    print(f"Unit vector of 3a-5b: {(1/cMag)*c}")
def part4A():
    f = np.array([5,9])
    print(f"Magnitude of force vector: {sqrt(np.dot(f,f))}")
def part4B():
    pointB = np.array([5,10])
    pointA = np.array([3,4])
    d = pointB-pointA
    print(f"Displacement vector: {d}")
def part4C():
    pointB = np.array([5,10])
    pointA = np.array([3,4])
    d = pointB-pointA
    dMag = sqrt(np.dot(d,d))
    print(f"Magnitude of displacement vector: {dMag}")
def part4D():
    #Work = dot product of force and displacement vector
    f = np.array([5,9])
    d = np.array([2,6])
    Work = np.dot(f,d)
    print(f"Work: {Work}")
def part4E():
    #Cosine of thhe angle between two vectors is the dot product of the two vectors
    #divided by the product of their magnitudes
    f = np.array([5,9])
    d = np.array([2,6])
    fMag = sqrt(np.dot(f,f))
    dMag = sqrt(np.dot(d,d))
    tophalf = np.dot(f,d)
    bottomhalf = fMag * dMag
    cosAngle = tophalf/bottomhalf
    print(f"The cosine of the angle: {cosAngle}")
def part4F():
    cosAngle = (16*sqrt(265))/265
    #given as a float because exact calculation isn't all too helpful
    angle = acos(cosAngle).evalf()
    print(f"Angle between force and displacement vectors: {angle} radians") 
part4F()