import random
import vectorArithmetic
import itertools
import datetime
import math
import inspect
from inspect import currentframe, getframeinfo
from typing import Sequence

global errLog
global success
global runType

global errList
errList = []

global absTol
global relTol
absTol = 1e-05
relTol = 1e-05

global expectedFailure
expectedFailure = False


def customAssertion(boolValue: bool, assertionType: str) -> None:
    global expectedFailure
    if not boolValue:
        global success
        global errList
        global runType
        if not expectedFailure:
            success = False
        if not (assertionType in errList):
            # print only one error per assertion type.  We want to be able to read the error log easily.
            errList.append(assertionType)
            callingFrame = currentframe().f_back
            frameInfo = getframeinfo(callingFrame)
            codeContext = frameInfo.code_context[0]
            statementStart = codeContext.find("customAssertion(")
            statement = codeContext[statementStart + len("statementStart") + 2:-2]
            statement = str(statement)
            keyValuePairs = getVariableValues(callingFrame)
            errLog.write("-" * 100 + "\n")
            errLog.write(f"{assertionType}; {runType}; Expected? {expectedFailure}\n")
            errLog.write(f"Assertion Error, line {frameInfo.lineno}: {assertionType}; {runType}\n")
            errLog.write(f"{statement}\n")
            errLog.write(" || ".join(keyValuePairs) + "\n")
            errLog.write("-" * 100 + "\n")


def getVariableValues(callingFrame: "inspect.FrameInfo") -> set[str]:
    keys = []
    values = []
    for key, value in callingFrame.f_locals.items():
        keys.append(str(key))
        try:
            val = str(value)
        except:
            val = "unavailable"
        values.append(val)
    return (":".join((key, value)) for (key, value) in zip(keys, values))


def testSystem() -> None:
    global success
    global runType

    # <editor-fold desc="Variable Initialization">
    n = 200
    valRange = (-10, 10)
    # </editor-fold>

    # <editor-fold desc="Test Algebraic Consistency">
    # Real Numbered Vectors
    runType = "Real Vectors"
    testNVectors([vectorArithmetic.Vector],
                 random.uniform, n, valRange)
    # Integer Vectors
    runType = "Integer Vectors"
    testNVectors([vectorArithmetic.Vector],
                 random.randint, n, valRange)
    # Mixed Complex, Real Vectors
    runType = "Mixed Complex, Real Vectors"
    testNVectors([vectorArithmetic.Vector, vectorArithmetic.ImaginaryVector],
                 random.uniform, n, valRange)
    # Mixed Complex, Integer Vectors
    runType = "Mixed Complex, Integer  Vectors"
    testNVectors([vectorArithmetic.Vector, vectorArithmetic.ImaginaryVector],
                 random.randint, n, valRange)
    # Complex Vectors
    runType = "Complex Vectors"
    testNVectors([vectorArithmetic.ImaginaryVector],
                 random.uniform, n, valRange)
    # Complex Vectors with integer x/y values
    runType = "Complex Integer Vectors"
    testNVectors([vectorArithmetic.ImaginaryVector],
                 random.randint, n, valRange)
    # </editor-fold>

    # <editor-fold desc="Check Vector Isomorphism and Vector Theory">
    # Ensure vector algebra is isomorphic to imaginary algebra
    runType = "Real Vector->Imaginary Isomorphism, Vector Theory"
    checkIsomorphismAndVectorTheory(random.uniform, n, valRange)
    runType = "Integer Vector->Imaginary Isomorphism, Vector Theory"
    checkIsomorphismAndVectorTheory(random.randint, n, valRange)
    # </editor-fold

    if success:
        print("Tests Completed Successfully")
    else:
        print("A failure occurred.  Check the error log: " + errLogFileName)


def testNVectors(vecTypeList: Sequence, randomFunc: callable, n: int, valRange=(-10, 10)) -> None:
    for i in range(n):
        # <editor-fold desc="Planting Seeds">
        # we won't allow any of our vectors to be (0,0) but
        # we do want zero values sometimes.  We'll alternate
        # which axis is allowed to be 0.
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
        # </editor-fold>

        # <editor-fold desc="Creating Vectors">
        V1 = random.choices(vecTypeList)[0](x=x1, y=y1)
        V2 = random.choices(vecTypeList)[0](x=x2, y=y2)
        V3 = random.choices(vecTypeList)[0](x=x3, y=y3)
        V4 = random.choices(vecTypeList)[0](x=x4, y=y4)
        # </editor-fold>

        # <editor-fold desc="Check Algebraic Rules">
        checkAddition(V1, V2, V3, V4)
        checkMultiplication(V1, V2, V3, V4)
        checkExponentiation(V1, V2, V3, V4)
        checkLogarithm(V1, V2, V3, V4)
        # </editor-fold>


