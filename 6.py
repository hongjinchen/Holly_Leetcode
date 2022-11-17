def question(x):
    bit = 0
    b = x
    bits = []
    if x < 0:
        return False
    # get bits of number a
    while True:
        if x / 10 != 0:
            bit += 1
            x = int(x / 10)
        else:
            break

    # 得到每一位的数字
    bb = bit
    for r in range(bit):
        bb -= 1
        f = b // 10**bb
        bits.append(f)
        b = b % 10**bb

    for i, value in enumerate(bits):
        if bits[i] != bits[len(bits) - 1 - i]:
            return False
    return True


print(question(11))
