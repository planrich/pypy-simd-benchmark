import time
import sys
import array

# show start
def py_sum(v,w,s):
    i = 0
    x = 0
    while i < s:
        x += v[i]
        i += 1
# show stop

def run(v,w,j,s):
    for i in range(j):
        v = py_sum(v,w,s)
        assert v == 2.0*s

if __name__ == '__main__':
    s = int(sys.argv[1])
    j = int(sys.argv[2])
    v = array.array('d', [2.0]*s)

    t = time.time()
    run(v,None,j,s)
    print "time: %s" % (time.time() - t)
    
