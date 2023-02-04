import sys
import math
A, B, V = map(int, sys.stdin.readline().split())
up = (V-B)/(A-B)
print(math.ceil(up))