def checkAddition(V1: vectorArithmetic.Vector,
                  V2: vectorArithmetic.Vector,
                  V3: vectorArithmetic.Vector,
                  V4: vectorArithmetic.Vector) -> None:
    # http://math2.org/math/algebra/basicidens.htm
    global expectedFailure

    # <editor-fold desc="Additive Identity">
    # a + 0 = a
    customAssertion(V1 + vectorArithmetic.V0 == V1, "Additive Identity")
    customAssertion(V2 + vectorArithmetic.V0 == V2, "Additive Identity")
    customAssertion(V3 + vectorArithmetic.V0 == V3, "Additive Identity")
    # </editor-fold>

    # <editor-fold desc="Additive Inverse">
    # a + (-a) = 0
    customAssertion(V1 - V1 == vectorArithmetic.V0, "Additive Inverse")
    customAssertion(V2 - V2 == vectorArithmetic.V0, "Additive Inverse")
    customAssertion(V3 - V3 == vectorArithmetic.V0, "Additive Inverse")
    # </editor-fold>

    # <editor-fold desc="Additive Associativity">
    # a + (b + c) = (a + b) + c - associativity
    customAssertion(V1 + (V2 + V3) == (V1 + V2) + V3, "Additive Associativity")
    # </editor-fold>

    # <editor-fold desc="Additive Commutativity">
    # a + b = b + a - commutativity
    customAssertion(V1 + V2 == V2 + V1, "Additive Commutativity")
    customAssertion(V2 + V3 == V3 + V2, "Additive Commutativity")
    customAssertion(V1 + V3 == V3 + V1, "Additive Commutativity")
    # </editor-fold>

    # <editor-fold desc="Definition of Subtraction">
    # a - b = a + (-b) subtraction
    customAssertion(V1 - V2 == V1 + (-V2), "Definition of Subtraction")
    customAssertion(V2 - V3 == V2 + (-V3), "Definition of Subtraction")
    customAssertion(V1 - V3 == V1 + (-V3), "Definition of Subtraction")
    # </editor-fold>

    # <editor-fold desc="Additive Isomorphism to Scalar Algebra">
    # |V1 + V2| = |V1| + |V2|
    # |V1 - V2| = |V1| - |V2|
    # I wish this were true but it is not.
    expectedFailure = True
    customAssertion((V1 + V2).magnitude == (V1.magnitude + V2.magnitude), "Additive Isomorphism to Scalar Algebra")
    customAssertion((V2 + V3).magnitude == (V2.magnitude + V3.magnitude), "Additive Isomorphism to Scalar Algebra")
    customAssertion((V1 + V3).magnitude == (V1.magnitude + V3.magnitude), "Additive Isomorphism to Scalar Algebra")
    customAssertion((V1 - V2).magnitude == (V1.magnitude - V2.magnitude), "Additive Isomorphism to Scalar Algebra")
    customAssertion((V2 - V3).magnitude == (V2.magnitude - V3.magnitude), "Additive Isomorphism to Scalar Algebra")
    customAssertion((V1 - V3).magnitude == (V1.magnitude - V3.magnitude), "Additive Isomorphism to Scalar Algebra")
    expectedFailure = False
    # </editor-fold>


