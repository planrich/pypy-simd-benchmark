try:
    import _numpypy.multiarray as np
except ImportError:
    import numpy as np

# show start
def numpy_any(V,count):
    # V contains only 0s
    for _ in range(count):
        a = V.any()
        assert not a
# show stop

if __name__ == '__main__':
    import sys
    s = int(sys.argv[1])
    I = int(sys.argv[2])
    V = np.array([0] * s)

    numpy_any(V, I//10)

    import time
    s = time.time()
    numpy_any(V,I)
    print "time: %s" % (time.time()-s)
