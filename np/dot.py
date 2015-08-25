try:
    import _numpypy.multiarray as np
except ImportError:
    import numpy as np

def main(m,v,o):
    for i in range(0,2000):
        np.dot(m,v,out=o)

if __name__ == '__main__':
    import sys
    s = int(sys.argv[1])
    m = np.array([1] * (s*s), dtype='float').reshape((s,s))
    v = np.array([0] * s, dtype='float')
    o = np.array([0] * s, dtype='float')


    import time
    s = time.time()
    main(m,v,o)
    e = time.time()
    print "time: %s" % (e-s)


