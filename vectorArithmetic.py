import math
import numbers


# we will use syntax return self.__class__(definition) for
# operator overloading in this class so that inherited methods create
# objects of the correct subclass


def vectorMethod(func):
    def decorated(self, other, *args, **kargs):
        if isinstance(other, Vector):
            return func(self, other, *args, **kargs)
        elif isinstance(other, complex):
            return func(self, Vector(x=other.real, y=other.imag), *args, **kargs)
        else:
            return NotImplemented
    return decorated


def scalarMethod(func):
    def decorated(self, other, *args, **kargs):
        if isinstance(other, Vector):
            return func(self, other, *args, **kargs)
        elif isinstance(other, (int, float)):
            return func(self, other, *args, **kargs)
        else:
            return NotImplemented
    return decorated


class Vector:
    absTol = 1e-05
    relTol = 1e-05

    def __init__(self, x=None, y=None, θ=None, magnitude=None):
        if (not x is None) and (not y is None):
            if (not θ is None) or (not magnitude is None):
                raise TypeError("if x and y are specified neither θ nor magnitude may be specified.")
            self.x = x
            self.y = y
            self.magnitude = (x * x + y * y) ** .5
            if x == 0:
                if y > 0:
                    self.θ = math.pi / 2
                else:
                    self.θ = 3 * math.pi / 2
            else:
                self.θ = math.atan(y / x) % (2 * math.pi)
            if x < 0:
                self.θ += math.pi
                self.θ = self.θ % (2 * math.pi)

        elif (not θ is None) and (not magnitude is None):
            if (not x is None) or (not y is None):
                raise TypeError("if θ and magnitude are specified neither x nor y may be specified.")
            self.magnitude = magnitude
            self.θ = θ % (2 * math.pi)
            self.x = magnitude * math.cos(θ)
            self.y = magnitude * math.sin(θ)
        else:
            raise TypeError("x and y or θ and magnitude should be specified")

    # <editor-fold desc="Algebraic Operators">
    # <editor-fold desc="Addition Subtraction Negation">
    @scalarMethod
    def __add__(self, other):
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
        elif isinstance(other, numbers.Number):
            x = self.x + other
            y = self.y
        return self.__class__(x=x, y=y)

    @scalarMethod
    def __sub__(self, other):
        if isinstance(other, Vector):
            x = self.x - other.x
            y = self.y - other.y
        elif isinstance(other, numbers.Number):
            x = self.x - other
            y = self.y
        return self.__class__(x=x, y=y)

    def __neg__(self):
        return self.__class__(x=-self.x, y=-self.y)
    # </editor-fold>

    # <editor-fold desc="Mutiplication Division">
    @scalarMethod
    def __mul__(self, other):
        if isinstance(other, Vector):
            magnitude = self.magnitude * other.magnitude
            θ = self.θ + other.θ
        elif isinstance(other, numbers.Number):
            magnitude = self.magnitude * other
            θ = self.θ
        return self.__class__(magnitude=magnitude, θ=θ)

    @scalarMethod
    def __truediv__(self, other):
        if isinstance(other, Vector):
            magnitude = self.magnitude / other.magnitude
            θ = self.θ - other.θ
        elif isinstance(other, numbers.Number):
            magnitude = self.magnitude / other
            θ = self.θ
        return self.__class__(magnitude=magnitude, θ=θ)
    # </editor-fold>

    # <editor-fold desc="Exponentiation Natural Logarithm">
    @scalarMethod
    def __pow__(self, other):
        if isinstance(other, Vector):
            magnitude = self.magnitude ** other.magnitude
            θ = self.θ * (other.θ - 1) - other.θ
        elif isinstance(other, numbers.Number):
            magnitude = self.magnitude ** other
            θ = self.θ * other
        return self.__class__(magnitude=magnitude, θ=θ)

    def ln(self):
        # LN(W) = ln(|W|) < - θW
        if self.magnitude == 0:
            return NotImplemented
        magnitude = math.log(self.magnitude)
        θ = - self.θ
        return self.__class__(magnitude = magnitude, θ = θ)
    # </editor-fold>
    # </editor-fold>

    # <editor-fold desc="Comparison Operators">
    def __bool__(self):
        return self.magnitude > 0

    def __abs__(self):
        return self.magnitude

    @scalarMethod
    def __eq__(self, other):
        if isinstance(other, Vector):
            absTol = 1e-05
            relTol = 1e-05
            return math.isclose(self.magnitude, other.magnitude, rel_tol=relTol, abs_tol=absTol)
        elif isinstance(other, numbers.Number):
            return (self.x == other) and self.y == 0

    @vectorMethod
    def __lt__(self, other):
        return self.magnitude < other.magnitude

    @vectorMethod
    def __le__(self, other):
        return self.magnitude <= other.magnitude

    @vectorMethod
    def __ne__(self, other):
        return not self == other

    @vectorMethod
    def __gt__(self, other):
        return self.magnitude > other.magnitude

    @vectorMethod
    def __ge__(self, other):
        return self.magnitude >= other.magnitude
    # </editor-fold>

    # <editor-fold desc="Object Conversions">
    def __int__(self):
        return int(self.x)

    def __complex__(self):
        return complex(self.x, self.j)

    def __float__(self):
        return float(self.x)
    # <editor-fold desc="String Output/Printing">
    def __str__(self):
        return f"({int(self.x * 100) / 100},{int(self.y * 100) / 100});({int(self.magnitude * 100) / 100}<{int(self.θ * 100) / 100})"

    def __repr__(self):
        return f"({int(self.x * 100) / 100},{int(self.y * 100) / 100});({int(self.magnitude * 100) / 100}<{int(self.θ * 100) / 100})"
    # </editor-fold>
    # </editor-fold>


