"""I am wondering what the correlation is between imaginary arithmetic
and vector arithmetic.
Let's consider an imaginary number to be simply a vector Vi = (x, y)

How does (a, b) + (c, d) correlate to (a, bi) + (c, di)?
    This is obviously the same.  Don't need to check.
How does (a, b) - (c, d) correlate to (a, bi) - (c, di)?
    This is obviously the same.  Don't need to check.


How does (a, b) x (c, d) correlate to (a, bi) * (c, di)?
    Depends how you define vector multiplication.  Let's look at some examples.
How does (a, b) / (c, d) correlate to (a, bi) / (c, di)?
    Depends how you define vector division. Let's look at some examples.

Vector multiplication doesn't really exist.  Instead, there are dot
products and cross products.

However, let's define a vector multiplication operator, *, where
V1 * V2 = |V1| * |V2| < θ1 + θ2

How would division work in such a system?
if V3 = V1 * V2, then V3 / V1 = V2 and V3 / V2 = V1

What operation gives this?  Simply the reverse of multiplication:
V3 / V1 = |V3| / |V1| < θ3 - θ1
"""

import math
import random

class vector():
    def __init__(self, x = None, y = None, θ = None, magnitude = None):
        if (not x is None) and (not y is None):
            if (not θ is None) or (not magnitude is None):
                raise TypeError("if x and y are specified neither θ nor magnitude may be specified.")
            self.x = x
            self.y = y
            self.magnitude = (x * x + y * y) ** .5
            self.θ = math.atan(y / x)
            if x > 0:
                self.θ += math.pi
        elif (not θ is None) and (not magnitude is None):
            if (not x is None) or (not y is None):
                raise TypeError("if θ and magnitude are specified neither x nor y may be specified.")
            self.magnitude = magnitude
            self.θ = θ
            self.x = magnitude * math.cos(θ)
            self.y = magnitude * math.sin(θ)
        else:
            raise TypeError("x and y or θ and magnitude should be specified")

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return imaginaryVector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return imaginaryVector(x, y)

    def __eq__(self, other):
        if self.x == 0 or other.x == 0:
            xEq = (abs(self.x - other.x) < 0.0001)
        else:
            xEq = (abs(self.x / other.x) < 1.0001)
        if self.y == 0 or other.y == 0:
            yEq = (abs(self.y - other.y) < 0.0001)
        else:
            yEq = (abs(self.y / other.y) < 1.0001)
        return (xEq and yEq)
    
    def __mul__(self, other):
        magnitude = self.magnitude * other.magnitude
        θ = self.θ + other.θ
        return JacksNewVectorFromMagnitudeAngle(magnitude, θ)

    def __truediv__(self, other):
        magnitude = self.magnitude / other.magnitude
        θ = self.θ - other.θ
        return JacksNewVectorFromMagnitudeAngle(magnitude, θ)

class imaginaryVector(vector):
    def __mul__(self, other):
        x = self.x * other.x - self.y * other.y
        y = self.x * other.y + other.x * self.y
        return imaginaryVector(x, y)

    def __truediv__(self, other):
        numerator = self * imaginaryVector(other.x, - other.y)
        denomenator = other.x * other.x + other.y * other.y
        return imaginaryVector(numerator.x / denomenator, numerator.y / denomenator)