def checkMultiplication(V1: vectorArithmetic.Vector,
                        V2: vectorArithmetic.Vector,
                        V3: vectorArithmetic.Vector,
                        V4: vectorArithmetic.Vector) -> None:
    # http://math2.org/math/algebra/basicidens.htm
    global absTol
    global relTol
    global expectedFailure

    # <editor-fold desc="Multiplicative Identity">
    # a * I = a
    customAssertion(V1 * vectorArithmetic.I == V1, "Multiplicative Identity")
    customAssertion(V2 * vectorArithmetic.I == V2, "Multiplicative Identity")
    customAssertion(V3 * vectorArithmetic.I == V3, "Multiplicative Identity")
    # </editor-fold>

    # <editor-fold desc="Multiplicative Inverse">
    # a / a = I
    customAssertion(V1 / V1 == vectorArithmetic.I, "Multiplicative Inverse")
    customAssertion(V2 / V2 == vectorArithmetic.I, "Multiplicative Inverse")
    customAssertion(V3 / V3 == vectorArithmetic.I, "Multiplicative Inverse")
    # </editor-fold>

    # <editor-fold desc="Multiplicative Continuity of Inverse Comparison">
    # if x<y, -x > -y
    # this fails because in our system -x == x
    expectedFailure = True
    minV1 = min(V1, V2)
    minV2 = min(V2, V3)
    minV3 = min(V1, V3)
    maxV1 = max(V1, V2)
    maxV2 = max(V2, V3)
    maxV3 = max(V1, V3)
    customAssertion(-minV1 > -maxV1, "Multiplicative Continuity of Inverse Comparison")
    customAssertion(-minV2 > -maxV2, "Multiplicative Continuity of Inverse Comparison")
    customAssertion(-minV3 > -maxV3, "Multiplicative Continuity of Inverse Comparison")
    expectedFailure = False
    # </editor-fold>

    # <editor-fold desc="Multiplication times 0">
    # a * 0 = 0
    customAssertion(V1 * vectorArithmetic.V0 == vectorArithmetic.V0, "Multiplication times 0")
    customAssertion(V2 * vectorArithmetic.V0 == vectorArithmetic.V0, "Multiplication times 0")
    customAssertion(V3 * vectorArithmetic.V0 == vectorArithmetic.V0, "Multiplication times 0")
    # </editor-fold>

    # <editor-fold desc="Multiplicative Associativity">
    # a * (b * c) = (a * b) * c - associativity
    customAssertion(V1 * (V2 * V3) == (V1 * V2) * V3, "Multiplicative Associativity")
    # </editor-fold>

    # <editor-fold desc="Multiplicative Commutativity">
    # a + b = b + a - commutativity
    customAssertion(V1 * V2 == V2 * V1, "Multiplicative Commutativity")
    customAssertion(V2 * V3 == V3 * V2, "Multiplicative Commutativity")
    customAssertion(V1 * V3 == V3 * V1, "Multiplicative Commutativity")
    # </editor-fold>

    # <editor-fold desc="Distributive Law">
    # a * (b + c) = a * b + a * c - distributive law
    customAssertion(V1 * (V2 + V3) == V1 * V2 + V1 * V3, "Distributive Law")
    customAssertion(V2 * (V1 + V3) == V2 * V1 + V2 * V3, "Distributive Law")
    customAssertion(V3 * (V1 + V2) == V3 * V1 + V3 * V2, "Distributive Law")
    # </editor-fold>

    # <editor-fold desc="Definition of Division">
    # a / b = a * (1 / b) definition of division
    customAssertion((V1 / V2) == V1 * (vectorArithmetic.I / V2), "Definition of Division")
    customAssertion((V1 / V3) == V1 * (vectorArithmetic.I / V3), "Definition of Division")
    customAssertion((V2 / V3) == V2 * (vectorArithmetic.I / V3), "Definition of Division")
    # </editor-fold>

    # <editor-fold desc="Dividing by Zero Invalid">
    # V / 0 undefined for all V
    for v in (V1, V2, V3):
        failure = False
        try:
            v / vectorArithmetic.V0
        except ZeroDivisionError:
            failure = True
        customAssertion(failure, "Dividing by Zero Invalid")
    # </editor-fold>

    # <editor-fold desc="Multiplicative Relation to Addition">
    # a + a + a ... n times = a * n
    n = random.randint(5, 10)
    testV1 = V1 * n
    testV2 = V2 * n
    testV3 = V3 * n
    V1Add = vectorArithmetic.V0
    V2Add = vectorArithmetic.V0
    V3Add = vectorArithmetic.V0
    for i in range(n):
        V1Add += V1
        V2Add += V2
        V3Add += V3
    customAssertion(V1Add == testV1, "Multiplicative Relation to Addition")
    customAssertion(V2Add == testV2, "Multiplicative Relation to Addition")
    customAssertion(V3Add == testV3, "Multiplicative Relation to Addition")
    # </editor-fold>

    # <editor-fold desc="Multiplicative Isomorphism between Vectors and Scalars">
    # |V1 * V2| = |V1| * |V2|
    # |V1 / V2| = |V1| / |V2|
    customAssertion(math.isclose((V1 * V2).magnitude, (V1.magnitude * V2.magnitude), rel_tol=relTol, abs_tol=absTol), "Multiplicative Isomorphism to Scalar Algebra")
    customAssertion(math.isclose((V2 * V3).magnitude, (V2.magnitude * V3.magnitude), rel_tol=relTol, abs_tol=absTol), "Multiplicative Isomorphism to Scalar Algebra")
    customAssertion(math.isclose((V1 * V3).magnitude, (V1.magnitude * V3.magnitude), rel_tol=relTol, abs_tol=absTol), "Multiplicative Isomorphism to Scalar Algebra")
    customAssertion(math.isclose((V1 / V2).magnitude, (V1.magnitude / V2.magnitude), rel_tol=relTol, abs_tol=absTol), "Multiplicative Isomorphism to Scalar Algebra")
    customAssertion(math.isclose((V2 / V3).magnitude, (V2.magnitude / V3.magnitude), rel_tol=relTol, abs_tol=absTol), "Multiplicative Isomorphism to Scalar Algebra")
    customAssertion(math.isclose((V1 / V3).magnitude, (V1.magnitude / V3.magnitude), rel_tol=relTol, abs_tol=absTol), "Multiplicative Isomorphism to Scalar Algebra")
    # </editor-fold>


