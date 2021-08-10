import random
import vectorArithmetic


def testSystem():
    n = 1000
    valRange = (-10, 10)
    #Real Numbered Vectors
    createNVectors([vectorArithmetic.vector],
                   random.uniform, n, valRange)
    #Integer Vectors
    createNVectors([vectorArithmetic.vector],
                   random.randint, n, valRange)
    #Mixed Complex, Real Vectors
    createNVectors([vectorArithmetic.vector, vectorArithmetic.imaginaryVector],
                   random.uniform, n, valRange)
    #Mixed Complex, Integer Vectors
    createNVectors([vectorArithmetic.vector, vectorArithmetic.imaginaryVector],
                   random.randint, n, valRange)
    #Complex Vectors
    createNVectors([vectorArithmetic.imaginaryVector],
                   random.uniform, n, valRange)
    #Complex Vectors with integer x/y values
    createNVectors([vectorArithmetic.imaginaryVector],
                   random.randint, n, valRange)
    print("Tests Completed Successfully")

def createNVectors(vecTypeList, randomFunc, n, valRange = (-10, 10)):
    for i in range(n):
        #we won't allow any of our vectors to be (0,0) but
        #we do want zero values sometimes.  We'll alternate
        #which axis is allowed to be 0.
        x1 = randomFunc(valRange[0], valRange[1])
        while x1 == 0:
            x1 = randomFunc(valRange[0], valRange[1])
        x2 = randomFunc(valRange[0], valRange[1])
        x3 = randomFunc(valRange[0], valRange[1])
        while x3 == 0:
            x3 = randomFunc(valRange[0], valRange[1])
        x4 = randomFunc(valRange[0], valRange[1])
        y1 = randomFunc(valRange[0], valRange[1])
        y2 = randomFunc(valRange[0], valRange[1])
        while y2 == 0:
            y2 = randomFunc(valRange[0], valRange[1])
        y3 = randomFunc(valRange[0], valRange[1])
        y4 = randomFunc(valRange[0], valRange[1])
        while y4 == 0:
            y4 = randomFunc(valRange[0], valRange[1])

        V1 = random.choices(vecTypeList)[0](x = x1, y = y1)
        V2 = random.choices(vecTypeList)[0](x = x2, y = y2)
        V3 = random.choices(vecTypeList)[0](x = x3, y = y3)
        V4 = random.choices(vecTypeList)[0](x = x4, y = y4)
        
        checkAddition(V1, V2, V3)
        checkMultiplication(V1, V2, V3)
        checkDistributivity(V1, V2, V3)
        checkPowerRules(V1, V2, V3, V4)

   
def checkAddition(V1, V2, V3):
    #a + (b + c) = (a + b) + c - associativity
    assert (V1 + (V2 + V3) == (V1 + V2) + V3)
    #a + b = b + a - commutativity
    assert (V1 + V2  == V2 + V1)
    assert (V2 + V3  == V3 + V2)
    assert (V1 + V3  == V3 + V1)
    #a + 0 = a
    assert (V1 + vectorArithmetic.V0 == V1)
    assert (V2 + vectorArithmetic.V0 == V2)
    assert (V3 + vectorArithmetic.V0 == V3)
    #a + (-a) = 0
    assert (V1 - V1 == vectorArithmetic.V0)
    assert (V2 - V2 == vectorArithmetic.V0)
    assert (V3 - V3 == vectorArithmetic.V0)


def checkMultiplication(V1, V2, V3):
    #a * (b * c) = (a * b) * c - associativity
    assert (V1 * (V2 * V3) == (V1 * V2) * V3)
    #a + b = b + a - commutativity
    assert (V1 * V2  == V2 * V1)
    assert (V2 * V3  == V3 * V2)
    assert (V1 * V3  == V3 * V1)
    #a + 0 = a
    assert (V1 * vectorArithmetic.I == V1)
    assert (V2 * vectorArithmetic.I == V2)
    assert (V3 * vectorArithmetic.I == V3)
    #a + (-a) = 0
    assert (V1 / V1 == vectorArithmetic.I)
    assert (V2 / V2 == vectorArithmetic.I)
    assert (V3 / V3 == vectorArithmetic.I)


def checkDistributivity(V1, V2, V3):
    #a * (b + c) = (a * b) + (a * c)
    assert (V1 * (V2 + V3) == (V1 * V2) + (V1 * V3))


