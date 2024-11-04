class Calculator:
    def sum(self, a,b):
        result = a + b
        return result
    
    def sub(self,a,b):
        result = a - b
        return result
    
    def mult(self,a, b):
        return a * b
    
    def div(self,a, b):
        if (b == 0):
            raise ArithmeticError('Деление на ноль')
        return a / b

    def pow(self,a, b):
        return a ** b

    def avg(self,nums):
        if len(nums) == 0:
            return 0
        s = 0
        for num in nums:
            s = self.sum(s,num)  
        l = len(nums)
        return s/l    