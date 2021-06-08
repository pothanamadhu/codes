n=int(input())
data=list(map(int,input().split()))
p=int(input())
k=0
if data.count(p)>1:
      print(True)
      for i in range(n):
            if data[i]==p:
                  k=k+1
            if k==2:
                  print(i)
                  break
else:
      print(False)

