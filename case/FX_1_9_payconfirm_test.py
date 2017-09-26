import unittest
import requests
import os, sys, time
from common import urlbase,take_sign
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db import test_data


class emp_login(unittest.TestCase):
    ''' 企业/个人用户查看提现申请详情 '''



    def setUp(self):
        self.emp = urlbase.list()[2]

        self.base_url = self.emp+"/pay/confirm"
        #self.base_url = 'http://120.237.128.121:814/DTBTradeSystem/api/pay/queryDetail'

        self.s = requests.Session()
        self.nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


    def test_login_success(self):
        ''' 完备的参数'''

        data = {"apply_no":"PAY2017071612121111","review_status":"1",}
        #sourceFrom 平台标识 1为延保
        sign = take_sign.sign_data(dict_data=data)

        params = '?apply_no=PAY2017071612121111&review_status=1&sign='+sign
        print(params)
        r = self.s.get(self.base_url+params)
        self.result = r.json()

        #self.assertEqual(self.result['code'],0)


    def tearDown(self):
        '''结束初始化环境'''
        print(self.result)




if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()