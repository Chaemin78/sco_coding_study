a = []
while len(a) !=9 :
    a.append(int(input()))

max = 0
index = 0

for i in a:
    if a[i] <= a[i+1]:
        continue
    if a[i] > a[i+1]:
        max = a[i]
        index = i