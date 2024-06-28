import requests

# 定义请求的 URL 和头部信息
url = "https://test-ltacpop-api.starcharge.com/csms/webapi/login/password/update?locale=en"

headers = {
    "sec-ch-ua": "^\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "tzName": "Asia/Shanghai",
    "locale": "en",
    "sec-ch-ua-mobile": "?0",
    "Authorization": "a8fe8a91-28b6-4c54-ab5f-c395afdcefc6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://test-ltacpop-csms-web.starcharge.com/",
    "tzOffset": "480",
    "sec-ch-ua-platform": "^\"Windows\""
}


# 定义请求的数据模板，其中密码字段将被替换为从 TXT 文件读取的密码
data_template = {
    "account": "+86-17823157411",  # 固定的账户号码
    "newPassword": "",  # 这里将被替换为从文件读取的密码
    "code": "25210" 
}

# 读取密码列表
def read_passwords_from_file(file_path):
    with open(file_path, 'r') as file:
        passwords = file.readlines()
    passwords = [password.strip() for password in passwords]  # 去除每行密码末尾的换行符
    passwords = [password for password in passwords if len(password.strip()) >= 12]
    return passwords

# 执行批量测试
def batch_test(passwords):
    for password in passwords:
        # 替换数据模板中的密码字段
        data = data_template.copy()
        data['newPassword'] = password

        # 发送 POST 请求
        response = requests.post(url, headers=headers, json=data)

        # 打印每个请求的响应状态码和响应内容
        print(f"Testing password: {password}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}\n")

# 主函数
def main():
    passwords_file = '10-million-password-list-top-10000.txt'
    passwords = read_passwords_from_file(passwords_file)
    batch_test(passwords)

if __name__ == "__main__":
    main()