"""
About the problem :
Given:

    There will be given two sorted arrays and their lengths respectively.
    Need to merge the given two sorted arrays in same place .[[should not create a seperate array to return]] 

Approach:

    To deal with this problem we can use three pointer approach.
    but we should not create a seperate array.
    so we can return the array1 after merging the second array
    need to add some space to add elements in array add like arr1 = [1,2,3,4,0,0,0,0]
    0--------> represents the space to add those places were access by another variable in this case k
    last index of array1 = len-1 --------> i
    last index of arry2 =  len-1 --------> j
    so the last index of k is length of arr1 + arr2 - 1  \\ k = [[m+n-1]]
    run the loop until there will be no elements in second sorted array.
    compare : arr1[i]>arr2[j]:
                arr1[k] = arr1[i]
            if this happens decrement the position of i by 1
            else
                arr1[k] = arr2[j]
            if this happens decrement the position of j by 1
    after checking the condition decrement the k by 1.

    return array1.


"""
def merge(nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1

        while j>=0:
            if nums1[i]>nums2[j]:
                nums1[k] = nums1[i]
                i=i-1
            else:
                nums1[k] = nums2[j]
                j = j-1
            k = k-1
        return nums1