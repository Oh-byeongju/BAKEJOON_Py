import sys
input = sys.stdin.readline

N = int(input())
print(2**N - 1)

def recur(N, start, end, sub):
    if N == 1:
        print(start, end)
        return

    recur(N - 1, start, sub, end)
    print(start, end)
    recur(N - 1, sub, end, start)

recur(N, 1, 3, 2)