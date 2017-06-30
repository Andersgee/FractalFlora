import numpy as np
from matplotlib import pyplot as plt
import math


def factorial(n, a, c, p0=np.array([0, 0]), p1=np.array([0, 1])):
    if n < 1:
        return
    else:
        plt.plot([p0[0], p1[0]], [p0[1], p1[1]], color=mycolor(n), linewidth=6*n/N)
        p2 = np.dot((p1-p0)*c, rotMat(a)) + p1
        factorial(n-1, 0, c*0.99, p1, p2)
        if ~ n % 3:
            factorial(n-2, angle, c*0.8, p1, p2)
        if ~ n % 2:
            factorial(n-2, -angle, c*0.8, p1, p2)


def rotMat(a):
    return np.array([[np.cos(a), np.sin(a)], [-np.sin(a),  np.cos(a)]])


def mycolor(n):
    brown = np.array([89/255, 56/255, 7/255])
    green = np.array([23/255, 232/255, 40/255])
    return brown*math.sqrt((n/N)) + (green/n)**1.1


if __name__ == '__main__':
    N = 16
    angle = 25*math.pi/180
    factorial(N, 0, 1)
    plt.axes().set_aspect('equal')
    plt.show()
