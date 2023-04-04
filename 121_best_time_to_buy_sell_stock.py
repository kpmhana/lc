
class Solution:
    def maxProfit(self, prices) -> int:
        print(prices)

        profit = 0
        i = 0
        min = prices[i]
        max = prices[i]

        while(i+1 < len(prices)):

            if(prices[i] < min):
                min = prices[i]
#                max = prices[i]

            if(prices[i+1]-min > profit):
                max = prices[i+1]
                profit = max - min
                
            i = i + 1

        return profit
    
    def maxProfit2(self, prices) -> int:
        print(prices)

        profit = 0
        min = prices[0]

        for p in prices:
            if(p < min):
                min = p
            profit = max(profit, p-min)

        return profit
    




p = [7,1,5,3,6,4,19,9] #18
#p = [1,7,6,4,3,18] #17
#p = [3,2,6,5,0,3] #4
#p = [2,1,2,1,0,1,2] #2

s1 = Solution
print(s1.maxProfit2(s1,p))