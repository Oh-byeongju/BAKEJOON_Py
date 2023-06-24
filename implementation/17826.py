import sys
input = sys.stdin.readline

score_list = list(map(int, input().split()))
my_score = int(input())

if my_score >= score_list[4]:
    print('A+')
elif my_score >= score_list[14]:
    print('A0')
elif my_score >= score_list[29]:
    print('B+')
elif my_score >= score_list[34]:
    print('B0')
elif my_score >= score_list[44]:
    print('C+')
elif my_score >= score_list[47]:
    print('C0')
else:
    print('F')
