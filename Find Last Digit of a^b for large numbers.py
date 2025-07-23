import math
class Solution:
    def getLastDigit(self,a,b):
        # code here 
        self.a=a
        self.b=b
        int_a = int(self.a)
        int_b = int(self.b)
        power=pow(int_a,int_b,10)
        return power
