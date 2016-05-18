# Numpy og matplotlib for å lage fremvise graf
import numpy as np
import matplotlib.pyplot as plt
# Timeit for for å registrere tid
from timeit import Timer

def build_list(n):
 return list(range(n))

def build_dict(n):
 return {i: str(i ) for i in range(n)}

def inx(x,n):
 str(0) in x
 str(n//2) in x
 str(n-1) in x
 str("a") in x
 
timeList = Timer("inx(x,n)",
                 "from __main__ import n, build_list, inx; x = build_list(n)")

timeDict = Timer("inx(x,n)",
                 "from __main__ import n, build_dict, inx; x = build_dict(n)")

value_list = []
value_dict = []

print("N", "\t", "List", "\t", "Dict")
for size in range(1000, 100000+1, 5000):
 n = size
 #Repeat 10x10 times (100 times)
 list_secs = timeList.repeat(10,10)
 dict_secs = timeDict.repeat(10,10)
 print(n, "\t", min(list_secs), "\t", min(dict_secs))
 
 value_list.append(min(list_secs))
 value_dict.append(min(dict_secs))
 
 xList = [1000,6000,11000,16000,21000,26000,31000,36000,41000,46000,51000,56000,61000,66000,71000,76000,81000,86000,91000,96000]
 yList = value_list

 xDict = [1000,6000,11000,16000,21000,26000,31000,36000,41000,46000,51000,56000,61000,66000,71000,76000,81000,86000,91000,96000]
 yDict = value_dict

plt.plot(xList, yList, label='List time')
plt.plot(xDict, yDict, 'ro', label='Dictionary time')

plt.axis([0, 100000, 0, max(value_list) + 0.2])
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Time it test')
plt.legend()
 
plt.show()