# BubbleSort
def BubbleSort(num):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]>num[j]:
                num[i],num[j]=num[j],num[i]
# InsertionSort
def InsertionSort(num):
    for i in range(1,len(num)):
        a=num[i]
        j=i-1
        while j>=0 and a<num[j]:
            num[j+1]=num[j]
            j-=1
        num[j+1]=a
# SelectionSort
def SelectionSort(num):
    for i in range(len(num)):
        min=i
        for j in range(min+1,len(num)):
            if num[j]<num[min]:
                min=j
        num[i],num[min]=num[min],num[i]
sonlar=[7,6,4,9,2,1,8,3,4,7,9,3]
#BubbleSort(sonlar)
#SelectionSort(sonlar)
InsertionSort(sonlar)
print(sonlar)