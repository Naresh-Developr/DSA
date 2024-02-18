def sort(arr):
    if len(arr) >1 :
        mid = len(arr)//2
        R = arr[mid:]
        L = arr[:mid]
        sort(R)
        sort(L)
        merge(L,R,arr)


def merge(l,r,arr):
    i=0
    j=0
    k=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            arr[k] = l[i]
            i = i+1
        else:
            arr[k] = r[j]
            j = j+1
        k = k+1

    while i<len(l):
        arr[k] = l[i]
        i += 1
        k += 1
    
    while j<len(r):
        arr[k] = r[j]
        j += 1 
        k += 1





if __name__ == '__main__':
    array = [7,6,5,4,3,2,1]
    print(f"Before: {array}")
    #test=[0,0,0,0,0,0,0]
    sort(array)
    print(f"After: {array}")