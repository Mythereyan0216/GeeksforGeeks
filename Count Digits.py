class Solution:
    def evenlyDivides(self, n):
        self.n=n
        count=0
        n1=n
        while n!=0:
            l_d=n%10
            if(l_d==0):
                pass
            elif(n1%l_d==0):
                count+=1
            n=n//10
        return count
