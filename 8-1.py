import time
start_time = time.time()
def fibo(x):
    if x == 1 or x ==2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(39))

end_time= time.time()
print(end_time-start_time)