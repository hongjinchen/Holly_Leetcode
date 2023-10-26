# import sys

# for line in sys.stdin:
#     a = line.split()
#     sentence=str(a[0])

sentence="meili"
if len(sentence)<3:
        print(0)
    
if len(sentence)==3 and "mei" not in sentence:
        print(0)
elif len(sentence)==3 and "mei" in sentence:
        print(1)
    
number=0
new_sentence=sentence
index=0
isDelete=False

def getMei(self,index,new_sentence,isDelete):
        if "mei" in new_sentence:
            number+=1

        if index==len(new_sentence)-1:
            return False
        
        for i in range(index,len(new_sentence)-1):
            if isDelete==False:
                isDelete==True
                self.getMei(index,new_sentence[index:]+new_sentence[:index],isDelete)
            else:
                isDelete==False
                self.getMei(index+1,new_sentence,isDelete)
getMei(index,new_sentence,isDelete)
print(number)


#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)


#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))
