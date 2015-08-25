try:
    import _numpypy.multiarray as np
    import _numpypy.umath as ufunc
except ImportError:
    import numpy as np
    ufunc = np

import random
import math

def bmu(grid, x, y, sel, tmp):
    """ calc the best matching unit, the one that has the smallest euclidean dist """
    min_pos = 0
    min_dist = float(10000)
    for i in range(x*y):
        entry = grid[i]
        ufunc.subtract(sel, entry, out=tmp)
        # euclidean dist
        ufunc.multiply(tmp, tmp, out=tmp)
        d = ufunc.sqrt(tmp.sum())
        if d < min_dist:
            min_dist = d
            min_pos = i
    return min_pos

def adjust(G, X, Y, pos, hci, alpha, selection, tmp):
    m = G[pos]
    # m = m + alpha * (hci) * (m - sel)
    ufunc.subtract(m, selection, out=tmp)
    ufunc.multiply(tmp, alpha, out=tmp)
    ufunc.add(m, tmp, out=m)

    G[pos] = m

def som(D,I,X,Y,G,DATA,tmp):
    r = random.Random()
    r.seed(0)
    for j in xrange(I):
        i = r.randint(0,49)
        selection = DATA[i]
        pos = bmu(G, X, Y, selection, tmp)
        alpha = float(j)/I
        hci = 1 # not calculated for this bench
        adjust(G,X,Y,pos,hci,alpha,selection,tmp)

    return None

def setup(D,I):
    X = 10
    Y = 10
    G = [np.array([1] * D) for i in range(X*Y)]
    DATA = [np.array([2] * D) for i in range(50)]
    tmp = np.empty(D)
    return D,I,X,Y,G,DATA,tmp


if __name__ == "__main__":
    import sys
    import time
    I = int(sys.argv[1])
    args = setup(int(sys.argv[1]), I)
    s = time.time()
    som(*args)
    e = time.time()
    print "time:", (e-s)
