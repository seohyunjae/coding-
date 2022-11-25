# 탑다운 방식
# import time
start_time = time.time()
#초기화
d = [0]*100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0: #만약 이미 계산을 하였다면?
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
print(d)
end_time= time.time()
print(end_time-start_time)
    