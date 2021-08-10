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
        try:
            V3 = vectorArithmetic.vector(x = x3, y = y3)
        except:
            print(logging.error(f"vector creation error x3:{x3};y3:{y3}",
                                exc_info=traceBackICanUse.full_exc_info()))
            return
        testExp(V1, V2, V3)

def testNIntegerVectors(n, valRange = (-100, 100)):
    for i in range(n):
        x1 = random.randint(valRange[0], valRange[1])
        x2 = random.randint(valRange[0], valRange[1])
        x3 = random.randint(valRange[0], valRange[1])
        y1 = random.randint(valRange[0], valRange[1])
        y2 = random.randint(valRange[0], valRange[1])
        y3 = random.randint(valRange[0], valRange[1])
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
        try:
            V3 = vectorArithmetic.vector(x = x3, y = y3)
        except:

            print(logging.error(f"vector creation error x3:{x3};y3:{y3}",
                                exc_info=traceBackICanUse.full_exc_info()))
            return
        testExp(V1, V2, V3)


"""
Our implementation must have the following properties:
(V1 ^ V2) * (V1 ^ V3) = V1 ^ (V2 + V3) - Product Rule
(V1 ^ V2) / (V1 ^ V3) = V1 ^ (V2 - V3) - Quotient Rule
(V1 ^ V2) ^ V3) = V1 ^ (V2 * V3) - Power of power Rule
(V1 * V2) ^ V3 = (V1 ^ V3) * (V2 ^ V3) - Power of a product Rule
V ^ I = V - Power of One Rule
V ^ 0 = I - Power of Zero Rule
V ^ (-I) = I / V - Power of Negative One Rule
V1 ^ (-V2) = 1 / (V1 ^ V2) - Change Sign of Exponents Rule
"""

