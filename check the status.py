class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        self.a=a
        self.b=b
        self.flag=flag
        if(self.a>0 and self.b<0 and self.flag==False):
            return True
        elif(self.a<0 and self.b>0 and self.flag==False):
            return True
        elif(self.a<0 and self.b<0 and self.flag==True):
            return True
        else:
            return False
s=Solution()
s.checkStatus(1,2,True)