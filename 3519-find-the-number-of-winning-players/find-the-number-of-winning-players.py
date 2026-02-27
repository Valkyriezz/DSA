class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        count=0
        hashmap={}
        for player,color in pick:
            if player not in hashmap:
                hashmap[player]=[color]
            else:
                hashmap[player].append(color)
        print(hashmap)
        for i in hashmap:
            hashmap2={}
            for color in hashmap[i]:
                if color in hashmap2:
                    hashmap2[color]+=1
                else:
                    hashmap2[color]=1
            freq=float("-inf")
            for val in hashmap2.values():
                if val>freq:
                    freq=val
            print(freq)
            if freq>i:
                count+=1
        return count

        