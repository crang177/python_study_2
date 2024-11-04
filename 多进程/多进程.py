from  multiprocessing.dummy import Pool
import time

def test(n):
    return n**n

b=[]
t1=time.time()
for i in range(1110):
    b.append(test(i+1))
#print(b)
print(time.time()-t1)

print()
t2=time.time()
ls=[]
for i in range(1110):
    ls.append(i+1)
pool=Pool(3)
res=pool.map(test,ls)
#print(res)
print(time.time()-t2)