def θ2θp(θ):
    if θ < 0 or θ > 2 * math.pi:
        raise ValueError("θ must be between 0 and 2 pi")
    if θ == 0:
        return 1
    return 1 - 1 / math.log(θ / (2 * math.pi))


def θp2θ(θp):
    if θp < 1:
        raise ValueError("θp must be greater than or equal to 1")
    if θp == 1:
        return 0
    return 2 * math.pi * math.exp(1 / (1 - θp))


class ImaginaryVector(Vector):

    # <editor-fold desc="Algebraic Operators">
    # <editor-fold desc="Multiplication/Division">
    @scalarMethod
    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            x = self.x * other
            y = self.y * other
            return self.__class__(x=x, y=y)
        elif isinstance(other, Vector):
            x = self.x * other.x - self.y * other.y
            y = self.x * other.y + other.x * self.y
            return self.__class__(x=x, y=y)

    @scalarMethod
    def __truediv__(self, other):
        if isinstance(other, numbers.Number):
            x = self.x / other
            y = self.y / other
            return self.__class__(x=x, y=y)
        elif isinstance(other, Vector):
            numerator = self * ImaginaryVector(other.x, - other.y)
            denomenator = other.x * other.x + other.y * other.y
            return self.__class__(x=numerator.x / denomenator,
                                  y=numerator.y / denomenator)
    # </editor-fold>
    # </editor-fold>

    # <editor-fold desc="String Output/Printing">
    def __str__(self):
        return f"({int(self.x * 100) / 100},{int(self.y * 100) / 100}i);({int(self.magnitude * 100) / 100}<{int(self.θ * 100) / 100})"

    def __repr__(self):
        return f"({int(self.x * 100) / 100},{int(self.y * 100) / 100}i);({int(self.magnitude * 100) / 100}<{int(self.θ * 100) / 100})"
    # </editor-fold>


E = Vector(x=math.e, y=0)
I = Vector(x=1, y=0)
V0 = Vector(x=0, y=0)
Ip = Vector(x=0, y=1)