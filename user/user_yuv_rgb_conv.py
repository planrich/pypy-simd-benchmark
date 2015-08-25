
from vec import vec

def conv_yuv_to_rgb(pixels, pixels_rgb):
    assert isinstance(pixels, vec)
    assert isinstance(pixels_rgb, vec)
    i = 0
    while i < len(pixels.array):
        y = pixels.array[i]
        u = pixels.array[i+1]
        v = pixels.array[i+2]

        r = y + (1.370705 * (v-128))
        b = y + (1.732446 * (u-128))
        g = y - (0.698001 * (v-128)) - (0.337633 * (u-128))

        i += 3

if __name__ == "__main__":
    yuv = vec([0.5,0.4,0.3] * 2048 * 1440)
    rgb = vec([0.5,0.4,0.3] * 2048 * 1440)
    for i in range(10):
        conv_yuv_to_rgb(yuv,rgb)
    import time
    t = time.time()
    for i in range(300):
        conv_yuv_to_rgb(yuv,rgb)
    print "took", time.time() - t
