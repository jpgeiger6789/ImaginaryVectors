import math
import numbers
from typing import Union

# we will use syntax return self.__class__(definition) for
# operator overloading in this class so that inherited methods create
# objects of the correct subclass


def vectorMethod(func: callable) -> callable:
    def decorated(self, other, *args, **kargs):
        if isinstance(other, Vector):
            return func(self, other, *args, **kargs)
        elif isinstance(other, complex):
            return func(self, Vector(x=other.real, y=other.imag), *args, **kargs)
        else:
            return NotImplemented
    return decorated


def scalarMethod(func: callable) -> callable:
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

    def __init__(self, x: float = None, y: float = None, θ: float = None, magnitude: float = None):
        if (not (x is None)) and (not (y is None)):
            if (not (θ is None)) or (not (magnitude is None)):
                raise TypeError("if x and y are specified neither θ nor magnitude may be specified.")
            self.x = x
            self.y = y
            self.magnitude = (x * x + y * y) ** .5
            if x == 0:
                if y > 0:
                    self.θ = math.pi / 2
                elif y < 0:
                    self.θ = 3 * math.pi / 2
                else:
                    self.θ = 0
            else:
                self.θ = math.atan(y / x) % (2 * math.pi)
            if x < 0:
                self.θ += math.pi
                self.θ = self.θ % (2 * math.pi)

        elif (not (θ is None)) and (not (magnitude is None)):
            if (not (x is None)) or (not (y is None)):
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
    def __add__(self, other: Union["Vector", float, int]) -> "Vector":
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
        elif isinstance(other, (float, int)):
            x = self.x + other
            y = self.y
        else:
            return NotImplemented
        return self.__class__(x=x, y=y)

    @scalarMethod
    def __sub__(self, other: Union["Vector", float, int]) -> "Vector":
        if isinstance(other, Vector):
            x = self.x - other.x
            y = self.y - other.y
        elif isinstance(other, (float, int)):
            x = self.x - other
            y = self.y
        else:
            return NotImplemented
        return self.__class__(x=x, y=y)

    def __neg__(self) -> "Vector":
        return self.__class__(x=-self.x, y=-self.y)
    # </editor-fold>

    # <editor-fold desc="Mutiplication Division">
    @scalarMethod
    def __mul__(self, other: Union["Vector", float, int]) -> "Vector":
        if isinstance(other, Vector):
            magnitude = self.magnitude * other.magnitude
            if magnitude == 0:
                θ = 0
            else:
                θ = self.θ + other.θ
        elif isinstance(other, (float, int)):
            magnitude = self.magnitude * other
            θ = self.θ
        else:
            return NotImplemented
        return self.__class__(magnitude=magnitude, θ=θ)

    @scalarMethod
    def __truediv__(self, other: Union["Vector", float, int]) -> "Vector":
        if isinstance(other, Vector):
            magnitude = self.magnitude / other.magnitude
            θ = self.θ - other.θ
        elif isinstance(other, (float, int)):
            magnitude = self.magnitude / other
            θ = self.θ
        else:
            return NotImplemented
        return self.__class__(magnitude=magnitude, θ=θ)
    # </editor-fold>

    # <editor-fold desc="Exponentiation Logarithm">
    @scalarMethod
    def __pow__(self, other: Union["Vector", float, int]) -> "Vector":
        if isinstance(other, Vector):
            magnitude = self.magnitude ** other.magnitude
            θ = self.θ * (other.θ - 1) - other.θ
        elif isinstance(other, (float, int)):
            magnitude = self.magnitude ** other
            θ = self.θ * other
        else:
            return NotImplemented
        return self.__class__(magnitude=magnitude, θ=θ)

    def ln(self) -> "Vector":
        # LN(W) = ln(|W|) < - θW
        if self.magnitude == 0:
            return NotImplemented
        magnitude = math.log(self.magnitude)
        θ = - self.θ
        return self.__class__(magnitude=magnitude, θ=θ)

    def log(self, other: "Vector") -> "Vector":
        # if V1 ^ V3 = V2, logV1(V2) = V3
        # if we have two vectors V1 and V2, LogV1(V2) = LN(V2) / LN(V1)
        if self.magnitude == 0:
            return NotImplemented
        if other.magnitude == 0:
            return NotImplemented
        return other.ln() / self.ln()
    # </editor-fold>
    # </editor-fold>

    # <editor-fold desc="Comparison Operators">
    def __bool__(self) -> bool:
        return self.magnitude > 0

    def __abs__(self) -> float:
        return self.magnitude

    @scalarMethod
    def __eq__(self, other: Union["Vector", int, float]) -> bool:
        if isinstance(other, Vector):
            absTol = 1e-05
            relTol = 1e-05
            magEql = math.isclose(self.magnitude, other.magnitude, rel_tol=relTol, abs_tol=absTol)
            θEql = math.isclose(self.θ, other.θ, rel_tol=relTol, abs_tol=absTol)
            return magEql and θEql
        elif isinstance(other, (int, float)):
            return (self.x == other) and self.y == 0

    @vectorMethod
    def __lt__(self, other: "Vector") -> bool:
        return self.magnitude < other.magnitude

    @vectorMethod
    def __le__(self, other: "Vector") -> bool:
        return self.magnitude <= other.magnitude

    @vectorMethod
    def __ne__(self, other: "Vector") -> bool:
        return not self == other

    @vectorMethod
    def __gt__(self, other: "Vector") -> bool:
        return self.magnitude > other.magnitude

    @vectorMethod
    def __ge__(self, other: "Vector") -> bool:
        return self.magnitude >= other.magnitude
    # </editor-fold>

    # <editor-fold desc="Object Conversions">
    def __int__(self) -> int:
        return int(self.x)

    def __complex__(self) -> complex:
        return complex(self.x, self.y)

    def __float__(self) -> float:
        return float(self.x)

    # <editor-fold desc="String Output/Printing">
    def __str__(self) -> str:
        return f"Vector: ({self.x:.2e},{self.y:.2e});({self.magnitude:.2e}<{self.θ:.2e})"

    def __repr__(self) -> str:
        return f"Vector: ({self.x},{self.y});({self.magnitude}<{self.θ})"
    # </editor-fold>
    # </editor-fold>


