# Time : O(nlogn)
# Space: O(n)
# Leetcode:Yes
# Issues:None


# Trie solution


# sorting solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for i in nums:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1

        h2 = sorted(hmap.items(),key = lambda x: x[1], reverse = True) # desc sort on count
        
        res = [i for i,freq in h2[:k]]

        return res