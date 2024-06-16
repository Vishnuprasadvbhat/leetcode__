nums = [0,1,0,3,12]
list = []
for i in nums:
    if i ==0:
        nums.remove(i)
        list.append(i)
print([nums + list])