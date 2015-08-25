try:
    import _numpypy.multiarray as np
except ImportError:
    import numpy as np

def main(v,o):
    for i in range(0,100000):
        v * 2

if __name__ == '__main__':
    import sys
    s = int(sys.argv[1])
    v = np.array([1] * s, dtype='float')


    import time
    s = time.time()
    main(v,None)
    e = time.time()
    print "time: %s" % (e-s)