def checkPowerRules(V1, V2, V3, V4):
    for v in (V1, V2, V3):
        #m^n exists (n > 0)
        #alternatively, there exists an a that solves b = a^n -- a = b^(1/n)
        r = random.uniform(1, 10)
        i1 = random.randint(1, 10)
        i2 = random.randint(1, 10)
        i3 = random.randint(1, 10)
        x = v ** r
        x = v ** i1
        #don't need an assertion here, we're just looking for an error

        #m^i = n * n * n...(i times)
        m = vectorArithmetic.I
        for j in range(i1):
            m = m * v
        assert (m == x)

        #0^n = 0 (n > 0) Power of zero rule
        m = v
        for j in range(i1):
            m = m * vectorArithmetic.V0
            assert (m == vectorArithmetic.V0)
        
        #a^0 = I Power of one rule
        assert (v ** 0 == vectorArithmetic.I)

        #a^(-1) = I / a Power of negative one rule
        t1 = (v ** (-1))
        t2 = (vectorArithmetic.I / v)
        assert ((v ** (-1)) == (vectorArithmetic.I / v))

        #a^-n = I / a^n Change sign of exponents rule
        t1 = (v ** (-1))
        t2 = (vectorArithmetic.I / v)
        assert ((v ** (-1)) == (vectorArithmetic.I / v))

        #(a^m)*(a^n) = (a^(m + n))  product rule
        t1 = (v ** i1)
        t2 = (v ** i2)
        t3 = t1 * t2
        t4 = (v ** (i1 + i2))
        assert ((v ** i1) * (v ** i2) == (v ** (i1 + i2)))
        
        #(a^m) / (a^n) = (a^(m-n))  quotient rule
        #(a^m) * (a^-n) = (a^(m-n))  quotient rule
        #t1 = (v ** i1) #don't need to recompute
        #t2 = (v ** i2)#don't need to recompute yet
        t3 = t1 / t2
        t4 = (v ** (i1 - i2))
        assert ((v ** i1) / (v ** (i2)) == (v ** (i1 - i2)))
        
        #a^m * a^-n = a * (m-n) alternative quotient rule
        #t1 = (v ** i1) #don't need to recompute
        t2 = (v ** -i2)
        t3 = t1 * t2
        t4 = (v ** (i1 - i2))
        assert ((v ** i1) * (v ** (-i2)) == (v ** (i1 - i2)))
        
        #(a^m)^n = a^(mn) Power of a power rule
        #t1 = (v ** i1) #don't need to recompute
        t2 = t1 ** i2
        t3 = v ** (i1 * i2)
        assert (((v ** i1) ** i2) == (v ** (i1 * i2)))
        
        #(a*b)^n = (a^(n)) * (b^(n)) Power of a product rule
        t1 = (v * V4) 
        t2 = t1 ** i2
        t3 = v ** (i2)
        t4 = V4 ** (i2)
        t5 = t3 * t4
        assert (((v * V4) ** i2) == ((v ** (i2)) * (V4 ** (i2))))
        
        #(a^(1/m))^n = (a^(n/m)) Fractional exponents
        t1 = (v ** (1/i1))
        t2 = t1 ** i2
        t3 = (v ** (i2 / i1))
        assert (((v ** (1/i1)) ** i2) == (v ** (i2 / i1)))
        
        #q=v^n*w^m ==> q^l=(v^n*w^m)^l=(v^(n*l)*w^(m*l)) Power of a product rule
        t1 = (V4 ** i1) * (v ** i2)
        t2 = (t1 ** i3)
        t3 = V4 ** (i1*i3)
        t4 = v ** (i2*i3)
        t5 = t3*t4
        assert ((t1 ** i3) ==
                   ((V4 ** (i1*i3)) * (v ** (i2*i3))))

        #if y = n*x, e^y = e^(n*x)
        t1 = (v * i1)
        t2 = vectorArithmetic.E ** t1
        t3 = vectorArithmetic.E ** (v * i1)
        assert (vectorArithmetic.E ** t1 ==
                   vectorArithmetic.E ** (v * i1))

        #if x<y, -x = -1*x > -y = -1*y
        #this doesn't necessarily make sense, as there is no clear definition
        #of greater or less than in our system

        #V / 0 undefined for all V
        r = random.uniform(0, 1)
        failure = False
        try:
            v / vectorArithmetic.V0
        except:
            failure = True
        finally:
            assert (failure)

if __name__ == "__main__":
    testSystem()
