l=[]
i=int(input())
for j in range(0,i):
  k=list(input())
  l.append(k)
m=zip(*l)
n=list(m)
for j in n:
  if(len(j)==j.count(j[0])):
    print(j[0],end=" ")
  else:
    break
