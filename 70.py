f0=1
f1=2
n=3
for i in range(n-2):
    f0,f1=f1,f0+f1
print (f1)