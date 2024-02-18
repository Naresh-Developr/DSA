array = [1,2,3,4,5,6,7,8,9,0]
target = 0

for i in range(len(array)):
    if target == array[i]:
        print(f"Element found in the index of {i}")
        break