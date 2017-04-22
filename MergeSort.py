def mergeSort(A,p,r):
    if p<r:
        q=(p+r)//2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,r,q)

def merge(A,p,r,q):
    n1=q-p+1
    n2=r-q
    L=[]
    R=[]
    for i in range(0,n1):
        L.append(A[p+i])
    for j in range(0,n2):
        R.append(A[q+j+1])

    L.append(-1)
    R.append(-1)
    i=0
    j=0
    for z in range(p,r+1):
        if (L[i]<=R[j] and L[i]!=-1) or (L[i]>R[j] and R[j]==-1):
            A[z]=L[i]
            i=i+1
        else:
            A[z]=R[j]
            j=j+1