def θ2θp(θ: float) -> float:
    if θ < 0 or θ > 2 * math.pi:
        raise ValueError("θ must be between 0 and 2 pi")
    if θ == 0:
        return 1
    return 1 - 1 / math.log(θ / (2 * math.pi))


def θp2θ(θp: float) -> float:
    if θp < 1:
        raise ValueError("θp must be greater than or equal to 1")
    if θp == 1:
        return 0
    return 2 * math.pi * math.exp(1 / (1 - θp))


class ImaginaryVector(Vector):

    # <editor-fold desc="Algebraic Operators">
    # <editor-fold desc="Multiplication/Division">
    @scalarMethod
    def __mul__(self, other: Union[Vector, "ImaginaryVector", int, float]) -> "ImaginaryVector":
        if isinstance(other, Vector):
            x = self.x * other.x - self.y * other.y
            y = self.x * other.y + other.x * self.y
            return self.__class__(x=x, y=y)
        elif isinstance(other, (int, float)):
            x = self.x * other
            y = self.y * other
            return self.__class__(x=x, y=y)

    @scalarMethod
    def __truediv__(self, other: Union[Vector, "ImaginaryVector", int, float]) -> "ImaginaryVector":
        if isinstance(other, Vector):
            numerator = self * ImaginaryVector(other.x, - other.y)
            denominator = other.x * other.x + other.y * other.y
            return self.__class__(x=numerator.x / denominator,
                                  y=numerator.y / denominator)
        elif isinstance(other, (int, float)):
            x = self.x / other
            y = self.y / other
            return self.__class__(x=x, y=y)
    # </editor-fold>
    # </editor-fold>

    # <editor-fold desc="String Output/Printing">
    def __str__(self) -> str:
        return f"Imaginary Vector: ({self.x:.2e},{self.y:.2e}i);({self.magnitude:.2e}<{self.θ:.2e})"

    def __repr__(self) -> str:
        return f"Imaginary Vector: ({self.x},{self.y}i);({self.magnitude}<{self.θ})"
    # </editor-fold>


E = Vector(x=math.e, y=0)
I = Vector(x=1, y=0)
V0 = Vector(x=0, y=0)
Ip = Vector(x=0, y=1)
Ipi = Vector(x=0, y=math.pi)


V1 = Vector(2, 4)
V1 * V0