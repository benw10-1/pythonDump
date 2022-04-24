import numpy as np

s = "x^2+2x+1"
s = s.replace("-", "+-")
s = s.split("+")
for y in np.arange(-100, 100, ):
    total = 0
    num = str(y)
    for x in s:
        if "x" in x:
            if "^" in x:
                total += float(x.split("^")[0].replace("x", num))**float(x.split("^")[1])
            else:
                total += float(x.split("x")[0]) * float(num)
        else:
            total += float(x)

    print(num, ",", int(total))
