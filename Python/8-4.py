#보텀 업 방식
d = [0]*1000

d[1] = 1
d[2] = 1
n = 991
for i in range(3, 992):
    d[i] = d[i-1] + d[i-2]

print(d[n])
