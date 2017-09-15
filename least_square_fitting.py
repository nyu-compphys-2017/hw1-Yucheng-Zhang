"""
Code for exercise 3.8 Least-squares fitting and the photoelectric effect.
Python 3.6.1 built in Anaconda.
"""

import numpy as np
from pylab import plot, show, xlabel, ylabel, savefig

if __name__ == "__main__":
    data = np.loadtxt("millikan.txt", float)
    X = data[:, 0]
    Y = data[:, 1]
    N = len(X)
    Ex = 1/N * sum(X)
    Ey = 1/N * sum(Y)
    Exx = 1/N * sum([x**2 for x in X])
    Exy = 1/N * sum([x*y for x, y in zip(X, Y)])
    m = (Exy - Ex * Ey) / (Exx - Ex**2)
    c = (Exx * Ey - Ex * Exy) / (Exx - Ex**2)
    print("m = ", m, "c = ", c)
    line = [m * x + c for x in X]
    plot(X, Y, "k.")
    plot(X, line)
    xlabel("x")
    ylabel("y")
    savefig("millikan.pdf", bbox_inches="tight")
    e = 1.602e-19
    print("h = ", m * e)
