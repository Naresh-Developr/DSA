class TrieNode:

    def __init__(self):
        self.children = {}
        self.IsEnd = False

class trie:
    
    def __init__(self):
        self.root = TrieNode()

    def add(self,word):
        currentNode = self.root;
        for character in word:
            if character not in currentNode.children:
                currentNode.children[character] = TrieNode()
            currentNode = currentNode.children[character]
        currentNode.IsEnd = True

    def search(self,word):
        currentNode = self.root;
        for character in word:
            if character not in currentNode.children:
                return False
            currentNode = currentNode.children[character]
        if currentNode.IsEnd==True:
            return True
        else:
            return False
        
    def remove(self,word):
        if not self.search(word):
            print("Word not found....")
            return 
        
        currentNode = self.root
        stack = []
        for character in word:
            stack.append(currentNode)
            currentNode = currentNode.children[character]
        currentNode.IsEnd = False

        while len(stack)>0:
            node = stack.pop()
            char = word[len(stack)]

            if not node.children[char].IsEnd and not node.children[char]:
                del node.children[char]
            else:
                break
        print("word removed")
t =  trie()
t.add("gold")
t.add("go")
t.search("go")
t.remove("gol")