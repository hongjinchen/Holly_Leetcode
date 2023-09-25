# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

 
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        answer_list=[]
        for item in strs:
            if answer_list==[]:
                answer_list.append([item])
            else:
                sublist=self.isAnagram(item,answer_list)
                if self.isAnagram(item,answer_list)==[]:
                    answer_list.append([item])
                else:
                    answer_list.remove(sublist)
                    sublist.append(item)
                    answer_list.append(sublist)
        
        return answer_list


    
    def isAnagram(self,item,answer_list):
        for index  in range(len(answer_list)):
            comparer=answer_list[index]
            if len(item)==len(comparer[0]):
                for j in item:
                    if j in comparer[0]:
                        continue
                    else:
                        break
                return comparer
        return []
            



if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))