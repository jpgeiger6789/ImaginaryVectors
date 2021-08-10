import random
import vectorArithmetic


def testNRealVectors(n, valRange = (-1000, 1000)):
    for i in range(n):
        x1 = random.uniform(valRange[0], valRange[1])
        y1 = random.uniform(valRange[0], valRange[1])
        x2 = random.uniform(valRange[0], valRange[1])
        y2 = random.uniform(valRange[0], valRange[1])
        testTwoVectors(x1, y1, x2, y2)

def testNIntegerVectors(n, valRange = (-1000, 1000)):
    for i in range(n):
        x1 = random.randint(valRange[0], valRange[1])
        y1 = random.randint(valRange[0], valRange[1])
        x2 = random.randint(valRange[0], valRange[1])
        y2 = random.randint(valRange[0], valRange[1])
        testTwoVectors(x1, y1, x2, y2)

def testTwoVectors(x1, y1, x2, y2):
    imagVec1 = vectorArithmetic.imaginaryVector(x = x1, y = y1)
    imagVec2 = vectorArithmetic.imaginaryVector(x = x2, y = y2)
    realVec1 = vectorArithmetic.vector(x = x1, y = y1)
    realVec2 = vectorArithmetic.vector(x = x2, y = y2)

    imagMultVec = imagVec1 * imagVec2
    realMultVec = realVec1 * realVec2
    
    imagDivVec1 = imagVec1 / imagVec2
    imagDivVec2 = imagMultVec / imagVec1
    imagDivVec3 = imagMultVec / imagVec2
    realDivVec1 = realVec1 / realVec2
    realDivVec2 = realMultVec / realVec1
    realDivVec3 = realMultVec / realVec2
    
    multSame = imagMultVec == realMultVec
    divSame = (imagDivVec1 == realDivVec1 and
               imagDivVec2 == imagVec2 and
               imagDivVec3 == imagVec1 and
               realDivVec2 == realVec2 and
               realDivVec3 == realVec1)

    recip11 = vectorArithmetic.I / realVec1
    recip12 = vectorArithmetic.I / recip11
    recip21 = vectorArithmetic.I / realVec2
    recip22 = vectorArithmetic.I / recip21
    
    recipSame = (recip12 == realVec1 and
               recip22 == realVec2)
    
    print(f"Vector1: {x1}, {y1}")
    print(f"Vector2: {x2}, {y2}")
    print(f"multiplication is the same: {multSame}")
    print(f"division is the same: {divSame}")
    print(f"reciprocal is the same: {recipSame}")
    if multSame and divSame:
        print("multiplication results:  (imaginary then real)")
        print(f"{imagMultVec.x}, {imagMultVec.y}")
        print(f"{realMultVec.x}, {realMultVec.y}")
        print("division results:  (imaginary then real")
        print(f"{imagDivVec1.x}, {imagDivVec1.y}")
        print(f"{realDivVec1.x}, {realDivVec1.y}")
    if not multSame:        
        print("imaginary multiplication results:")
        print(f"{imagMultVec.x}, {imagMultVec.y}")
        print("real vector multiplication results:")
        print(f"{realMultVec.x}, {realMultVec.y}")
    if not divSame:
        print("imaginary division results forward:")
        print(f"{imagDivVec1.x}, {realDivVec1.y}")
        print("real vector division results forward:")
        print(f"{realDivVec1.x}, {realDivVec1.y}")
        print("imaginary division results reverse 1 (should equal Vector2):")
        print(f"{imagDivVec2.x}, {imagDivVec2.y}")
        print("imaginary division results reverse 2 (should equal Vector1):")
        print(f"{imagDivVec3.x}, {imagDivVec3.y}")
        print("real vector division results reverse 1 (should equal Vector2):")
        print(f"{realDivVec2.x}, {realDivVec2.y}")
        print("real vector division results reverse 2 (should equal Vector1):")
        print(f"{realDivVec3.x}, {realDivVec3.y}")
    if not recipSame:
        print(f"reciprocal of V1 = {recip11}; second reciprocal = {recip12}")
        print(f"reciprocal of V2 = {recip21}; second reciprocal = {recip22}")
    print("-------------------------------")


def testNAdditions(n, valRange = (-1000, 1000)):
    for i in range(n):
        x1 = random.uniform(valRange[0], valRange[1])
        y1 = random.uniform(valRange[0], valRange[1])
        x2 = random.uniform(valRange[0], valRange[1])
        y2 = random.uniform(valRange[0], valRange[1])
        testAddition(x1, y1, x2, y2)

def testAddition(x1, y1, x2, y2):
    vec1 = vectorArithmetic.vector(x = x1, y = y1)
    vec2 = vectorArithmetic.vector(x = x2, y = y2)
    addVec = vec1 + vec2
    print(f"Vec1: {vec1}")
    print(f":Vec2: {vec2}")
    print(f"addVec: {addVec}")
    print("-------------------------------")
