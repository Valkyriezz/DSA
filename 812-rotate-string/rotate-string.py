class Solution(object):
    def rotateString(self, s, goal):
        new=s+s
        print(new)
        if len(goal)!=len(s):
            return False
        if goal not in new:
            return False
        return True
        
        