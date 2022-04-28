#Stephen Ingersoll
#Data Structures Course Project Spring 2022
#Samah Senbel

import math

temperature = []
for i in range(0,10):
    t = float(input())
    temperature.append(t)

    n = len(temperature)

    average = sum(temperature)/len(temperature)

    r = 0
    for i in temperature:
        r = r + pow(i-average,2)

    stdev = math.sqrt(r/n)

    if (stdev <= 1):
        print("Comfy")
    else:
        print("Not Comfy")
