class Solution(object):
    def largestOddNumber(self, num):
        n=len(num)
        lastseenodd=-1
        if int(num[-1])%2!=0:
            return num
        else:
            for i in range(n):
                if int(num[i])%2!=0:
                    lastseenodd=i
        if lastseenodd==-1:
            return ""
        else:
            return num[:lastseenodd+1]
        