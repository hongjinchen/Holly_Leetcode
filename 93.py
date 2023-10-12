# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
# 分段问题其实就是在n-1个空隙里面，如何合理的插入3个"."，使得获得的ip合法。
# 那么总可能性就只有n-1选3种可能，再排除掉前导0和数值大于255的情况，就可以返回了。
        self.res = []
        self.dfs(s,0,"")
        return self.res
    

    def dfs(self, s, count, ip_address):
        if count==3 and s!="":
            if int(s)<=255 and (len(s)==1 or s[0]!='0'):
                 self.res.append(ip_address+s)
            return
        
        if s=="":
            return
        
        for i in range(1, 4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.dfs(s[i:], count + 1, ip_address + s[:i] + '.')
                
                if s[0] == '0': 
                    break  # 避免前导0


if __name__ == "__main__":
    solution = Solution()
    s = "101023"
    print(solution.restoreIpAddresses(s))
