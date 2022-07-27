# Searching algorithms
# Linear search
def LinearSearch(nums,x):
    for i in range(len(nums)):
        if nums[i]==x:
            return i
    return -1
numbers=[1,5,6,1,9,7]
n=int(input("n= "))
if LinearSearch(numbers,n)!=-1:
    print(n,"qiymati",LinearSearch(numbers,n),"-indexda joylashgan")
else:
    print("Bunday qiymat yo'q")
# Binary search
def BinarySearch(nums,l,r,x):
    if r>=l:
        mid=l+(r-l)//2
        if nums[mid]==x:
            return mid
        elif nums[mid]<x:
            return BinarySearch(nums,mid+1,r,x)
        else:
            return BinarySearch(nums,l,mid-1,x)
    else:
        return "Topilmadi"
ls=[-1,5,9,11,25]
print(BinarySearch(ls,0,len(ls)-1,11))
