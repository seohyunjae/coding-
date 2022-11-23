a = list(map(int,input().split()))
remove_set ={0}


result = [k for k in a if k not in remove_set]
result.sort()
for k in result:
  print(k, end='')
print('')
  

for i in a:
  print(i, end='')
