class Solution:
    def isPalindrome(self, x: int) -> bool:
        def reverse(num):
            newnum=0
            while num>0:
                digit=num%10
                newnum=newnum*10+digit
                num=num//10
            return newnum
        return reverse(x)==x