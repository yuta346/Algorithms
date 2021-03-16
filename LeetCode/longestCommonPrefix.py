# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         arr = strs
#         prefix_list = []
#         for i in range(len(arr)-1):
#             print(arr[i][i])
#             print(arr[i+1][i+1])
#             if arr[i][i] == arr[i+1][i+1]:
                
                
#                 prefix_list.append(i)

#         print(prefix_list)


# s = Solution()
# li = ["flower","flow","flight"]
# print(s.longestCommonPrefix(li))

list1 = ['Yuta', 'Ryan', 'Luke', 'Padome']
list2 = ['Hagiwara', 'Hasegawa', 'Furnival', 'Amidara']
list3 = [1,3,5,7,9]
list4 = [2,4,6,8,10]

zi = zip(list1, list2)
print(list(zi))

zi2 = list(zip(list1, list3))
print(zi2)

for a,b in zip(list1, list2):
    print(a,b)

dict_zip = dict(zip(list2, list4))
print(dict_zip)

zi3 = list(zip(list3, list4)); print(zi3)

