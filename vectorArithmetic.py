"""
I am wondering what the correlation is between imaginary arithmetic
and vector arithmetic.  Is there a way of defining vector arithmetic
that is isomorphic to imaginary arithmetic?  If so, how would such
a system conceptually include things like raising a real number to a complex
number?

Let's consider an imaginary number to be simply a vector Vi = (x, y)

How does (a, b) + (c, d) correlate to (a, bi) + (c, di)?
How does (a, b) - (c, d) correlate to (a, bi) - (c, di)?

These are obviously isomorphic.  It's less obvious however, how to create
vector multiplication and division functions which are isomorphic to
imaginary arithmetic.

I'll stop here to note that we must define a 0 vector and an identity vector,
which must satisfy the properties:
V0 + X = X for all X
I * X = X * I for all X

For convenience sake, we will define an alternative identity vector
I' to simplify the shorthand of defining a vector with only a complex component.
We will write this as I'; in truth, this is just a complex vector
C = [0, iθ].

The zero vector is easy; it is simply the vector (0, 0).  As will be seen
later when we define our system of multiplication, the identity vector will
be (1, 0) (this tends to be true when we map scalar values onto our
vector field - our scalars will usually be mapped onto the complex plane
by setting its complex, or y value, to 0.

We must define a system of vector multiplication whereby:
(a, b) x (c, d) is isomporphic to (a, bi) * (c, di)
(a, b) / (c, d) is isomorphic to (a, bi) / (c, di)?

We'll need to define a new type of vector multiplication.
It won't be the dot product, since that returns a scalar.
It won't be the cross product, since that returns a vector perpendicular
to the two vectors, and we want a method that returnsa vector in the
same plane.


We would like our vector multiplication to meet the following requirement:
if X = V * W, |X| = |V| * |W|

Therefore, let's define the vector multiplication to have this property:
if X = V * W, |X| = |V| * |W|

For the angle, we need to consider the fact that the vector [I' * i] will
never scale our vector.  It will, however rotate it by 90 degrees.
This can be seen from R = C * I':  (n, mi) * (0, i) = (-m, ni).
R can be seen to have the same magnitude as C, but with a 90 degree rotation.
In general, the angular change from multiplication works out to be
dθ = abs(θX - θV) (we only ever rotate one way), and thus we have a
firm definition of vector multiplication in our system:
V * W = X; in polar coordinates, X = |V| * |W| < min(θX, θV) + abs(θX - θV)
This can much more simply be written as X = |V| * |W| <  θX + θV

Since we constrained the angular output of our multiplication to match
what happens in the complex numbers, this vector definition is exactly
isomorphic to imaginary algebra.

How would division work in such a system?
if V3 = V1 * V2, then V3 / V1 = V2 and V3 / V2 = V1

What operation gives this?  Simply the reverse of multiplication:
V3 / V1 = |V3| / |V1| < θ3 - θ1

From this, scalar multiplication and division of a vector are simple (once
again, we can consider scalar multiplication and division as complex
multiplication and division with a complex value of 0

W = V * x; |W| = |V|* x; θW = θV
W = V / x; |W| = |V| / x; θW = θV

This method of multiplication division is in fact isomorphic to complex
multiplication and division.
Great!  We've come up with a mapping from complex numbers to vectors, as
we had hoped.

How about scalar exponentiation of our vectors?
For a vector raised to a positive integer n,  this will be simply a
vector multiplied by itself n times.  But what about  non-integers
and negative numbers?

Our implementation must meet all the algebraic requirements of
an exponentiation system
https://mathinsight.org/exponentiation_basic_rules

For a vector V1 squared, the angle of the resulting vector V2 will be
θ2 = θ1 * 2 (multiplication is just addition to the nth power)
Therefore, when taking the square root of a vector V1, the angle
of the resulting vector V2 will be
θ2 = θ1 / 2
For a vector V1 cubed the angle of the resulting vector V2 will be
θ2 = θ1 * 3
Therefore, when taking the cubic root of a vector V1, the angle
of the resulting vector V2 will be
θ2 = θ1 / 3
We can extrapolate to say that for a vector V1 raised to a real
power r, the angle of the resulting vector V2 will be
θ2 = θ1 * r

Therefore, we can say define vector exponentiation by a scalar is defined
as follows:
V^n = |V|^n < θ*n

We'll need to define vector exponentiation by a vector next.

We would like our exponentiation to meet the following requirement:
If W = X^V, we would like the magnitude of our resulting vector
to be equal to the scalar exponentiation of the two operands:
|W| = |X| ^ |Y|

For the angle, we can recognize that exponentiation is just multiplication...
multiplied. In particular, for n and m, n^m / n*m = n^(m-1) / m
given that division of vectors results in simple subtraction of angles, we can say
that if W = X ^ Y, θW will look something like θW = θX * (θY - 1) - θY
We will use this as an operating definition until we have something better
to go off of.

Finally, we need to implement a logarithm, which is the inverse of the
exponentiation.  It must have the followign properties:
https://mathinsight.org/logarithm_basics

If X^V = W, the logarithm is defined as follows:
logX(W) = V

We already know what X^V will be:
W = |X| ^ |V| < θX * (θY - 1) - θY

What is a fucntion, which given this input, will give the correct output?

Let's see what happens when one of these is the E vector:
If E ^ V = W, the natural logarithm is defined as follows:
LN(W) = V

So what is the output of E ^ V?
W = |E| ^ |V| < θE * (θV - 1) - θV

since θE = 0, this is simplified:
W = |E| ^ |V| < - θV

From here, it is obvious what the LN operator needs to be:
LN(W) = ln(|W|) < - θW

I have not yet put together a test procedure for this, but I am quite
confident that this is correct.


However, since all logarithms can be defined using base trasnformations, from
an arbitrary base, we only need to define a single logarithmic function, from
which any other logarithmic function could be generated.
We will define the natural logarithm, since it's the most useful.

First, we will attempt to define a vector E which is isomorphic to the scalar
e in this system.
define exp(V) as the sum from k = 0 to infinity of V^k / k!:
exp(V) = I + V + V^2/2! + V^3/3! + ...
E = exp(I) =  I * Σ(1/k)! from k = 0 to infinity
however, Σ(1/k)! from k = 0 to infinity is the definition of the scalar e.
Therefore, in our system, E = e * I
This is exactly what you would expect - as usual, our scalar mapping is
simply a complex number with 0 imaginary part.



We will now explore in depth what it means to raise a vector to the power of another vector
(or a complex number to the power of another complex number)

We will be trying to come up with a conceptual and mathematical model that defines the following:
W ^ Z = K
Where W, Z, and K are vectors (or complex numbers)

We will use the definition of a logarithm to get there.

Strap in, this one's a doozy!!  This is the entire purpose of this exercise and it is
freakin' complicated.  If anyone does end up reading this, I hope it helps you conceptualize
what it even means to raise a vector to the power of another vector.

I've tried to use uppercase letters to indicate Vectors and Vector Operands
and lowercase letters to indicate scalars and scalar operands.  I may have not done
this perfectly.

What is a logarithm?  It's a function such that
logb(b^x) = x

For a complex number raised to an integer power, this means that
logw(W ^ n) = n

For example:
If  W = (1, 3i) and n = 2,  W ^ n = (-8, 8i)
Since Logw(W ^ n) = n, we know that logw(-8, 8i) = 2

let W = (wx + wyi)
let Z = (zx + zyi)
let W^Z = K
What is K?

LogW(W^Z) = Z                                      <<definition of a logarithm
LogW(W^Z) = logW(K)                                <<W ^ Z = K
LogW(K) = Z                                        <<simple substitution
LogW(K) = LogE(K) / LogE(W)                        <<change of base rule: logb(x) = logd(x)/logd(b)
LogW(K) = LN(K) / LN(W)                            <<Instead of base W, we now use base E
LogW(K) * LN(W) = LN(K)                            <<multiplication by LN(W)
LN(K) = LogW(K) * LN(W)                            <<rearranging
K = E^[LogW(K)*LN(W)]                              <<raise both sides to an exponent 
K = E ^ [Z    *LN(W)]                              <<substitution
W^Z = E^[Z*LN(W)]                                  <<substitution
-----------------------------------------------------------------------------------
W' = LN(W)                                         <<defining a new term W'
E^(W') = W                                         <<E^LN(X)= X
Suppose W = (I*Rw)*E^(I'*θw)                       <<good guess from the guys who know the answer
-----------------------------------------------------------------------------------
Then W' = LN[(I*Rw)*E^(I'*θw)]                     <<substitution
W' = LN(I*Rw) + LN(E^(I'*θw))                      <<Ln(A*B) = Ln(A)+Ln(B)
W' = LN(I*Rw) + I'*iθw				   <<Ln(E^(x)) = I*x
W = E^(W')					   <<copied from above
W = E^[LN(I*Rw) + I'*θw]                           <<substituting W' 
W = [E^LN(I*Rw)]*[E^(I'*θw)]                       <<X^(A+B) = (X^A)*(X^B)
W = (I*Rw)*E^(I'*θw)				   <<E^LN(X) = X
W^Z = [(I*Rw)*E^(I'*θw)]^Z                         <<Exponentiating the above line by the vector Z
W^Z = E^[Z*LN(W)]                                  <<copied from the line before we defined W'
W^Z = E^[Z]*E^[LN(W)]                              <<X^(A+B) = (X^A)*(X^B)
W^Z = E^[Z]*W                                      <<E^LN(W) = W
^^need to look more closely at this.  Seems wrong.

W^Z = E^[Z]*(I*Rw)*E^(I'*θw )                      <<W = (I*Rw)*E^(I*iθw)
W^Z = (I*Rw)*E^[Z]*E^(I'*θ w)                      <<rearranging
W^Z = (I*Rw)*E^(Z + I'*θw )                        <<(X^A)*(X^B) = X^(A+B)
W^Z = K

K = (I*Rw)*E^(Z + I'*iθw)
We've now redefined exponentiation in terms of an exponential function.

If we can define our exponential function, we can have a well defined system of exponentiation.

Once again, we would like to have a system such that
|W ^ Z| = |W| ^ |Z|
We will allow this to be a definition and see if we can calculate a value for the angular change of this
system.

From an intuitive perspective, what does the below function tell us?
K = (I*Rw)*E^(Z + I'*iθw)

Let's look only at the magnitude.  I will revert back to a more familiar scalar notation.
let's use the form Rk = |K|
then, if we define Q = Z + (I' * iθw), we have a nice scalar equivalency:
Rk=Rw*(Re)^(Rq)

Here, Q = (Zx, Zy + θw)
Rq = (Zx^2 + (Zy + θw)^2)^.5

Since we know W and Z, this is well defined:
Rk = Rw * Re ^ Rq

Further, the exponentiation is "recursively" deifined in terms of the exponentiation of the natural logarithm:
W^X = Rw * E ^ Q
"""

