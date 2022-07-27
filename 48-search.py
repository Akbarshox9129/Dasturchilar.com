# Searching algorithms
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