def checkExponentiation(V1: vectorArithmetic.Vector,
                        V2: vectorArithmetic.Vector,
                        V3: vectorArithmetic.Vector,
                        V4: vectorArithmetic.Vector) -> None:

    # https://mathinsight.org/exponentiation_basic_rules

    for v in (V1, V2, V3):
        # <editor-fold desc="Exponentiation Membership 1">
        # 1:  If {V} is the set containing all vectors, V1 ^ n ∈ {V} where n is any real number
        # 2: alternatively, there exists an V2 that solves V1 = V2^n -- V2 = V1^(1/n)
        r = random.uniform(2, 10)
        i1 = random.randint(2, 10)
        i2 = random.randint(2, 10)
        i3 = random.randint(2, 10)
        try:
            x = v ** r
            x = v ** i1
        except:
            customAssertion(False, "Exponentiation Membership 1")
        # don't need an assertion here, we're just looking for an error
        # </editor-fold>

        # <editor-fold desc="Exponentiation Membership 2">
        # 1:  If {V} is the set containing all vectors, V1 ^ n ∈ {V} where n is any real number
        # 2:  alternatively, there exists an V2 that solves V1 = V2^n -- V2 = V1^(1/n)
        r = random.uniform(2, 10)
        t1 = v ** r
        customAssertion(v == t1 ** (1 / r), "Exponentiation Membership 2")
        # </editor-fold>

        # <editor-fold desc="Equivalence of Exponentiation and Multiplication">
        # m^i = n * n * n...(i times)
        m = vectorArithmetic.I
        for j in range(i1):
            m = m * v
        customAssertion(m == v ** i1, "Equivalence of Exponentiation and Multiplication")
        # </editor-fold>

        # <editor-fold desc="Power of Zero">
        # 0^n = 0 (n > 0) Power of zero rule
        m = v
        for j in range(i1):
            m = m * vectorArithmetic.V0
            customAssertion(m == vectorArithmetic.V0, "Power of Zero")
        # </editor-fold>

        # <editor-fold desc="Power of One">
        # a^0 = I Power of one rule
        customAssertion(v ** 0 == vectorArithmetic.I, "Power of One")
        # </editor-fold>

        # <editor-fold desc="Power of Negative 1">
        # a^(-1) = I / a Power of negative one rule
        t1 = (v ** (-1))
        t2 = (vectorArithmetic.I / v)
        customAssertion(v ** (-1) == vectorArithmetic.I / v, "Power of Negative 1")
        # </editor-fold>

        # <editor-fold desc="Exponential Continuity of Inverse Comparison">
        # 1: if x<I, n>1  = x^n < x
        # 2: if x>I, x^(-1) < x
        # <editor-fold desc="Continuity of Inverse Comparison Setup">
        if V1 > vectorArithmetic.I:
            invV1 = V1 ** -1
            stdV1 = V1
        else:
            invV1 = V1
            stdV1 = V1 ** -1
        if V2 > vectorArithmetic.I:
            invV2 = V2 ** -1
            stdV2 = V2
        else:
            invV2 = V2
            stdV2 = V2 ** -1
        if V3 > vectorArithmetic.I:
            invV3 = V3 ** -1
            stdV3 = V3
        else:
            invV3 = V3
            stdV3 = V3 ** -1
        i = random.randint(5, 15)
        # </editor-fold>
        # <editor-fold desc="Continuity of Inverse Comparison 1">
        if invV1 != vectorArithmetic.I:
            customAssertion(invV1 ** i < stdV1, "Continuity of Inverse Comparison 1")
        if invV2 != vectorArithmetic.I:
            customAssertion(invV2 ** i < stdV2, "Continuity of Inverse Comparison 1")
        if invV3 != vectorArithmetic.I:
            customAssertion(invV3 ** i < stdV3, "Continuity of Inverse Comparison 1")
        # </editor-fold>
        # <editor-fold desc="Continuity of Inverse Comparison 2">
        if invV1 != vectorArithmetic.I:
            customAssertion(stdV1 > invV1, "Continuity of Inverse Comparison 2")
        if invV2 != vectorArithmetic.I:
            customAssertion(stdV2 > invV2, "Continuity of Inverse Comparison 2")
        if invV3 != vectorArithmetic.I:
            customAssertion(stdV3 > invV3, "Continuity of Inverse Comparison 2")
        # </editor-fold>
        # </editor-fold>

        # <editor-fold desc="Change Sign of Exponents Rule">
        # a^-n = I / a^n Change sign of exponents rule
        t1 = (v ** (-1))
        t2 = (vectorArithmetic.I / v)
        customAssertion(v ** (-1) == vectorArithmetic.I / v, "Change Sign of Exponents Rule")
        # </editor-fold>

        # <editor-fold desc="Exponentiation Product Rule">
        # (a^m)*(a^n) = (a^(m + n))  product rule
        t1 = (v ** i1)
        t2 = (v ** i2)
        t3 = t1 * t2
        t4 = (v ** (i1 + i2))
        customAssertion((v ** i1) * (v ** i2) == (v ** (i1 + i2)), "Exponentiation Product Rule")
        # </editor-fold>

        # <editor-fold desc="Exponentiation Quotient Rule 1">
        # 1: (a^m) / (a^n) = (a^(m-n))  quotient rule
        # 2: (a^m) * (a^-n) = (a^(m-n))  quotient rule
        t1 = (v ** i1)
        t2 = (v ** i2)
        t3 = t1 / t2
        t4 = (v ** (i1 - i2))
        customAssertion((v ** i1) / (v ** i2) == (v ** (i1 - i2)), "Exponentiation Quotient Rule 1")
        # </editor-fold>

        # <editor-fold desc="Exponentiation Quotient Rule 2">
        # 1: (a^m) / (a^n) = (a^(m-n))  quotient rule
        # 2: (a^m) * (a^-n) = (a^(m-n))  quotient rule
        t1 = (v ** i1)
        t2 = (v ** -i2)
        t3 = t1 * t2
        t4 = (v ** (i1 - i2))
        customAssertion((v ** i1) * (v ** (-i2)) == v ** (i1 - i2), "Exponentiation Quotient Rule 2")
        # </editor-fold>

        # <editor-fold desc="Power of a Power Rule">
        # (a^m)^n = a^(mn) Power of a power rule
        t1 = (v ** i1)
        t2 = t1 ** i2
        t3 = v ** (i1 * i2)
        customAssertion((v ** i1) ** i2 == (v ** (i1 * i2)), "Power of a Power Rule")
        # </editor-fold>

        # <editor-fold desc="Power of a Product Rule">
        # (a*b)^n = (a^(n)) * (b^(n)) Power of a product rule
        t1 = (v * V4)
        t2 = t1 ** i2
        t3 = v ** i2
        t4 = V4 ** i2
        t5 = t3 * t4
        customAssertion((v * V4) ** i2 == (v ** i2) * (V4 ** i2), "Power of a Product Rule")
        # </editor-fold>

        # <editor-fold desc="Fractional Exponents">
        # (a^(1/m))^n = (a^(n/m)) Fractional exponents
        t1 = (v ** (1 / i1))
        t2 = t1 ** i2
        t3 = (v ** (i2 / i1))
        customAssertion((v ** (1 / i1)) ** i2 == v ** (i2 / i1), "Fractional Exponents")
        # </editor-fold>

        # <editor-fold desc="Power of Multiple Products Rule">
        # q=v^n*w^m ==> q^l=(v^n*w^m)^l=(v^(n*l)*w^(m*l)) Power of multiple products rule
        # we're going to statically declare n m and l to avoid our vectors getting too large
        n = 2
        m = 3
        l = 2
        t1 = (V4 ** n) * (v ** m)
        t2 = (t1 ** l)
        t3 = V4 ** (n * l)
        t4 = v ** (m * l)
        t5 = t3 * t4
        customAssertion(t1 ** l == (V4 ** (n * l)) * (v ** (m * l)), "Power of Multiple Products Rule")
        # </editor-fold>

        # <editor-fold desc="Exponentiation Product rule for vector E">
        # if y = n*x, e^y = e^(n*x)
        t1 = (v * i1)
        t2 = vectorArithmetic.E ** t1
        t3 = vectorArithmetic.E ** (v * i1)
        customAssertion(vectorArithmetic.E ** t1 == vectorArithmetic.E ** (v * i1), "Exponentiation Product rule for vector E")
        # </editor-fold>


