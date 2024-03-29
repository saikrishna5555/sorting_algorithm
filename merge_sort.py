def merge_sort(arr):
    if len(arr)<=1:
        return

    #divide array into two halves
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    
    merge_sort(left)
    merge_sort(right)
    

    merge_two_list(left,right,arr)

def merge_two_list(left,right,arr):
    i=0
    j=0
    k=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1

    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1


    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
    

arr=[2,4,5,2,5,23,34,6,8,233,787,6]
merge_sort(arr)
print(arr)
