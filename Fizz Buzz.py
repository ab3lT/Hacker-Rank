class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        tem = [None] * n
        for i in range(1 , n+1):
            
            if i % 3 == 0 and i % 5 == 0:
                tem[i - 1] = "FizzBuzz"
            elif i % 3 == 0 :
                tem[i - 1] = "Fizz"
            elif i % 5 == 0 :
                tem[i - 1] = "Buzz"    
            else:
                tem[i-1] = str(i)
        return tem