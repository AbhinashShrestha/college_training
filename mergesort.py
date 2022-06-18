#merge sort function
our_array:list=[1,3,5,7,9,2,4,6]
def merge(left_array,right_array,arr):
    n1=len(left_array)
    n2=len(right_array)
    i=j=k=0
    while i<n1 and j<n2:
        if left_array[i]<right_array[j]:
            arr[k]=left_array[i]
            i+=1
        else:
            arr[k]=right_array[j]
            j+=1
        k+=1
    while i<n1:
        arr[k]=left_array[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]=right_array[j]
        j+=1
        k+=1

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left,right,arr)
merge_sort(our_array)
print(our_array)