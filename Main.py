import random
import InsertionSort as insS
import MergeSort as merS
import CountingSort as couS
from timeit import default_timer as timer


n=int(input("Insert list dimension: "))
A = []
B = []
C = []
for i in range(0,n):
    val = random.randint(0, 100)
    A.append(val)
    B.append(val)
    C.append(val)
Abest = []
Bbest = []
Cbest = []
for j in range(0,n):
    Abest.append(j)
    Bbest.append(j)
    Cbest.append(j)
Aworst = []
Bworst = []
Cworst = []
for z in range(n-1,-1,-1):
    Aworst.append(z)
    Bworst.append(z)
    Cworst.append(z)

start=timer()
insS.insertionSort(A)
end=timer()
print("Insertion sort random: "+str(end-start))
start=timer()
insS.insertionSort(Abest)
end=timer()
print("Insertion sort best: "+str(end-start))
start=timer()
insS.insertionSort(Aworst)
end=timer()
print("Insertion sort worst: "+str(end-start))

start=timer()
merS.mergeSort(B,0,n-1)
end=timer()
print("Merge sort random: "+str(end-start))
start=timer()
merS.mergeSort(Bbest,0,n-1)
end=timer()
print("Merge sort best: "+str(end-start))
start=timer()
merS.mergeSort(Bworst,0,n-1)
end=timer()
print("Merge sort worst: "+str(end-start))

R = []
for k in range(0,n):
    R.append(0)
m=max(C)
start = timer()
Result=couS.countingSort(C,R,m)
end=timer()
print("Counting sort random: "+str(end-start))
