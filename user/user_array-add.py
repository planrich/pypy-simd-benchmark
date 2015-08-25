import time
import sys
import array

def f(v,w,s):
    i = 0
    while i < s:
        w[i] = w[i] + v[i]
        i += 1

def run(v,w,j,s):
    for i in range(j):
        f(v,w,s)

if __name__ == '__main__':
    s = int(sys.argv[1])
    j = int(sys.argv[2])
    w = array.array('d', [0.0]*s)
    v = array.array('d', [1.0]*s)

    b = time.time()
    run(w,v,j,s)
    e = time.time()
    print "time:", (e-b)
    
