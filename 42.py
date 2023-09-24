class Solution:
    def trap(self, height: list[int]) -> int:
        water=0
        highest_level=max(height)
        current_level_index=[]
        # print(water)
        for i in range(highest_level):
            for index in range(len(height)):
                number=height[index]
                if number!=0:
                    current_level_index.append(index)
                    height[index]=number-1
            current_level_index.sort(reverse = True)
            current_water=current_level_index[0]-current_level_index[len(current_level_index)-1]+1-len(current_level_index)
            water=water+current_water
            current_level_index=[]

        return water
    
if __name__ == "__main__":
    height = [4,2,0,3,2,5]
    new_solu=Solution()
    print(new_solu.trap(height))