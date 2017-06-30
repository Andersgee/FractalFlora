import numpy as np
from matplotlib import pyplot as plt

def factorial(n, a, p0=np.array([0,0]), p1=np.array([0,1])):
    if n < 1:
        return
    else:
        plt.plot([p0[0], p1[0]], [p0[1], p1[1]])
        p2 = np.dot((p1-p0), rotMat(a)) + p1
        factorial(n-1, pi/7, p1, p2)
        factorial(n-1, -pi/7, p1, p2)

def rotMat(a):
    return np.array([[np.cos(a), np.sin(a)], [-np.sin(a),  np.cos(a)]])

if __name__ == '__main__':
    pi=3.14159
    factorial(6, a=-pi/7)
    plt.show()
