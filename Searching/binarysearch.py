nums = [1,3]

start = 1
end = len(nums)-1
target = 3

def search(arr,start,end,target):
    while start<=end:
        mid = (start+end)//2

        if arr[mid]==target:
            return mid
        if arr[mid]>target:
            start = mid+1
        else:
            end = mid-1
    return -1

value = search(nums,start,end,target)
print(value)