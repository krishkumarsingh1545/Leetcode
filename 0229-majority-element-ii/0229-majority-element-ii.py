class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2 = 0, 0
        el1, el2 = None, None
        for i in nums:
            if count1 == 0 and i != el2:
                count1 = 1
                el1 = i
            elif count2 == 0 and i != el1:
                count2 = 1
                el2 = i
            elif i == el1:
                count1+=1
            elif i == el2:
                count2+=1
            else: 
                count1-=1
                count2-=1
        ll = []
        frq, frq2 = 0, 0
        for i in nums:
            if i == el1:
                frq+=1
            if i == el2:
                frq2+=1
        k = len(nums)//3
        if frq > k: ll.append(el1)
        if frq2 > k: ll.append(el2)
        ll.sort()
        return ll