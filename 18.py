def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
    result = list()
    length = len(nums)
    if not nums or length < 4:
        return result
    nums.sort
    for i in range(length - 3):
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1]:
            continue
        for j in range(i + 1, length - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:  # 当j的值与前面的值相等时忽略
                continue
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] < target:
                continue
            left = j + 1
            right = length - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return result
