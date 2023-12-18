# 输入1999.11.29。输出一九九九年十一月二十九日。输入为变量
def digit_to_chinese(digit):
    """Converts a digit to its Chinese representation."""
    chinese_digits = "零一二三四五六七八九"
    return chinese_digits[int(digit)]

def number_to_chinese(number):
    """Converts a number to its Chinese representation."""
    return ''.join(digit_to_chinese(digit) for digit in str(number))

def date_to_chinese(date):
    """Converts a date in the format YYYY.MM.DD to Chinese representation."""
    year, month, day = date.split('.')
    year_chinese = number_to_chinese(year)
    month_chinese = number_to_chinese(month)
    day_chinese = number_to_chinese(day)

    # Special handling for months and days less than 10
    if len(month) == 2 and month[0] == '1':
        month_chinese = '十' + month_chinese[1:]
    if len(day) == 2:
        if day[0] == '1':
            day_chinese = '十' + day_chinese[1:]
        else:
            day_chinese = number_to_chinese(day[0]) + '十' + day_chinese[1:]

    # Remove leading '一' for days and months
    month_chinese = month_chinese.lstrip('一')
    day_chinese = day_chinese.lstrip('一')
    
    return f"{year_chinese}年{month_chinese}月{day_chinese}日"

# Convert the given date
print(date_to_chinese("1999.11.29"))