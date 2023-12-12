# 字符串有三种编辑操作:插入一个英文字符、删除一个英文字符或者替换一个英文字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

# 示例 1:

# 输入: 
# first = "pale"
# second = "ple"
# 输出: True

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(second)-len(first))>1:
            return False
        
        elif len(second)==len(first):
            # 替换一个英文字符的情況
            difference=0
            for i in range(len(first)):
                if first[i]!=second[i]:
                    difference+=1
            if difference>1:
                return False
            else:
                return True
        else:
            # 插入一个英文字符、删除一个英文字符
            # if len(second)>len(first):
            #     for index in range(len(first)):
            #         if first[index] not in second:
            #             return False
            # else:
            #     for index in range(len(second)):
            #         if second[index] not in first:
            #             return False
            #  没有考虑乱序情况
            
            
            # difference=0
            # if len(second)>len(first):
            #     for index in range(len(second)):
            #         if second[:index]+second[index+1:] in first:
            #             return True
            # else:
            #     for index in range(len(first)):
            #         if first[:index]+first[index+1:] in second:
            #             return True
            # return False
            
            quick=0
            slow=0
            if len(second)>len(first):
                # 快指针对应second，慢指针对应first
                while quick<len(second) and slow<len(first):
                    if first[slow]==second[quick]:
                        slow+=1
                        quick+=1
                    else:
                        quick+=1

            else:
                # 快指针对应first，慢指针对应second
                while quick<len(first) and slow<len(second):
                    if second[slow]==first[quick]:
                        slow+=1
                        quick+=1
                    else:
                        quick+=1
                
            if quick-slow>1:
                return False
            
            return True             

if __name__=="__main__":
    solution=Solution()
    # first = "pale"
    # second = "ple"
    first = "teacher"
    second = "taches"
    # first = "a"
    # second = "ab"
    print(solution.oneEditAway(first,second))