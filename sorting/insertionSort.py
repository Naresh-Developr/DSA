# non optimized -- check with 1,2,3,4,5,6,7
def insertion(arr):
    n = len(arr)
    #print(n)
    c =0

    for i in range(1,n):
        for j in range(i,0,-1):
            c += 1
            if arr[j]<arr[j-1]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
    return arr,c
        

a = [7,6,5,4,1,2,3]
#v = insertion(a)

#optimized -- check with the above input

def insertion_opt(arr):
    n = len(arr)
    count = 0
    for i in range(0,n):
        for j in range(i,0,-1):
            count += 1
            if arr[j]<arr[j-1]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else:
                break
    return arr, count

v = insertion_opt(a)
print(v[0])
print(v[1])
    