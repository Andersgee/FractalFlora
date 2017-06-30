import numpy as np
from matplotlib import pyplot as plt
from math import pi

def factorial(n, a, p0=np.array([0,0]), p1=np.array([0,1])):
    if n < 1:
        return
    else:
        plt.plot([p0[0], p1[0]], [p0[1], p1[1]])
        p2 = np.dot((p1-p0), rotMat(a)) + p1
        factorial(n-2, angle*1.5, p1, p2)
        factorial(n-1, -angle/3, p1, p2)
        if ~n%3:
            factorial(n-2, angle/2, p1, p2)

def rotMat(a):
    return np.array([[np.cos(a), np.sin(a)], [-np.sin(a),  np.cos(a)]])

if __name__ == '__main__':
    angle=25*pi/180
    factorial(10, -angle)
    plt.show()
