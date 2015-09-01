import time
import sys
import array

# show start
def py_add(A,B,size):
    i = 0
    while i < size:
        A[i] = A[i] + B[i]
        i += 1
# show stop

if __name__ == '__main__':
    s = int(sys.argv[1])
    j = int(sys.argv[2])
    a = array.array('d', [0.0]*s)
    b = array.array('d', [1.0]*s)

    for i in range(j//10):
        py_add(a,b,s)

    t = time.time()
    for i in range(j):
        py_add(a,b,s)
    print "time:", (time.time()-t)
    
