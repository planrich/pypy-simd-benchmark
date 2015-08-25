import numpy as np
c = np.ones(10000, dtype='float')
for i in range(0,10000):
    p = np.prod(c)
    assert int(p) == 1
