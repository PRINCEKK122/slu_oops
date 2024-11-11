from lab7 import vector3f


class Vector4D(vector3f):
    def __init__(self, x, y, z, w):
        super().__init__(x, y, z)
        self._w = w

    def getW(self):
        return self._w

    def __add__(self, other):
        result = super().__add__(other)
        w = self._w + other._w
        return Vector4D(result._x, result._y, result._z, w)

    def __mul__(self, scale):
        v3 = super().__mul__(scale)
        if isinstance(scale, int):
            w = self.getW() * scale
            return Vector4D(v3.getX(), v3.getY(), v3.getZ(), w)
        elif isinstance(scale, Vector4D):
            return Vector4D(
                v3.getX(),
                v3.getY(),
                v3.getZ(),
                self._w * scale._w,
            )

    # def __rmul__(self, scale):
    #     return self.__mul__(scale)

    def dotProduct(self, other):
        product = self.__mul__(other)
        return product.getX() + product.getY() + product.getZ() + product.getW()

    def magnitude(self):
        base = pow(self._x, 2) + pow(self._y, 2) + pow(self._z, 2) + pow(self._w, 2)
        return pow(base, 0.5)

    def normalize(self):
        magnitude = self.magnitude()
        return Vector4D(
            self._x / magnitude,
            self._y / magnitude,
            self._z / magnitude,
            self._w / magnitude
        )

    def __str__(self):
        return f"{super().__str__()}, {self.getW()}"


if __name__ == "__main__":
    v1 = Vector4D(3, 1, 4, 2)
    v2 = Vector4D(5, 7, 6, 9)
    v3 = v1 + v2
    print("vector one:", v1)
    print("vector two:", v2)
    print()
    print("vector one magnitude:", v1.magnitude())
    print("vector two magnitude:", v2.magnitude())
    print()
    print("The dot product of the two vectors:", v1.dotProduct(v2))
    print()
    v1_scale = v1 * 3
    v2_scale = v2 * 3
    print("vector one multiplied by 3:", v1_scale)
    print("vector two multiplied by 3:", v2_scale)
    print()
    vector_sum = v1_scale + v2_scale
    print("vector sum:", v1_scale + v2_scale)
    print("normalized vector sum", vector_sum.normalize())


    # print(v3)
