class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        hashmap={}
        for i in arr:
            bitrep=bin(i)[2:]
            summ=0
            for digits in bitrep:
                summ+=int(digits)
            hashmap[i]=summ
        res=sorted(arr,key=lambda x:(hashmap[x],x))
        return res



        