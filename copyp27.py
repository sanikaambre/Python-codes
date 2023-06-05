import copy
nums_x=[1,[2,3,4]]
print("Original list:",nums_x)
nums_y=copy.copy(nums_x)
print("\n Copy of the said list")
print(nums_y)
print("\n Change the value of an element of the original list:")
nums_x[1][1]=10
print(nums_x)
print("\n Second list:")
print(nums_y)
nums=[[1],[2]]
nums_copy=copy.copy(nums)
print("\n Original list:")
print(nums)
print("\n Copy of the said list")
print(nums_copy)
print("\n Change the value of an element of the original list:")
nums[0][0]=0
print("\n First list")
print(nums)
print("\n Second list:")
print(nums_copy)
