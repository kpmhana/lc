
class Solution:
    def twoSum(nums, target):
        d = {}
        #for i in range(0, len(nums)):
        for i, val in enumerate(nums):
            c = target - val
            
            # If c exists in d, then there is a compliment - at places d[c] and i
            if c in d.keys():   #didn;t put brackets
                # we found it
                return([d[c],i])
            else:
                d[val] = i

        return([])


print(Solution.twoSum([3,1,2,8,2],9))


""" 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums=sorted(nums)
        i=0
        j=len(nums)-1
        while(sorted_nums[i]+sorted_nums[j]!=target):
            if sorted_nums[i]+sorted_nums[j]<target:
                i+=1
            else:
                j-=1
        first_val=sorted_nums[i]
        second_val=sorted_nums[j]
        one=nums.index(first_val)
        nums[one]=sum(nums)
        return [one,nums.index(second_val)] 
"""