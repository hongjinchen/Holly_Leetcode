class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        str_list=list(boxes)
        answer_list=[]
        for i in range(len(str_list)):
            number=0
            for k in range(len(str_list)):
                if str_list[k]=="1":
                    # 这里进行判断，减少计算的步骤
                    number=number+abs(k-i)
            answer_list.append(number)
        return answer_list

# class Solution:
#     def minOperations(self, boxes: str) -> list[int]:
#         res = []
#         for i in range(len(boxes)):
#             count = 0
#             for j in range(len(boxes)):
#                 if boxes[j]=='1':
#                     count += abs(j-i)
#             res.append(count)
#         return res
if __name__ == "__main__":
    boxes = "010"
    new_solu=Solution()
    print(new_solu.minOperations(boxes))