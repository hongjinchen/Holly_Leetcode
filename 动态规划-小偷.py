n=4
numbers=['1', '2', '3', '4']

new_numbers=[]
for i in range(len(numbers)):
    new_numbers.append(int(numbers[i]))

numbers=new_numbers

if len(numbers)<=2:
    print(max(numbers))
else:
    # dp
    def get_max(numbers):
        dp = [0] * len(numbers)
        dp[0] = numbers[0]
        dp[1] = max(numbers[0], numbers[1])

        for i in range(2, len(numbers)):
            n_2 = numbers[i] + dp[i - 2]
            n_1 = numbers[i - 1]
            dp[i] = max(n_2, n_1)
        return max(dp)
    
    numbers = new_numbers
    numbers_without1=numbers[1:]
    numbers_withoutn=numbers[:-1]
    numbers_without1_result=get_max(numbers_without1)
    numbers_withoutn_result=get_max(numbers_withoutn)

    print(max(numbers_without1_result,numbers_withoutn_result))