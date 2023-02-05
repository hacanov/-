class math:
    def __init__(self,a,b):
         self.a, self.b = a,b
    def addition(self):
         print( self.a+self.b)
    def multiplication(self):
         print( self.a*self.b)
    def division(self):
         print( self.a/self.b)
    def subtraction(self):
         print(self.a - self.b)
math_obj=Math(4,2)
print(' addition',math_obj.addition())
print(' multiplication',math_obj. multiplication())
print(' division',math_obj.division())
print(' subtraction',math_obj.subtraction())
