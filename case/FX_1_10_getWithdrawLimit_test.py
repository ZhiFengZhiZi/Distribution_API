import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db import test_data


class emp_login(unittest.TestCase):
    ''' 接口方法，文件以test结尾.. '''



    def setUp(self):
        '''脚本前置内容'''
        self.emp = urlbase.list()[2]

        self.base_url = self.emp+'/pay/getWithdrawLimit'

        self.s = requests.Session()


    def test_login_success(self):
        ''' 验证码接口'''

        ##以x-www-form-urlencoded
        r = self.s.get(self.base_url)
        self.result = r.json()

        self.assertEqual(self.result['code'],0)


    def tearDown(self):
        '''结束初始化环境'''
        print(self.result)




if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()