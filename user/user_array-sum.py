import time
import sys
import array

def f(v,w,s):
    i = 0
    x = 0
    while i < s:
        x += v[i]
        i += 1
    assert x == 2.0*s

def run(v,w,j,s):
    for i in range(j):
        f(v,w,s)

if __name__ == '__main__':
    s = int(sys.argv[1])
    j = int(sys.argv[2])
    v = array.array('d', [2.0]*s)

    b = time.time()
    run(v,None,j,s)
    e = time.time()
    print "time:", (e-b)
    
