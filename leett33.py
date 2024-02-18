def search(nums,target):
    def peak(nums):
            start = 0
            end = len(nums)-1

            while start<=end:
                mid = (start+end)//2

                if mid < len(nums)-1 and nums[mid] > nums[mid+1]:
                    return mid
                if nums[mid] < nums[start]:
                    end = mid -1
                else:
                    start = mid+1
            return len(nums)-1

    peak_value = peak(nums)

    def binsearch(target,nums,start,end):

        while start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return -1
 
    if target < nums[0]:
        return binsearch(target,nums,peak_value+1,len(nums)-1)
    else:
        return binsearch(target,nums,0,peak_value)
    
num = [4,5,6,7,0,1,2]
target = 0
value = search(num,target)

print(value)