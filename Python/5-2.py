from collections import deque
q = deque()
q.append(5)
q.append(4)
q.append(4)
q.append(2)
q.popleft()

print(q)
