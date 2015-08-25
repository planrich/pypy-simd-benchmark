import time
import sys
import array

def add(A,B,s):
    i = 0
    while i < s:
        A[i] = A[i] + B[i]
        i += 1

if __name__ == '__main__':
    s = int(sys.argv[1])
    j = int(sys.argv[2])
    a = array.array('d', [0.0]*s)
    b = array.array('d', [1.0]*s)

    for i in range(j//10):
        add(a,b,s)

    t = time.time()
    for i in range(j):
        add(a,b,s)
    print "time:", (time.time()-t)
    
