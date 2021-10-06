import vectorArithmetic
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math


def plotVectorExponentiations(magnitude: float = math.pi, numpoints: int = 16, minAngle = 0, maxAngle = 2 * math.pi) -> None:
    vectors = []
    exponentiatedVectors = []
    angleRatios = []

    for i in range(numpoints + 1):
        θ = minAngle + i * (maxAngle - minAngle) / numpoints
        v = vectorArithmetic.Vector(θ=θ, magnitude=magnitude)
        vectors.append(v)
        #EtotheV = v.exp()
        EtotheV = v.exp_TaylorExpansion()

        if v.θ != 0:
            angleRatios.append([EtotheV.θ, v.θ])
        exponentiatedVectors.append(EtotheV)
    print("angle ratios, no adjustment for 0")
    print(angleRatios)
    print("max angle ratio:")
    print(max([i[0] for i in angleRatios]))
    print("min angle ratio:")
    print(min([i[0] for i in angleRatios]))
    # vectors.append(vectorArithmetic.Vector(θ=0, magnitude=1))

    x = []
    y = []
    for vec in vectors:
        x.append(vec.x)
        y.append(vec.y)
    plt.plot(x, y)

    for i in range(len(vectors)):
        vec = vectors[i]
        EtotheV = exponentiatedVectors[i]
        x = (EtotheV.x + vec.x, vec.x)
        y = (EtotheV.y + vec.y, vec.y)
        plt.plot(x, y)


    """
    for i in range(len(vectors)):
        vec = vectors[i]
        EtotheV = exponentiatedVectors[i]
        x = (0, vec.x)
        y = (0, vec.y)
        plt.plot(x, y)
    """






"""
ListList = [[0, 0, vectors[i].x, vectors[i].y] for v in vectors]
soa = np.array(ListList)

soaZip = zip(*soa)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(*soaZip)
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])
plt.show()
"""