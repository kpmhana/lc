
class Solution:
    def twoSum(nums, target):
        d = {}
        for i in range(0, len(nums)):
            c = target - nums[i]
            
            # If c exists in d, then there is a compliment - at places d[c] and i
            if c in d.keys():   #didn;t put brackets
                # we found it
                print(i, d[c])
                return
            else:
                d[nums[i]] = i

            
        print("Not found")


Solution.twoSum([3,1,2,8,2],9)
