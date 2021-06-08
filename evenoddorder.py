def eoorder(data,n):
      e=0
      o=0
      k=0
      even=[]
      odd=[]
      for i in range(n):
            if(data[i]%2==0):
                  even.append(data[i])
                  e=e+1
            else:
                  odd.append(data[i])
                  o=o+1
      m=o
      for k in range(o):
            data[k]=even[k]
      for l in range(o,e+o):
            data[m]=odd[l-o]
            m=m+1
n=int(input())
data=list(map(int,input().split()))
eoorder(data,n)
for i in data:
      print(i,end=" ")
