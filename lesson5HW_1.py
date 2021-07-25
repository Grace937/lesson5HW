q=int(input('學生數量?'))
ml=[]
a=0
for i in range(q):
    w=int(input('成績?'))
    ml.append(w)
    a=a+w
print(ml)
print(a/q)