import math
import numbers
import sys

#we will use syntax return self.__class__(definition) for
#operator overloading in this class so that inherited methods create
#objects of the correct subclass

class vector():
    def __init__(self, x = None, y = None, θ = None, magnitude = None):
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

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return self.__class__(x = x, y = y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return self.__class__(x = x, y = y)

    def __neg__(self):
        return self.__class__(x = -self.x, y = -self.y)

    def __eq__(self, other):
        absTol = 1e-05
        relTol = 1e-05
        return ((math.isclose(self.x, other.x, rel_tol=relTol, abs_tol=absTol))
                + (math.isclose(self.y, other.y, rel_tol=relTol, abs_tol=absTol))
                + (math.isclose(self.magnitude, other.magnitude, rel_tol=relTol, abs_tol=absTol))
                + (math.isclose(self.θ, other.θ, rel_tol=relTol, abs_tol=absTol))
                >= 2)
    
    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            magnitude = self.magnitude * other
            θ = self.θ
            return self.__class__(magnitude = magnitude, θ = θ)
        elif isinstance(other, vector):
            magnitude = self.magnitude * other.magnitude
            θ = self.θ + other.θ
            return self.__class__(magnitude = magnitude, θ = θ)
        else:
            raise ValueError("operand must be a scalar, vector, or imaginary number")
            
    def __truediv__(self, other):
        if isinstance(other, numbers.Number):
            magnitude = self.magnitude / other
            θ = self.θ
            return self.__class__(magnitude = magnitude, θ = θ)
        elif isinstance(other, vector):
            magnitude = self.magnitude / other.magnitude
            θ = self.θ - other.θ
            return self.__class__(magnitude = magnitude, θ = θ)
        else:
            raise ValueError("operand must be a scalar, vector, or imaginary number")
            


    def __pow__(self, other):
        if isinstance(other, vector):
            magnitude = self.magnitude ** other.magnitude 
            θ = self.θ * (other.θ - 1) - other.θ
##        if isinstance(other, vector): #old definition
##            magnitude = self.magnitude ** other.magnitude 
##            θ = self.θ * other.θ            
##            return self.__class__(magnitude = magnitude, θ = θ)
        elif isinstance(other, numbers.Number):
            magnitude = self.magnitude ** other
            θ = self.θ * other
            return self.__class__(magnitude = magnitude, θ = θ)

        else:
            raise TypeError(f"invalid argument: {other}")

    def ln(self):
        if self.magnitude == 0:
            raise ValueError("ln undefined for magnitude=0")
        magnitude = math.log(self.magnitude)
        θ = - self.θ
        return self.__class__(x = x, y = y)

    def __str__(self):
        return f"({int(self.x * 100)/100},{int(self.y * 100)/100});({int(self.magnitude * 100)/100}<{int(self.θ * 100)/100})"
    def __repr__(self):
        return f"({int(self.x * 100)/100},{int(self.y * 100)/100});({int(self.magnitude * 100)/100}<{int(self.θ * 100)/100})"
        
def θ2θp(θ):
    if θ < 0 or θ > 2 * math.pi:
        raise ValueError("θ must be between 0 and 2 pi")
    if θ == 0:
        return 1
    return 1-1/math.log(θ/(2*math.pi))

def θp2θ(θp):
    if θp < 1:
        raise ValueError("θp must be greater than or equal to 1")
    if θp == 1:
        return 0
    return 2*math.pi*math.exp(1/(1 - θp))

class imaginaryVector(vector):
    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            x = self.x * other
            y = self.y * other
            return self.__class__(x = x, y = y)
        elif isinstance(other, vector):
            x = self.x * other.x - self.y * other.y
            y = self.x * other.y + other.x * self.y
            return self.__class__(x = x, y = y)
        else:
            raise ValueError("operand must be a scalar, vector, or imaginary number")

    def __truediv__(self, other):
        if isinstance(other, numbers.Number):
            x = self.x / other
            y = self.y / other
            return self.__class__(x = x, y = y)
        elif isinstance(other, vector):
            numerator = self * imaginaryVector(other.x, - other.y)
            denomenator = other.x * other.x + other.y * other.y
            return self.__class__(x = numerator.x / denomenator, 
                                  y = numerator.y / denomenator)
        else:
            raise ValueError("operand must be a scalar, vector, or imaginary number")
   

    def __str__(self):
        return f"({int(self.x * 100)/100},{int(self.y * 100)/100}i);({int(self.magnitude * 100)/100}<{int(self.θ * 100)/100})"
    def __repr__(self):
        return f"({int(self.x * 100)/100},{int(self.y * 100)/100}i);({int(self.magnitude * 100)/100}<{int(self.θ * 100)/100})"



E = vector(x = math.e, y = 0)
I = vector(x = 1, y = 0)
V0 = vector(x = 0, y = 0)


"""
I'm not using this anymore but I worked hard on it and don't want to lose it.

Conceptually, vector multiplication is simply scalar multiplication of the
magnitude combined with scalar addition of the angle.  Therefore, we can
exponentiate the magnitude using normal methods.
For fractional powers divisible by 2, we will allow the angle to be rotated
by pi radians / 180 degrees.
This is conceptually similar
to the idea that (n^2)^.5 = +/- n
For the angle, we should consider what happens when we take the square root
of a squared vector, and the third root of a cubed vector, etc., and see if
we can extrapolate from there.

For a vector V1 squared, the angle of the resulting vector V2 will be
θ2 = θ1 * 2 (multiplication is just addition to the nth power)
Therefore, when taking the square root of a vector V1, the angle
of the resulting vector V2 will be
θ2 = θ1 / 2
For a vector V1 cubed the angle of the resulting vector V2 will be
θ2 = θ1 * 3
Therefore, when taking the cubic root of a vector V1, the angle
of the resulting vector V2 will be
θ2 = θ1 / 3
We can extrapolate to say that for a vector V1 raised to a real
power r, the angle of the resulting vector V2 will be
θ2 = θ1 * r

Therefore, we can say that vector exponentiation follows the following
rules:
If |n| > 1 or 1/n is not divisible by 2:
V^n = |V|^n < θ*n
If 0 < |n| < 1 and (1/n) is divisible by 2:
V^n = |V|^n < θ*n or |V|^n < θ*n + pi
This can awkwardly but more correctly be written:
V^2 = |V|^n < θ*n - pi/2 +/- pi/2

Given that the multiplication of vectors in this manner is isomorphic
to multiplication of imaginary numbers, we can use the same formula
to calculate the exponentiation of imaginary numbers. 

What about raising a vector to the power of a vector?

Intuitively, the magnitude of one would be raised to the magnitude of the other.

That is because the magnitude of a vector is an unbounded real number.

However, the angle is a real number bounded between 0 and 2pi (6.28).  We would like
the output of our angle exponentiation to be an unbounded number which we will
then convert back to an angle between 0 and 2pi.  We can possibly do this
by considering the angle as an exponentiation of some base angle, but we'll
want to see how that works for the magnitude and see if we can find a good
parallel.

What if we consider our individual magnitudes as exponents from a common base e?
M1 = e^X1
M2 = e^X2
X1 = ln(M1)
X2 = ln(M2)
Then, M1 ^ M2 = (e ^ X1) ^ (e ^ X2)

However, we can also calculate this in a simpler fashion, without calculating
X1 and X2:
logM1(M1 ^ M2) = M2
logB(x) = logD(x) / logD(B)
ln(M1 ^ M2) = logM1(M1 ^ M2) / ln(M1)
e^(ln(M1 ^ M2)) = e^(logM1(M1 ^ M2) / ln(M1))
M1 ^ M2 = e^(logM1(M1 ^ M2) / ln(M1)
M1 ^ M2 = e^(M2 / ln(M1))

What about the angle?

Let's assume that an angle of 0 corresponds to a "magnitude" of 1 - this means
that the angle should not shift at all.
Let's assume that an angle of 2 * pi corresponds to a "magnitude" of infinity -
this means that the angle will shift as much as it possibly can.
We need a mapping that takes the numbers 0 -> 2 * pi and translates them to
1 -> infinity.
Investigating several options, the simplest is below:
θ'=1-1/ln(θ/2pi)
Now that we have a mapping from 1 -> infinity, we can do exponentiation:
θ'result = θ'1 ^ θ'2
Finally, we will map backwards from θ' to θ - we will need to map
the numbers 1->infinity back to 0->2*pi:
θ'=1-1/ln(θ/2pi)
ln(θ/2pi)(θ'-1)=-1
ln(θ/2pi) = -1/(θ'-1)
θ/2pi = e^(-1/(θ'-1))
θ=2pi*e^(-1/(θ'-1))


##            magSquaredAddition =  self.x ** 2 + self.y ** 2 + other.x ** 2 + other.y **2 + \
##                2 * self.x * other.x + 2 * self.y * other.y
##            magnitudeMultiplication = self.magnitude * other.magnitude
##            magnitudeAddition = magSquaredAddition ** .5
##            unscaledMagnitude = magnitudeMultiplication * magnitudeAddition
##            magnitude = unscaledMagnitude / (self.magnitude)
"""
