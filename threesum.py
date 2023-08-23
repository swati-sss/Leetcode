def three_sum(nums):
    ans = []
    nums.sort()
    for i in range(0,len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        j = i+1
        k = len(nums)-1
        while j<k:
            total = nums[i]+nums[j]+nums[k]
            if total<0:
                j+=1
            elif total>0:
                k-=1
            else:
                triplet = (nums[i], nums[j], nums[k])
                ans.append(triplet)
                j+=1
                k-=1
                while j<k and nums[j]== nums[j-1]:
                    j+=1
                while j<k and nums[k]==nums[k+1]:
                    k-=1
    return ans
numbers = [-1,0,1,2,-1,-4]
print(three_sum(numbers))
