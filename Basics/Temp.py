s = 'bef'
res = [s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
print(res)

s1= 'bef'
res=[]
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        res.append(s1[i:j])
print(res)

