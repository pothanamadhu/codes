n=int(input())
temp=n
c=s=e=p=0
while n:
      n=n//10
      c=c+1
k=c
n=temp
l=n%10#4
f=n//pow(10,c-1)#1
while n:#1234
      r=n//pow(10,c-1)#1
      n=n%pow(10,c-1)#234
      if e==0:
            r=l##4
      if e==(k-1):
            r=f
      s=s*10+r#4
      e=e+1#1
      c=c-1#3
l=0
while s:
      r=s%10
      s=s//10
      l=l*10+r

print(l)
      
