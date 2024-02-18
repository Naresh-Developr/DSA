array = [5,7,7,8,8,10]

target = 8

start = 0
end = len(array)-1


def search(array ,target, flag):
        start=0
        end = len(array)-1
        ans = -1
       
        while start<=end:
            middle = (start+end)//2
            if array[middle] == target:
                ans = middle
                if flag:
                    end = middle-1
                else:
                    start = middle+1
            elif target>array[middle]:
                start = middle+1
            else:
                end = middle-1
        return ans

print(search(array,target,True) ,search(array,target,False))