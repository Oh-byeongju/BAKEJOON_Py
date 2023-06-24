import sys
input = sys.stdin.readline

Work_list = []

for i in range(24):
    temp = list(map(str, input().split()))
    for j in temp:
        Work_list.append(j)
    if len(Work_list) == 24:
        break

cnt = 0
cnt += len(Work_list)

Re = Work_list.count('Re')
Pt = Work_list.count('Pt')
Cc = Work_list.count('Cc')
Ea = Work_list.count('Ea')
Tb = Work_list.count('Tb')
Cm = Work_list.count('Cm')
Ex = Work_list.count('Ex')

if cnt == 0:
    print('Re', Re, '0.00')
    print('Pt', Pt, '0.00')
    print('Cc', Cc, '0.00')
    print('Ea', Ea, '0.00')
    print('Tb', Tb, '0.00')
    print('Cm', Cm, '0.00')
    print('Ex', Ex, '0.00')
    print('Total', cnt, '1.00')
else:
    print('Re', Re, "{:.2f}".format(Re/cnt))
    print('Pt', Pt, "{:.2f}".format(Pt/cnt))
    print('Cc', Cc, "{:.2f}".format(Cc/cnt))
    print('Ea', Ea, "{:.2f}".format(Ea/cnt))
    print('Tb', Tb, "{:.2f}".format(Tb/cnt))
    print('Cm', Cm, "{:.2f}".format(Cm/cnt))
    print('Ex', Ex, "{:.2f}".format(Ex/cnt))
    print('Total', cnt, '1.00')