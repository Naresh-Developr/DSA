#Ascending Order ---------------------------------------->

array = [1,2,3,4,5,6,7,8,9]

target = 0

start = 0
end = len(array)-1


def binarySearch(start,end):
    while start<=end:

        middle = (start+end)//2

        if array[middle] == target:
            return middle
            break
        elif array[middle] < target :
            start = middle+1
        else :
            end = middle-1
    return -1

ans = binarySearch(start,end)
print(f"Element found at index of {ans}")
    