def testExp(V1, V2, V3):
    print(f"testing vectors:")
    print(f"V1={V1}")
    print(f"V2={V2}")
    print(f"V3={V3}")
    try:
        productRuleImplementation = \
            (V1 ** V2) * (V1 ** V3) == V1 ** (V2 + V3)
        if not productRuleImplementation:
            print(f"productRuleImplementation Failure:")
            print(f"(V1 ^ V2) * (V1 ^ V3) = V1 ^ (V2 + V3)")
            print(f"V1 ^ V2 = {V1 ** V2}")
            print(f"V1 ^ V3 = {V1 ** V3}")
            print(f"(V1 ^ V2) * (V1 ^ V3) = {(V1 ** V2) * (V1 ** V3)}")
            print(f"V1 ^ (V2 + V3) = {V1 ** (V2 + V3)}") 
    except:
        print(logging.error(f"productRuleImplementation error V1:{V1};V2:{V2};V3:{V3}",
                            exc_info=traceBackICanUse.full_exc_info()))
    try:
        quotientRuleImplementation = \
            (V1 ** V2) / (V1 ** V3) == V1 ** (V2 - V3)
        if not quotientRuleImplementation:
            print(f"quotientRuleImplementation Failure:")
            print(f"(V1 ^ V2) / (V1 ^ V3) = V1 ^ (V2 - V3)")
            print(f"V1 ^ V2 = {V1 ** V2}")
            print(f"V1 ^ V3 = {V1 ** V3}")
            print(f"(V1 ^ V2) / (V1 ^ V3) = {(V1 ** V2) / (V1 ** V3)}")
            print(f"V1 ^ (V2 - V3) = {V1 ** (V2 - V3)}") 
    except:

        print(logging.error(f"quotientRuleImplementation error V1:{V1};V2:{V2};V3:{V3}",
                            exc_info=traceBackICanUse.full_exc_info()))
    try:
        productOfPowerRuleImplementation = \
            (V1 ** V2) ** V3 == V1 ** (V2 * V3)
        if not productOfPowerRuleImplementation:
            print(f"productOfPowerRuleImplementation Failure:")
            print(f"((V1 ^ V2) ^ V3) = V1 ^ (V2 * V3)")
            print(f"V1 ^ V2 = {V1 ** V2}")
            print(f"(V1 ^ V2) ^ V3 = {(V1 ** V2) ** V3}")
            print(f"(V2 * V3)  = {(V2 * V3)}")
            print(f"V1 ^ (V2 * V3) = {V1 ** (V2 * V3)}") 
    except:
        print(logging.error(f"productOfPowerRuleImplementation error V1:{V1};V2:{V2};V3:{V3}",
                            exc_info=traceBackICanUse.full_exc_info()))
    try:
        powerOfProductRuleImplementation = \
            (V1 * V2) ** V3 == (V1 ** V2) * (V1 ** V3)
        if not powerOfProductRuleImplementation:
            print(f"powerOfProductRuleImplementation Failure:")
            print(f"((V1 * V2) ^ V3) = (V1 ^ V2) * (V1 ^ V3)")
            print(f"(V1 * V2) = {V1 * V2}")
            print(f"((V1 * V2) ^ V3) = {(V1 * V2) ** V3}")
            print(f"(V1 ^ V2)  = {(V1 ** V2)}")
            print(f"(V1 ^ V3)  = {(V1 ** V3)}")
            print(f"(V1 ^ V2) * (V1 ^ V3) = {(V1 ** V2) * (V1 ** V3)}") 
    except:
        print(logging.error(f"powerOfProductRuleImplementation error V1:{V1};V2:{V2};V3:{V3}",
                            exc_info=traceBackICanUse.full_exc_info()))
    try:
        powerOfOneRuleImplementation = \
            V1 ** vectorArithmetic.I == V1
        if not powerOfProductRuleImplementation:
            print(f"powerOfOneRuleImplementation Failure:")
            print(f"V1 ^ I = V1)") 
            print(f"V1 ^ I = {V1 ** vectorArithmetic.I})") 
    except:
        print(logging.error(f"powerOfOneRuleImplementation error V1:{V1};V2:{V2};V3:{V3}",
                            exc_info=traceBackICanUse.full_exc_info()))
    try:
        powerOfZeroRuleImplementation = \
            V1 ** vectorArithmetic.V0 == vectorArithmetic.I
        if not powerOfProductRuleImplementation:
            print(f"powerOfZeroRuleImplementation Failure:")
            print(f"V1 ^ 0 = I)") 
            print(f"V1 ^ 0 = {V1 ** vectorArithmetic.V0})") 
    except:
        print(logging.error(f"powerOfZeroRuleImplementation error V1:{V1};V2:{V2};V3:{V3}",
                            exc_info=traceBackICanUse.full_exc_info()))
    try:
        powerOfNegativeOneRuleImplementation = \
            V1 ** (-vectorArithmetic.I) == vectorArithmetic.I / V1
        if not powerOfNegativeOneRuleImplementation:
            print(f"powerOfNegativeOneRuleImplementation Failure:")
            print(f"V1 ^ 0 = I)") 
            print(f"V1 ^ 0 = {V1 ** vectorArithmetic.V0})") 
    except:
        print(logging.error(f"powerOfNegativeOneRuleImplementation error V1:{V1};V2:{V2};V3:{V3}",
                            exc_info=traceBackICanUse.full_exc_info()))
    try:
        changeSignOfExponentsRuleImplementation = \
            V1 ** (-V2) == vectorArithmetic.I / (V1 ** V2)
        if not changeSignOfExponentsRuleImplementation:
            print(f"changeSignOfExponentsRuleImplementation Failure:")
            print(f"V1 ^ (-V2) = I / (V1 ^ V2))") 
            print(f"V1 ^ (-V2) = {V1 ** (-V2)})") 
            print(f"I / (V1 ^ V2) = {vectorArithmetic.I / (V1 ** V2)})")
    except:
        print(logging.error(f"changeSignOfExponentsRuleImplementation error V1:{V1};V2:{V2};V3:{V3}",
                            exc_info=traceBackICanUse.full_exc_info()))
    results = f"""
(V1 ^ V2) * (V1 ^ V3) = V1 ^ (V2 + V3) - Product Rule - Pass? {productRuleImplementation}
(V1 ^ V2) / (V1 ^ V3) = V1 ^ (V2 - V3) - Quotient Rule - Pass? {quotientRuleImplementation}
(V1 ^ V2) ^ V3) = V1 ^ (V2 * V3) - Power of power Rule - Pass? {productOfPowerRuleImplementation}
(V1 * V2) ^ V3 = (V1 ^ V3) * (V2 ^ V3) - Power of a product Rule - Pass? {powerOfProductRuleImplementation}
V ^ I = V - Power of One Rule - Pass? {powerOfOneRuleImplementation}
V ^ 0 = I - Power of Zero Rule - Pass? {powerOfZeroRuleImplementation}
V ^ (-I) = I / V - Power of Negative One Rule - Pass? {powerOfNegativeOneRuleImplementation}
V1 ^ (-V2) = 1 / (V1 ^ V2) - Change Sign of Exponents Rule - Pass? {changeSignOfExponentsRuleImplementation}
--------------------------------------------------------------------------------
"""
    print(results)
