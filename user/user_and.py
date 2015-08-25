import sys
sys.setcheckinterval(10000000)
def main():
    import _numpypy.multiarray as np
    a = np.array([1]*1499, dtype='int32')
    b = np.array([0]*1499, dtype='int32')
    c = a & b
    i = 0
    for j in range(1499):
        i += c[j]
    return i
print main()
