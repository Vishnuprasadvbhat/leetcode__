#
# array =[1,2,4,6]
# prefix_num = []
# prefix_num.append(array[0])
#
#
# for i in range (1,len(array)):
#     pnum = prefix_num[i] + array[i]
#     prefix_num.append(pnum)
# print(prefix_num[1::])

prefixSum = [0 for i in range(n + 1)]