def checkLogarithm(V1: vectorArithmetic.Vector,
                   V2: vectorArithmetic.Vector,
                   V3: vectorArithmetic.Vector,
                   V4: vectorArithmetic.Vector) -> None:

    # https://mathinsight.org/logarithm_basics

    # <editor-fold desc="Logarithm of E Rule">
    # ln(e) = 1
    customAssertion(vectorArithmetic.E.ln() == 1, "Logarithm of E Rule")
    # </editor-fold>

    # <editor-fold desc="Logarithm of 1 Rule">
    # ln(1) = 0
    customAssertion(vectorArithmetic.I.ln() == 0, "Logarithm of 1 Rule")
    # </editor-fold>

    # <editor-fold desc="Logarithm of 1p Rule">
    # ln(1) = 0
    customAssertion(vectorArithmetic.Ip.ln() == 0, "Logarithm of 1p Rule")
    # </editor-fold>

    for v in (V1, V2, V3):
        # <editor-fold desc="Definition of Logarithm">
        # If b^n=k, logb(k) = n
        # we can only check this directly for b = E and logb = ln
        if v.magnitude > 0:
            customAssertion((vectorArithmetic.E ** v).ln() == v, "Definition of Logarithm")
        # </editor-fold>

        # <editor-fold desc="Indirect Definition of Logarithm">
        # If b^n=k, logb(k) = n
        # we can check this indirectly using the change of base rule: LogW(K) = LN(K) / LN(W)
        # therefore, if we have two vectors V1 and V2, LogV1(V2) = LN(V2) / LN(V1)
        # this is implemented internally in our Vector type
        if v.magnitude > 1 and V4.magnitude > 0:
            t = v ** V4
            try:
                customAssertion(v.log(V4) == t, "Indirect Definition of Logarithm")
            except:
                pass
        # </editor-fold>

        # <editor-fold desc="Logarithm Product Rule">
        # ln(xy) = ln(x) + ln(y)
        if v.magnitude > 0 and V4.magnitude > 0:
            t = v * V4
            customAssertion(t.ln() == v.ln() + V4.ln(), "Logarithm Product Rule")
        # </editor-fold>

        # <editor-fold desc="Logarithm Quotient Rule">
        # ln(x/y) = ln(x) - ln(y)
        if v.magnitude > 0 and V4.magnitude > 0:
            t = v / V4
            customAssertion(t.ln() == v.ln() - V4.ln(), "Logarithm Quotient Rule")
        # </editor-fold>

        # <editor-fold desc="Logarithm of Power Rule">
        # ln(x^y) = y * ln(x)
        if v.magnitude > 0 and V4.magnitude > 0:
            t = v ** V4
            customAssertion(t.ln() == V4 * v.ln(), "Logarithm of Power Rule")
        # </editor-fold>

        # <editor-fold desc="Logarithm of Reciprocal Rule">
        # ln(1/x) = -ln(x)
        if v.magnitude > 0:
            t = v * V4
            customAssertion((vectorArithmetic.I / t).ln() == -(t.ln()), "Logarithm of Reciprocal Rule")
        # </editor-fold>


