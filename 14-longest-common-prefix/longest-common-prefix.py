class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # f f f ans=> f , i[:j]
        if not strs:
            return ""
        ans=""
        curr=strs[0]
        n=len(strs)
        for i in range(len(curr)):
            char=curr[i]
            for j in range(1,n):
                if i>=len(strs[j]) or strs[j][i]!=char:
                    return ans
            ans+=char
        return ans




        