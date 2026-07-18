class TimeMap:

    def __init__(self):
        self.dic={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key]=[]
        self.dic[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        x=self.dic[key]
        n=len(x)-1
        if timestamp >= x[n][0]:
            return x[n][1]
        elif timestamp < x[0][0]:
            return ""



        r,l=n,0
        while r!=l+1 and len(x)!=1:
            mid=(l+r)//2
            if x[mid][0]>=timestamp:
                r=mid
            else:
                l=mid
        if x[r][0]<=timestamp :
            return x[r][1]
        else:
            return x[l][1]

        
