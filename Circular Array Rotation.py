#vars
n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
if k>n:
  k=k%n
def rotate(arr,k):
  temp=arr[n-k:]
  for x in range(1,n):
    a[n-x]=a[n-x-k]
  a[:k]=temp

rotate(a,k)

#Print at indexes
for a0 in range(q):
    m = int(input().strip())
    print(a[m])
