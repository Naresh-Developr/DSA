"""""
We created a dictionary data type in python 

Dictionaries in python are nothing but the hashTables.

"""


class hashMap:

    def __init__(self,size=10):
        self.size = size
        #print(self.size)
        self.hashlist = [None]*self.size
        print(self.hashlist) 

    def GetIndex(self,key):
        return hash(key)%self.size
    
    def Add(self,key,value):  #__setitem__ to acess this like dict syntax
        index = self.GetIndex(key)

        if self.hashlist[index] is None:
            self.hashlist[index] = [[key,value]]
            print(self.hashlist)
        else:
            #TODO dont allow duplicates to store in hashtables
            sublist = self.hashlist[index]
            for i,pairs in enumerate(sublist):
                if pairs[0]==key:
                    pairs[1] = value
                    print(self.hashlist)
                    return
            self.hashlist[index].append([key,value])
            print(self.hashlist)
            


    def get(self,key):  #__getitem__ to use the synatax of dict to find values 
        #TODO find the element in hastable
        index = self.GetIndex(key)

        if self.hashlist[index] is not None:
            sublist = self.hashlist[index]
            for i,pairs in enumerate(sublist):                
                if pairs[0] == key:
                    print(f"found in index of {i}")
                    return pairs[1]
            return "element not found"
                
        
    def delete(self,key):  #__eitem__ to use the synatacx of dict to delete values
        #TODO delete the element in hastable
        index = self.GetIndex(key)

        if self.hashlist[index]:
            sublist = self.hashlist[index]
            print(sublist)
            for i,pair in enumerate(sublist):
                print(pair)
                print(i)
                if pair[0]==key:
                    print("entered")
                    del sublist[i]
                    print(self.hashlist)
                    return
            return "from delete:element not found"





test = hashMap()
test.Add(1,"Naresh")
test.Add("age",21)
test.Add("name","naresh")
test.Add("age",22)
test.Add("name","karthi")
test.Add("age",23)
test.Add("name","kavin")
test.Add("age",24)
test.Add("name","naveen")
test.Add("age",25)
#test.get("name")
#test.Add("age","Tamil")
#test.delete("name")
#test.get("name")
#print(test.get("name")) 
#print(test.delete("e"))
#print(test.hashlist)

# print(hash("Naresh")%10)
# print(hash("suresh")%10)

print(test)
    