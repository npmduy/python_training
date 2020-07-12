import os
import random
import matplotlib.pyplot as plt

# List of Points 1
listOfPoints1 = []

for i in range(1000):
    x = random.randint(1,100)
    y = random.randint(1,100)
    tup = (x,y)
    listOfPoints1.append(tup)

# List of Points 2
listOfPoints2 = []

for i in range(1000):
    x = random.randint(1,100)
    y = random.randint(1,100)
    tup = (x,y)
    listOfPoints2.append(tup)

# find intersection
set1 = set(listOfPoints1)
set2 = set(listOfPoints2)

if set1.isdisjoint(set2):
    intersection_ = 0
else:
    intersection_ = set1.intersection(set2)

# Draw graph
for x,y in listOfPoints1:
    if intersection_ != 0:
        if (x,y) in intersection_:
            plt.scatter(x,y,color='green')
        else:
            plt.scatter(x,y,color='red')
    else:
        plt.scatter(x,y,color='red')

for x,y in listOfPoints2:
    if intersection_ != 0:
        if (x,y) in intersection_:
            plt.scatter(x,y,color='green')
        else:
            plt.scatter(x,y,color='blue')
    else:
        plt.scatter(x,y,color='blue')

plt.show()