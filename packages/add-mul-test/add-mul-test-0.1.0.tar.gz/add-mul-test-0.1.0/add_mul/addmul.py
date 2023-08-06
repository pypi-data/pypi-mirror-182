
#import library
import numpy as np

class mul_add():

    def __init__(self,num):
        # paramaeter : num - Number to multiply with 
        self.mul = num
        pass
    def addnmul(self,num1,num2):
        # input parameter 1: num1
        # input parameter 2: num2
        
        """
        ### add the 2 parameter and multiply by the parameters in the class
        """
        result1 = np.add(num1,num2)
        result = np.dot(result1,self.mul)
        return result