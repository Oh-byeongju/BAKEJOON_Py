import sys
import math
input = sys.stdin.readline

A, B, V = map(int, input().split())

temp_V = V - A
temp_num = A - B

print(math.ceil(temp_V / temp_num)+1)