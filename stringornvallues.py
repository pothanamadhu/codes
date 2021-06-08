st=input()#
sr=input()#
b={}
d={}
n=0
for i in st:#
      if i not in d.keys() :
            b[i]=1
      else:
            b[i]+=1
for i in sr:
      if i not in d.keys():
            d[i]=1
      else:
            d[i]+=1
for k in b.keys():#i
      for q in d.keys():
            if k==q and b[k]==d[q]:
                  n=n+d[q]
if len(st)==len(sr) and len(st)==n:
      print(True)
else :
      print(False)
            


      
