import random
import vectorArithmetic
import traceBackICanUse
import logging



def testNRealVectors(n, valRange = (-10, 10)):
    for i in range(n):
        x1 = random.uniform(valRange[0], valRange[1])
        x2 = random.uniform(valRange[0], valRange[1])
        x3 = random.uniform(valRange[0], valRange[1])
        y1 = random.uniform(valRange[0], valRange[1])
        y2 = random.uniform(valRange[0], valRange[1])
        y3 = random.uniform(valRange[0], valRange[1])
        try:
            V1 = vectorArithmetic.vector(x = x1, y = y1)
        except:
            print(logging.error(f"vector creation error x1:{x1};y1:{y1}",
                                exc_info=traceBackICanUse.full_exc_info()))
            return
        try:
            V2 = vectorArithmetic.vector(x = x2, y = y2)
        except:
            print(logging.error(f"vector creation error x2:{x2};y2:{y2}",
                                exc_info=traceBackICanUse.full_exc_info()))
            return
        testLog(V1, V2)

def testNIntegerVectors(n, valRange = (-100, 100)):
    for i in range(n):
        x1 = random.uniform(valRange[0], valRange[1])
        x2 = random.uniform(valRange[0], valRange[1])
        y1 = random.uniform(valRange[0], valRange[1])
        y2 = random.uniform(valRange[0], valRange[1])
        try:
            V1 = vectorArithmetic.vector(x = x1, y = y1)
        except:
            print(logging.error(f"vector creation error x1:{x1};y1:{y1}",
                                exc_info=traceBackICanUse.full_exc_info()))
            return
        try:
            V2 = vectorArithmetic.vector(x = x2, y = y2)
        except:
            print(logging.error(f"vector creation error x2:{x2};y2:{y2}",
                                exc_info=traceBackICanUse.full_exc_info()))
            return
        testLog(V1, V2)


"""
Our implementation must have the following properties:
ln(V1*V2) = ln(V1) + ln(V2) - Product Rule
ln(V1/V2) = ln(V1) - ln(V2) - Quotient Rule
ln(V1 ** V2) = V2 * ln(V1) - Log of power Rule
ln(E) = 1 - Log of e
ln(1) = 0 - Log of 1
ln(1/V1) = -ln(V1) - Log of reciprocal
"""

def testLog(V1, V2):
    print(f"testing vectors V1={V1} and V2={V2}")
    try:
        productRuleImplementation = \
            (V1 * V2).ln() == V1.ln() + V2.ln()
        if not productRuleImplementation:
            print(f"productRuleImplementation Failure ln(V1*V2) = ln(V1) + ln(V2)")
            print(f"V1 * V2 = {V1 * V2}")
            print(f"ln(V1 * V2) = {(V1 * V2).ln()}")
            print(f"ln(V1) = {V1.ln()}; ln(V2) = {V2.ln()}")
    except:
        productRuleImplementation = ""
        print(logging.error(f"productRuleImplementation error V1:{V1};V2:{V2}",
                            exc_info=traceBackICanUse.full_exc_info()))
    try:
        quotientRuleImplementation = \
            (V1 / V2).ln() == V1.ln() - V2.ln()
        if not quotientRuleImplementation:
            print(f"QuotientRuleImplementation Failure ln(V1/V2) = ln(V1) - ln(V2)")
            print(f"V1 / V2 = {V1 / V2}")
            print(f"ln(V1 / V2) = {(V1 / V2).ln()}")
            print(f"ln(V1) = {V1.ln()}; ln(V2) = {V2.ln()}")
    except:
        quotientRuleImplementation = ""
        print(logging.error(f"quotientRuleImplementation error V1:{V1};V2:{V2}",
                            exc_info=traceBackICanUse.full_exc_info()))
    try:
        logOfPowerRuleImplementation = \
            (V1 ** V2).ln() == V2 * (V1.ln())
        if not logOfPowerRuleImplementation:
            print(f"logOfPowerRuleImplementation Failure ln(V1 ** V2) = V2 * ln(V1)")
            print(f"V1 ^ V2 = {V1 ** V2}")
            print(f"ln(V1 ^ V2) = {(V1 ** V2).ln()}")
            print(f"ln(V1) = {V1.ln()}; V2 * ln(V1) = {V2 * (V1.ln())}")
    except:
        logOfPowerRuleImplementation = ""
        print(logging.error(f"productOfPowerRuleImplementation error V1:{V1};V2:{V2}",
                            exc_info=traceBackICanUse.full_exc_info()))
    try:
        logOfERuleImplementation = \
            vectorArithmetic.E.ln() == vectorArithmetic.I
        if not logOfERuleImplementation:
            print(f"logOfERuleImplementation Failure ln(E) = 1")
            print(f"ln(E) = {vectorArithmetic.E.ln()}")
    except:
        logOfERuleImplementation = ""
        print(logging.error(f"powerOfProductRuleImplementation error V1:{V1};V2:{V2}",
                            exc_info=traceBackICanUse.full_exc_info()))
    try:
        logOfOneRuleImplementation = \
            vectorArithmetic.I.ln() == vectorArithmetic.V0
        if not logOfERuleImplementation:
            print(f"logOfOneRuleImplementation Failure ln(1) = 0")
            print(f"ln(I) = {vectorArithmetic.I.ln()}")
    except:
        logOfOneRuleImplementation = ""
        print(logging.error(f"logOfOneRuleImplementation error V1:{V1};V2:{V2}",
                            exc_info=traceBackICanUse.full_exc_info()))
    try:
        logOfReciprocalRuleImplementation = \
            (vectorArithmetic.I / V1).ln() == -(V1.ln())
        if not logOfReciprocalRuleImplementation:
            print(f"logOfReciprocalRuleImplementation Failure ln(1/V1) = -ln(V1)")
            print(f"(1/V1) = {vectorArithmetic.I / V1}")
            print(f"ln(1/V1) = {(vectorArithmetic.I / V1).ln()}")
            print(f"-ln(V1) = {-(V1).ln()}")
    except:
        logOfReciprocalRuleImplementation = ""
        print(logging.error(f"logOfReciprocalRuleImplementation error V1:{V1};V2:{V2}",
                            exc_info=traceBackICanUse.full_exc_info()))
    results = f"""
ln(V1*V2) = ln(V1) + ln(V2) - Product Rule - Pass? {productRuleImplementation}
ln(V1/V2) = ln(V1) - ln(V2) - Quotient Rule - Pass? {quotientRuleImplementation}
ln(V1 ** V2) = V2 * ln(V1) - Log of power Rule - Pass? {logOfPowerRuleImplementation}
ln(E) = 1 - Log of e - Pass? {logOfERuleImplementation}
ln(1) = 0 - Log of 1 - Pass? {logOfOneRuleImplementation}
ln(1/V1) = -ln(V1) - Log of reciprocal - Pass? {logOfReciprocalRuleImplementation}
-------------------------------------------------------------------------------
"""
    print(results)
