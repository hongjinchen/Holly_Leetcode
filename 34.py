nums = [5, 7, 7, 8, 8, 10]
target = 7
##O(log n)暗示二分法,因为存在多个重复元素，所以需要使用两个二分法来确认边界
if target not in nums:
    print([-1, -1])
left, right = 0, len(nums) - 1
mid = (left + right) // 2
answer = [0, 0]
while nums[mid] < target:
    left = mid
    mid = (left + right) // 2
    # 如果 nums[mid] = traget，继续向右寻找右边界
if nums[mid] - 1 == target:
    answer = [nums[mid] - 1, 0]
if nums[mid] + 1 == target:
    answer = [nums[mid] - 1, nums[mid] + 1]
print(answer)
