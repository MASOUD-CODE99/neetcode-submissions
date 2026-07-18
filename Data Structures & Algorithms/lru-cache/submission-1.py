class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dic={}
        self.cap = capacity        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            temp_val=self.cache[key]
            self.cache.pop(key)
            self.cache[key]=temp_val
            return self.cache[key]



    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            self.cache.pop(key)
            self.cache[key]=value

        elif len(self.cache)==self.cap:
            last_key = list(self.cache.keys())[0]
            self.cache.pop(last_key)
            self.cache[key]=value

        else:
            self.cache[key]=value









        
