
def selectionSort(arr):
    l = len(arr)
    i=0
    for i in range(i,l-1):
        ind = min(arr,i,l-1)
        arr[i],arr[ind] = arr[ind],arr[i]
    return arr

        


def min(arr,start,end):
    min_index = start
    min_value = arr[start]
    for i in range(start,end+1):
        if min_value > arr[i]:
            min_value = arr[i]
            min_index = i
    return min_index

a = [6,5,4,3,2,1,0]
value = selectionSort(a)
print(value)