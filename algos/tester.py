import concurrent.futures as cf
import time
import random

ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dict1 = {}


for x in ar:
    dict1[x] = 0

while True:
    try:
        dict1[random.choice(ar)] += 1
    except:
        break
total = 0
for x in dict1:
    total += dict1[x]

for x in dict1:
    print(str(x) + ":" + str(dict1[x]/total))

"""executor = cf.ThreadPoolExecutor(max_workers=1)

while t_f_s >"""