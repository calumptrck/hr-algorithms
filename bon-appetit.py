n, k = list(map(int,input().split(' ')))
costs = list(map(int,input().split(' ')))
charged = int(input())
actual = (sum(costs) - costs[k])//2
share = charged-actual
if (actual==charged):
    print('Bon Appetit')
else:
    print(share)
    