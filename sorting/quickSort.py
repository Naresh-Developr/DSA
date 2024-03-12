import random 


def QuickSort(arr):

    if (len(arr)<1):   #base condition
        return arr
    pivot = random.choice(arr)

    left = [i for i in arr if i<pivot]
    right = [i for i in arr if i>pivot]
    mid = [i for i in arr if i==pivot]

    # for i in arr:
    #     if pivot == i:
    #         mid.append(i)

    # for i in arr:
    #     if(i<pivot):
    #         left.append(i)

    # for i in arr:
    #     if(i>pivot):
    #         right.append(i)
    
    return QuickSort(left) + mid+ QuickSort(right)
    

    
    

    


arr = [9,8,7,6,5,4,3,2]

out = QuickSort(arr)
print(out)