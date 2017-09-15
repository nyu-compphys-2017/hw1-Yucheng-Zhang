"""
Code for exercise 3.7 The Mandelbrot set.
Python 3.6.1 built in Anaconda.
"""

import numpy as np
from pylab import plot, show, imshow, gray, xlabel, ylabel, savefig

def z_next(z, c):
    "The iteration equation."
    return [z[0]**2 - z[1]**2 + c[0], 2*z[0]*z[1] + c[1]]

if __name__ == "__main__":
    N = 1000
    NUM_ITER = 100
    X = np.linspace(-2, 2, N)
    Y = np.linspace(-2, 2, N)
    M_Set = []
    M_Map = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            z, c = [0, 0], [X[i], Y[j]]
            for k in range(NUM_ITER):
                z = z_next(z, c)
                if z[0]**2 + z[1]**2 > 4:
                    M_Map[j][i] = k + 1
                    break
            else:
                M_Set.append(c)
                #M_Map[j][i] = 0
                M_Map[j][i] = NUM_ITER # Attention to the indices

    #imshow(M_Map, origin="lower", extent=[-2, 2, -2, 2])
    #gray()
    Log_M_Map = np.log(M_Map)
    imshow(Log_M_Map, origin="lower", extent=[-2, 2, -2, 2])
    xlabel("x")
    ylabel("y")
    savefig("num_it_log.pdf", dpi=2000, bbox_inches='tight')
