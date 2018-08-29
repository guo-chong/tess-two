def adjustNode(arr,node,len):
    temp=arr[node]
    k=node*2+1
    while(k<len):
        if(k+1<len and arr[k+1]>arr[k]):
            k+=1
        if(arr[k]>temp):
            arr[node]=arr[k]
            node=k
            k = node * 2 + 1
        else:break
    arr[node]=temp
def heapSort(arr):
    for i in range(len(arr)//2-1,-1,-1):
        adjustNode(arr,i,len(arr))
    for j in range(len(arr)):
        arr[0],arr[len(arr)-j-1]=arr[len(arr)-j-1],arr[0]
        adjustNode(arr,0,len(arr)-j-1)


def quickSort(arr,start,end):
    if(start>=end):return
    temp=arr[start]
    p1,p2=start,end
    while(p1<p2):
        while(p1<p2 and arr[p2]>=temp):p2-=1
        while(p1<p2 and arr[p1]<=temp):p1+=1
        arr[p1],arr[p2]=arr[p2],arr[p1]
    arr[start],arr[p1]=arr[p1],arr[start]
    quickSort(arr,start,p1-1)
    quickSort(arr,p1+1,end)

def merge(arr,start,mid,end,result):
    p1,p2,pr=start,mid+1,start
    while(p1<=mid and p2<=end ):
        if(arr[p1]<arr[p2]):
            result[pr]=arr[p1]
            p1+=1
            pr+=1
        else:
            result[pr]=arr[p2]
            p2+=1
            pr+=1
    if(p1<=mid):result[pr:pr+mid-p1+1]=arr[p1:mid+1]
    if(p2<=end):result[pr:pr+end-p2+1]=arr[p2:end+1]
    arr[start:end+1]=result[start:end+1]

def mergeSort(arr,start,end,result):
    if(end<=start):return
    else:
        mid=(start+end)//2
        mergeSort(arr,start,mid,result)
        mergeSort(arr,mid+1,end,result)
        merge(arr,start,mid,end,result)


class BSTNode:
    def __init__(self,val):
        self.val=val
        self.left,self.right=None

class BSTree:
    def __init__(self):
        self.root=None
    def add(self,val):
        if self.root==None:
            self.root=BSTNode(val)
            return
        else:
            p=self.root
            while True:
                if val<p.val :
                    if p.left!=None:p=p.left
                    else:
                        p.left=BSTNode(val)
                        return
                else:
                    if p.right!=None:p=p.right
                    else:
                        p.right=BSTNode(val)
                        return

def bucketSort(arr):
    l=len(arr)
    minVal=min(arr)
    maxVal=max(arr)
    div=max(1,(maxVal-minVal)//l)
    bucket=[[] for _ in range(l+1)]
    for v in arr:
        idxB=int((v-minVal)//div)
        print(idxB)
        tempBucket=bucket[idxB]
        if len(tempBucket)==0:
            tempBucket.insert(0,v)
            continue
        p1,p2=0,len(tempBucket)-1
        mid=(p1+p2)//2
        while True:
            if(p2<=p1):
                if(v>=tempBucket[p1]):
                    tempBucket.insert(p1+1,v)
                    break
                else:
                    tempBucket.insert(p1,v)
                    break
            else:
                if(v>tempBucket[mid]):
                    p1=mid+1
                elif(v<tempBucket[mid]):
                    p2=mid-1
                else:
                    tempBucket.insert(mid,v)
                    break
                mid=(p1+p2)//2
    result=[]
    for b in bucket:
        result+=b
    return result


def binaryInsert(arr,val):
    if len(arr)==0:arr.insert(0,val)
    else:
        p0,p1=0,len(arr)-1
        mid=(p0+p1)//2
        while True:
            if p1<=p0:
                if val<=arr[p0]:
                    arr.insert(p0,val)
                    break
                else:
                    arr.insert(p0+1,val)
                    break
            else:
                if(arr[mid]<val):
                    p0=mid+1
                    mid=(p0+p1)//2
                elif(arr[mid]>val):
                    p1=mid-1
                    mid=(p0+p1)//2
                else:
                    arr.insert(mid,val)
                    break




# def match(s,p):
#     ps=0
#     for i in range(len(p)):
#         if ps==0:







arr=[2,2,5,6,9,7,2,5,4,0,3.5,6,3.5]
result=[]
for x in arr:
    binaryInsert(result,x)

r=bucketSort(arr)
print(r)






