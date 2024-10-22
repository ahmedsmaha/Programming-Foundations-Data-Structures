from collections import deque

def binary_numbers(n):
    if n <= 0:
        return
    queue = deque()
    queue.append(1)
    for _ in range(n):
        binary = queue.popleft()
        print(binary)
        queue.append(binary * 10)
        queue.append(binary * 10 + 1)

binary_numbers(6)