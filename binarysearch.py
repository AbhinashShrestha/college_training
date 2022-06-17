sorted_array=[1,2,3,4,5,6,7,8,9,10]
target_element=3
first=0
last=len(sorted_array)-1
def binary_search(to_find,start,end):
    if start>end:
        return "Not in the array"
    middle=(start+end)//2
    if sorted_array[middle]==to_find:
        return "{sorted_array[middle]} was found"
    if sorted_array[middle]>to_find:
        return binary_search(to_find,start,middle-1)
    if sorted_array[middle]<to_find:
        return binary_search(to_find,middle+1,end)

print(binary_search(target_element,first,last))