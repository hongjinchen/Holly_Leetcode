import unittest  # 导入unittest模块，用于编写测试用例
from selenium import webdriver  # 导入Selenium的webdriver模块
from selenium.webdriver.common.keys import Keys  # 导入Keys类，用于模拟键盘按键操作
import HtmlTestRunner  # 导入HtmlTestRunner模块，用于生成HTML格式的测试报告

class GoogleSearchTest(unittest.TestCase):  # 定义一个测试类，继承自unittest.TestCase
    def setUp(self):  # setUp方法会在每个测试方法执行前运行，用于设置测试环境
        # 设置WebDriver，这里需要替换为ChromeDriver的实际路径
        self.driver = webdriver.Chrome(executable_path='[ChromeDriver 路径]')

    def test_search_in_google(self):  # 定义一个测试方法，用于测试在Google上的搜索功能
        driver = self.driver
        driver.get("http://www.google.com")  # 使用WebDriver打开Google首页

        # 确保页面标题包含 "Google"
        self.assertIn("Google", driver.title)  # 使用assertIn断言检查标题中是否包含"Google"

        # 找到搜索框，并在其中输入查询
        elem = driver.find_element_by_name("q")  # 通过元素的name属性查找搜索框
        elem.send_keys("Python")  # 在搜索框中输入"Python"
        elem.send_keys(Keys.RETURN)  # 模拟按下回车键，提交搜索

        # 检查搜索结果页面是否包含搜索结果
        assert "No results found." not in driver.page_source  # 使用assert语句检查页面源代码中是否没有"No results found."

    def tearDown(self):  # tearDown方法会在每个测试方法执行后运行，用于清理测试环境
        self.driver.close()  # 关闭WebDriver

if __name__ == "__main__":  # 判断是否是直接运行这个脚本，如果是，则执行以下代码
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))  # 运行测试，使用HtmlTestRunner生成HTML格式的测试报告，并指定输出目录