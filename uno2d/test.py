_, _, k = input().split(" ")
k = int(k)
apt_pref = apt_size = {}
for x in input().split(" "):
    x = int(x)
    try:
        apt_pref[x] += 1
    except:
        apt_pref[x] = 0

for x in input().split(" "):
    x = int(x)
    try:
        apt_size[x] += 1
    except:
        apt_size[x] = 0

count = 0

for x in apt_pref:
    if x in apt_size:
        if x - k < apt_size[x]

print(count)
