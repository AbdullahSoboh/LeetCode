class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    # Create an empty dictionary to store indices of elements
        indices = {}
    
    # Iterate through the array
        for i in range(len(nums)):
          # Check if the complement is in the dictionary
          complement = target - nums[i]
          if complement in indices:
             # If complement is found, return the indices of the two elements
                return [indices[complement], i]
        
        # Add the index of the current element to the dictionary
          indices[nums[i]] = i
    
    # If no solution is found, return an empty list
        return []

        