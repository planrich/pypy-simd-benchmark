
import array
import sys
import time

# show start
def conv_rgb_to_yuv(R,G,B,Y,U,V):
    # see https://en.wikipedia.org/wiki/YUV
    # a naive implementation
    i = 0
    while i < len(R):
        Y[i] = R[i] * 0.299 + G[i] * 0.587 + B[i] * 0.114
        U[i] = -0.147 * R[i] + -0.289 + G[i] + 0.436 * B[i]
        V[i] = 0.615 * R[i] * -0.515 + G[i] * 0.100 + B[i]
        i += 1
# show stop

if __name__ == "__main__":
    w, h = [int(x) for x in sys.argv[1].split(",")]
    I = int(sys.argv[2])

    y = array.array('d', [0] * w * h)
    u = array.array('d', [0] * w * h)
    v = array.array('d', [0] * w * h)
    r = array.array('d', [0.1] * w * h)
    g = array.array('d', [0.7] * w * h)
    b = array.array('d', [0.2] * w * h)
    for i in range(10):
        conv_rgb_to_yuv(r,g,b,y,u,v)
    t = time.time()
    for i in range(I):
        conv_rgb_to_yuv(r,g,b,y,u,v)
    print "time: %s" % (time.time() - t)
