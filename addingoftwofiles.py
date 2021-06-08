import fpdf
import csv
import os
d="path"
parent="C:\Python33"
pat=os.path.join(parent,d)
data=os.listdir(pat)
new=[]
for i in range(len(data)):
               with open (data[i]) as f1:
                        dirc=list(csv.reader(f1))
                        for j in range(len(data)):
                              new.append(j)
print(new)
               
               


      
      
