def bubble(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

a = list(range(10,0,-1))

v= bubble(a)
print(v)