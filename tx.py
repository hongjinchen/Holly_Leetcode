# 字符串的压缩和解压缩
# 允许用户输入
# 基于用户输入判断选择什么操作
# 进行一定的规则检查和容错
# aabbcdd = a2b2c1d2
import sys

def compress_or_decompress_string(input_string):
    if not input_string:
        return input_string

    if any(char.isdigit() for char in input_string):
        # 解压缩
        decompressed = ""
        i = 0
        while i < len(input_string):
            char = input_string[i]
            i += 1
            count = ""
            while i < len(input_string) and input_string[i].isdigit():
                count += input_string[i]
                i += 1
            decompressed += char * int(count)
        return decompressed
    else:
        # 压缩
        compressed = ""
        count = 1
        for i in range(1, len(input_string)):
            if input_string[i] == input_string[i - 1]:
                count += 1
            else:
                compressed += input_string[i - 1] + str(count)
                count = 1
        compressed += input_string[-1] + str(count)
        return compressed

# 示例测试
print(compress_or_decompress_string("aabbcdd"))  # 应输出 a2b2c1d2
print(compress_or_decompress_string("a2b2c1d2")) # 应输出 aabbcdd