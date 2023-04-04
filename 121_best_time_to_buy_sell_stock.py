
class Solution:
    def maxProfit(self, prices) -> int:
        print(prices)

        profit = 0
        i = 0
        min = prices[i]
        max = prices[i]

        while(i+1 < len(prices)):

            if(prices[i] != 0  and prices[i] < min):
                min = prices[i]
                max = prices[i]

            if(prices[i+1] > max):
                max = prices[i+1]
                profit = max - min
                
            i = i + 1

        return profit



#p = [7,1,5,3,6,4,19,9]
#p = [1,7,6,4,3,18]
p = [3,2,6,5,0,3]
s1 = Solution
print(s1.maxProfit(s1,p))