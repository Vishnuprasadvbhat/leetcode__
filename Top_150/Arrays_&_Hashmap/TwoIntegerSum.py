nums=[4,5,6]
target=10
# pre_v = {}
# list = []
# for index, element in enumerate(nums):
#     diff = target - element
#     print(element,'--->', diff)
#     if diff in pre_v:
#         print([pre_v[diff],index])
#     pre_v[element] = index
# print(pre_v)




## brute force approach
length = len(nums)
print(length)
for i in range(length-1):
    for j in range(i+1,length):
        if nums[i] + nums [j] == target:
            print(i,j)