def checkIsomorphismAndVectorTheory(randomFunc: callable, n: int, valRange=(-10, 10)) -> None:
    for i in range(n):
        # <editor-fold desc="Planting Seeds">
        # we won't allow any of our vectors to be (0,0) but
        # we do want zero values sometimes.  We'll alternate
        # which axis is allowed to be 0.
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
        randInt1 = random.randint(-5, 5)
        randInt2 = random.randint(-5, 5)
        randInt3 = random.randint(-5, 5)
        randInt4 = random.randint(-5, 5)
        randInts = [randInt1, randInt2, randInt3, randInt4]
        randFloat1 = random.randrange(-5, 5)
        randFloat2 = random.randrange(-5, 5)
        randFloat3 = random.randrange(-5, 5)
        randFloat4 = random.randrange(-5, 5)
        randFloats = [randFloat1, randFloat2, randFloat3, randFloat4]
        # </editor-fold>

        # <editor-fold desc="Creating Vectors">
        V1 = vectorArithmetic.Vector(x=x1, y=y1)
        V2 = vectorArithmetic.Vector(x=x2, y=y2)
        V3 = vectorArithmetic.Vector(x=x3, y=y3)
        V4 = vectorArithmetic.Vector(x=x4, y=y4)
        I1 = vectorArithmetic.ImaginaryVector(x=x1, y=y1)
        I2 = vectorArithmetic.ImaginaryVector(x=x2, y=y2)
        I3 = vectorArithmetic.ImaginaryVector(x=x3, y=y3)
        I4 = vectorArithmetic.ImaginaryVector(x=x4, y=y4)
        vectors = (V1, V2, V3, V4)
        imaginaryVectors = (I1, I2, I3, I4)
        # </editor-fold>

        # <editor-fold desc="Unary Operation Isomorphism">
        customAssertion(V1 == I1, "Equality Isomorphism")
        customAssertion(V2 == I2, "Equality Isomorphism")
        customAssertion(V3 == I3, "Equality Isomorphism")
        customAssertion(V4 == I4, "Equality Isomorphism")
        customAssertion(-V1 == -I1, "Negation Isomorphism")
        customAssertion(-V2 == -I2, "Negation Isomorphism")
        customAssertion(-V3 == -I3, "Negation Isomorphism")
        customAssertion(-V4 == -I4, "Negation Isomorphism")
        customAssertion(V1.ln() == I1.ln(), "Logarithm Isomorphism")
        customAssertion(V2.ln() == I2.ln(), "Logarithm Isomorphism")
        customAssertion(V3.ln() == I3.ln(), "Logarithm Isomorphism")
        customAssertion(V4.ln() == I4.ln(), "Logarithm Isomorphism")
        # </editor-fold>

        # <editor-fold desc="Binary Operation Isomorphism - Built In's">
        customAssertion(V1 ** -1 == I1 ** -1, "Exponentiation Isomorphism - -1")
        customAssertion(V2 ** -1 == I2 ** -1, "Exponentiation Isomorphism - -1")
        customAssertion(V3 ** -1 == I3 ** -1, "Exponentiation Isomorphism - -1")
        customAssertion(V4 ** -1 == I4 ** -1, "Exponentiation Isomorphism - -1")

        customAssertion(V1 ** vectorArithmetic.Ip == I1 ** vectorArithmetic.Ip, "Exponentiation Isomorphism - I'")
        customAssertion(V2 ** vectorArithmetic.Ip == I2 ** vectorArithmetic.Ip, "Exponentiation Isomorphism - I'")
        customAssertion(V3 ** vectorArithmetic.Ip == I3 ** vectorArithmetic.Ip, "Exponentiation Isomorphism - I'")
        customAssertion(V4 ** vectorArithmetic.Ip == I4 ** vectorArithmetic.Ip, "Exponentiation Isomorphism - I'")

        customAssertion(vectorArithmetic.E ** V1 == vectorArithmetic.E ** I1, "Exponentiation Isomorphism - E")
        customAssertion(vectorArithmetic.E ** V2 == vectorArithmetic.E ** I2, "Exponentiation Isomorphism - E")
        customAssertion(vectorArithmetic.E ** V3 == vectorArithmetic.E ** I3, "Exponentiation Isomorphism - E")
        customAssertion(vectorArithmetic.E ** V4 == vectorArithmetic.E ** I4, "Exponentiation Isomorphism - E")
        # </editor-fold>

        # <editor-fold desc="Binary Operation Isomorphism, Vector Theory">
        for (i, j) in itertools.combinations(range(4), 2):
            Vi = vectors[i]
            Vj = vectors[j]
            Ii = imaginaryVectors[i]
            Ij = imaginaryVectors[j]

            customAssertion(Vi + Vj == Ii + Ij, "Addition Isomorphism")
            customAssertion(Vi + Vj.x == Vi + vectorArithmetic.Vector(Vj.x, 0), "Real Number Addition Isomorphism")
            customAssertion(Vi - Vj == Ii - Ij, "Subtraction Isomorphism")
            customAssertion(Vi - Vj.x == Vi - vectorArithmetic.Vector(-Vj.x, 0), "Real Number Subtraction Isomorphism")
            customAssertion(Vi * Vj == Ii * Ij, "Multiplication Isomorphism")
            customAssertion(Vi * Vj.x == Vi * vectorArithmetic.Vector(-Vj.x, 0), "Real Number Multiplication Isomorphism")
            try:
                customAssertion(Vi / Vj == Ii / Ij, "Division Isomorphism")
            except ZeroDivisionError:
                pass
            try:
                customAssertion(Vi / Vj.x == Vi / vectorArithmetic.Vector(-Vj.x, 0), "Real Number Division Isomorphism")
            except ZeroDivisionError:
                pass
            customAssertion(Vi ** Vj == Ii ** Ij, "Exponentiation Isomorphism")
            customAssertion(Vi ** Vj.x == Vi ** vectorArithmetic.Vector(-Vj.x, 0), "Real Number Exponentiation Isomorphism")

            customAssertion(Vi ** Vj == Vi ** vectorArithmetic.Vector(0, Vj.y), "Nonrotation from ignoring the x vector")
            for x in randInts:
                customAssertion(Vi ** Vj == Vi ** vectorArithmetic.Vector(x, Vj.y), "Nonrotation from ignoring the x vector")
            for x in randFloats:
                customAssertion(Vi ** Vj == Vi ** vectorArithmetic.Vector(x, Vj.y), "Nonrotation from ignoring the x vector")
            for (x, y) in itertools.combinations(randInts, 2):
                B = vectorArithmetic.Ip * x
                C = vectorArithmetic.Ip * y
                customAssertion(((Vi ** B) ** C).θ == Vi.θ, "Nonrotation from double exponentiation")

            # <editor-fold desc="Definition of Vector Exponentiation">
            # For any two scalars n and m, n^m / n*m = n^(m-1) / m
            # Therefore, for any two vectors V and W, V ^ W / V * W = V ^ (W - I) / W
            customAssertion((Vi ** Vj) / (Vi * Vj) == ((Vi ** (Vj - vectorArithmetic.I)) / Vi), "Definition of Vector Exponentiation")
            # </editor-fold>

            # <editor-fold desc="Definition of Vector Exponentiation">
            # For any two scalars n and m, n^m / n*m = n^(m-1) / m
            # Therefore, for any two vectors V and W, V ^ W / V * W = V ^ (W - I) / W
            customAssertion((Vi ** Vj) / (Vi * Vj) == ((Vi ** (Vj - vectorArithmetic.I)) / Vi), "Definition of Vector Exponentiation")
            # </editor-fold>

        # </editor-fold>


if __name__ == "__main__":
    success = True
    timestamp = datetime.datetime.now()
    errLogFileName = f"outputlog {timestamp.year}.{timestamp.month:02}.{timestamp.day:02}...{timestamp.hour:02}.{timestamp.minute:02}.{timestamp.second:02}.txt"

    with open(errLogFileName, "w", encoding="utf-8") as errLog:
        testSystem()
