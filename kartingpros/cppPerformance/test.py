import cppyy
cppyy.include("CarCalculations.h")
cppyy.load_library("CarCalculations")
from cppyy.gbl import CarCalculations
import math
import time

carCalc = CarCalculations()
# print(carCalc.calcRad(-23))

nums = []
for i in range(0,500):
    nums.append(-i)

cppTime = 1
pyTime = 1

def cppCalc():
    start_time = time.time_ns()
    for x in nums:
        carCalc.calcRad(x)
    finish_time = time.time_ns()
    # cppTime+=1
    cppTime += (finish_time-start_time)

def pythonCalc():
    start_time = time.time_ns()
    for x in nums:
        math.sin(x)
    finish_time = time.time_ns()
    # print(cppTime)
    pyTime+=(finish_time-start_time)

for i in range(100):
    start_time = time.time_ns()
    for x in nums:
        carCalc.calcRad(x)
    finish_time = time.time_ns()
    # cppTime+=1
    cppTime += (finish_time-start_time)

    start_time = time.time_ns()
    for x in nums:
        math.sin(x)
    finish_time = time.time_ns()
    # print(cppTime)
    pyTime+=(finish_time-start_time)


print(f"Python time is {pyTime/100}")
print(f"C++ time is {cppTime/100}")