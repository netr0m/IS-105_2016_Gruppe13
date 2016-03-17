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

print("N", "\t", "List", "\t", "Dict")
for size in range(1000, 100000+1, 5000):
 n = size
 list_secs = timeList.repeat(5,5)
 dict_secs = timeDict.repeat(5,5)
 print(n, "\t", min(list_secs), "\t", min(dict_secs))