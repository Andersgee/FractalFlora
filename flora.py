import numpy as np
from matplotlib import pyplot as plt
from math import pi

def factorial(n, a, p0=np.array([0,0]), p1=np.array([0,1])):
    if n < 1:
        return
    else:
        plt.plot([p0[0], p1[0]], [p0[1], p1[1]])
        p2 = np.dot((p1-p0), rotMat(a)) + p1
        factorial(n-1, angle, p1, p2)
        factorial(n-1, -angle, p1, p2)

def rotMat(a):
    return np.array([[np.cos(a), np.sin(a)], [-np.sin(a),  np.cos(a)]])

if __name__ == '__main__':
    angle=25*pi/180
    factorial(6, -angle)
    plt.show()
