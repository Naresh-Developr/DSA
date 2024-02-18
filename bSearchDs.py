#Decesending Order--------------------------->
array = [9,8,7,6,5,4,3,2,1]
start = 0
end = len(array)-1
target = 7

def binarySearch(start,end):
    while start<=end:
        middle = (start+end)//2
        if target == array[middle]:
            return middle
        if target > array[middle]:
            end = middle-1
        if target < array[middle]:
            start = middle+1
    return -1

ans = binarySearch(start,end);
print(f"The Element found in the index of {ans} ")


