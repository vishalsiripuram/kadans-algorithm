from sys import maxsize
def maxsub(arr,n):
    Max_S=-(maxsize)
    Max_End=0
    for i in range(n-1):
        Max_End+=arr[i]
        if Max_End<arr[i]:
            Max_End=arr[i]
        elif Max_S<Max_End:
            Max_S=Max_End
    return Max_S
arr=[]
n=int(input("enter size of array"))
for i in range(n):
    ele=int(input())
    arr.append(ele)
print(arr)
print(maxsub(arr,n))