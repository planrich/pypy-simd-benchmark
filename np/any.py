try:
    import _numpypy.multiarray as np
except ImportError:
    import numpy as np

# show start
def main(v,i):
    for _ in range(i):
        a = v.any()
        assert not a
# show stop

if __name__ == '__main__':
    import sys
    s = int(sys.argv[1])
    I = int(sys.argv[2])
    V = np.array([0] * s)

    main(V, I//10)

    import time
    s = time.time()
    main(V,I)
    print "time: %s" % (time.time()-s)
