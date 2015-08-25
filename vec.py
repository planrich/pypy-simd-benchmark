
import array

class vec(object):
    @staticmethod
    def sized(size, type='d'):
        return vec([0] * size, type)

    @staticmethod
    def of(content, type='d'):
        return vec(content, type)

    def __init__(self, content, type='d'):
        self.size = len(content)
        self.type = type
        self.array = array.array(type, content)

    def __add__(self, other):
        return self.add(other)

    def add(self, other, out=None):
        assert isinstance(other, vec)
        result = out
        if result is None:
            result = vec([0] * self.size, self.type)
        if self.size != other.size:
            raise Exception("size mismatch! %d != %d" % (self.size,other.size))
        i = 0
        while i < self.size:
            result.array[i] = self.array[i] + other.array[i]
            i += 1
        return result

    def __sub__(self, other):
        return self.sub(other)

    def sub(self, other, out=None):
        assert isinstance(other, vec)
        result = out
        if result is None:
            result = vec([0] * self.size, self.type)
        if self.size != other.size:
            raise Exception("size mismatch! %d != %d" % (self.size,other.size))
        i = 0
        while i < self.size:
            result.array[i] = self.array[i] - other.array[i]
            i += 1
        return result

    def __mul__(self, other):
        return self.mul(other)

    def mul(self, other, out=None):
        assert isinstance(other, vec)
        result = out
        if result is None:
            result = vec([0] * self.size, self.type)
        if self.size != other.size:
            raise Exception("size mismatch! %d != %d" % (self.size,other.size))
        i = 0
        while i < self.size:
            result.array[i] = self.array[i] * other.array[i]
            i += 1
        return result
