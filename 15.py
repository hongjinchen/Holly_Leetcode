nums = [0, 0, 0, 0]
nums.sort()
if nums[0] + nums[1] + nums[2] > 0:
    print([])
if nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3] < 0:
    print([])
result = []
for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    if nums[i] + nums[i + 1] + nums[i + 2] > 0:
        break
    if nums[i] + nums[len(nums) - 1] + nums[len(nums) - 2] < 0:
        continue
    third = len(nums) - 1
    target = -nums[i]
    for j in range(i + 1, len(nums) - 1):
        if nums[j] == nums[j - 1] and i!=j - 1:
            continue
        while j < third and nums[j] + nums[third] > target:
            third -= 1
        if j == third:
            break
        if nums[j] + nums[third] == target:
            result.append([nums[i], nums[j], nums[third]])
print(result)