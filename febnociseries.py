def gen_fib(f,l):
      a,b,c=0,1,0
      if f==0:
            print(a,b,end=" ")
      if f==1:
            print(b,end=" ")
      i=3
      while c<=l:
            c=a+b
            a=b
            b=c
            if  c>=f and c<=l:
                  print(c,end=" ")
f,l=map(int,input().split())
gen_fib(f,l)
