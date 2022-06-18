import psycopg2
mydb=psycopg2.connect( 
    database="postgres",
    user="postgres",
    password="urawaja$010",
    host="localhost",
    port=5432,
)
cursor=mydb.cursor()
query='Select * from "Student"'
cursor.execute(query)
array=list(cursor.fetchall())
print(array)
print("Given data is:")
for x in array:
    print(x)
    
def merge_sort(array,index):
    if len(array)>1:
        mid=len(array)//2
        left=array[:mid]
        right=array[mid:]
        merge_sort(left,index)
        merge_sort(right,index)
        i=j=k=0
        
        while i<len(left) and j<len(right):
            if left[i][index]<right[j][index]:
                array[k]=left[i]
                i+=1
            else:
                array[k]=right[j]
                j+=1
            k+=1
            
        while i<len(left):
            array[k]=left[i]
            i+=1
            k+=1
        
        while j<len(right):
            array[k]=right[j]
            j+=1
            k+=1
            
merge_sort(array,3)
print("Sorted data by age is:")
for x in array:
    print(x)