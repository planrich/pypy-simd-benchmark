import sys
import random
import array

def fir(B,X,n):
    # see https://en.wikipedia.org/wiki/Finite_impulse_response
    i = 0
    res = 0
    while i < n:
        b = B[i]
        x = X[i]
        a = x*b
        res += a
        del b,x,a
        i += 1
    return res

if __name__ == "__main__":
    l = int(sys.argv[1])
    I = int(sys.argv[2])

    random.seed(0)
    # fake the input
    B = array.array('d', [random.random() for _ in range(l)])
    X = array.array('d', [random.random() * 0.5 for _ in range(l)])
    for i in range(I//10):
        fir(B,X,len(X))
    import time
    t = time.time()
    for i in range(I):
        fir(B,X,len(X))
    print "took", time.time() - t
