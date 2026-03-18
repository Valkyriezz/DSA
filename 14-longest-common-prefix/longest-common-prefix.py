class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # f f f ans=> f , i[:j]

        if not strs:
            return ""
        w = len(strs[0])
        ans=""
        n=len(strs)
        for i in strs:
            w = min(w,len(i))

        for i in range(w):
            ls = []
            for j in strs:
                ls.append(j[i])
            if len(set(ls)) == 1:
                ans+=ls[0]
            else:
                break

                
                
        return ans
                
            

            





            



        