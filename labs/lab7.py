class vector3f:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    # getters
    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getZ(self):
        return self._z

    # setters
    def setX(self, value):
        self._x = value

    def setY(self, value):
        self._y = value

    def setZ(self, value):
        self._z = value

    def __add__(self, other):
        return vector3f(
            self._x + other.getX(), self._y + other.getY(), self._z + other.getZ()
        )

    def __mul__(self, scale):
        if isinstance(scale, int):
            return vector3f(self._x * scale, self._y * scale, self._z * scale)
        elif isinstance(scale, vector3f):
            return vector3f(self._x * scale._x, self._y * scale._y, self._z * scale._z)

    def __rmul__(self, scale):
        return self.__mul__(scale)

    def magnitude(self):
        base = pow(self._x, 2) + pow(self._y, 2) + pow(self._z, 2)
        return pow(base, 0.5)

    def dotProduct(self, other):
        product = self.__mul__(other)
        return product.getX() + product.getY() + product.getZ()

    def __str__(self):
        return f"{self._x}, {self._y}, {self._z}"

    def normalize(self):
        return vector3f(
            self._x / self.magnitude(),
            self._y / self.magnitude(),
            self._z / self.magnitude(),
        )

if __name__ == "__main__":
    vector_one = vector3f(3, 1, 2)
    vector_two = vector3f(4, 5, 6)

    print(vector_one.magnitude())
    print(vector_two.magnitude())
    product = vector_one * vector_two
    print(vector_one.dotProduct(vector_two))
    add_one = 3 * vector_one
    print(add_one)
    add_two = 3 * vector_two
    print(add_two)
    result_vector = add_one + add_two
    print(result_vector.normalize().magnitude())
    # print(result_vector)
