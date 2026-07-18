class Trie:  
    def __init__(self):    
        self.child={}
        self.word=False
class WordDictionary:

    def __init__(self):
        self.root=Trie()
        self.s="abcdefghijklmnopqrstuvwxyz"


    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.child:
                curr.child[c]=Trie()
            curr=curr.child[c]
        curr.word=True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for x in range(j,len(word)):
                if word[x]=='.':
                    for ch in cur.child.values():
                        if dfs(x+1,ch):
                            return True
                    return False
                else:
                    if word[x] not in cur.child:
                        return False
                    cur=cur.child[word[x]]
            return cur.word


        return dfs(0, self.root)