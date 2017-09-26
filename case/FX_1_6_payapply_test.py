import unittest
import requests
import os, sys, time
from common import urlbase,take_sign
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db import test_data


class emp_login(unittest.TestCase):
    ''' 企业/个人发起提现申请 '''



    def setUp(self):
        self.emp = urlbase.list()[2]

        self.base_url = self.emp+"/pay/apply"
        #self.base_url = 'http://192.168.31.160:8008/DTBTradeSystemAPI/api/pay/getWithdrawLimit'

        self.s = requests.Session()
        self.nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


    def test_login_success(self):
        ''' 完备的参数'''

        params = {"user_id":"11111","card_no":"62222222222222","card_open":"中国农业银行苏州支行",	"card_name":"张三","trade_amount":"100.00","withdrawPwd":"123456",'sourceFrom':'1'}
        #sourceFrom 平台标识 1为延保
        sign = take_sign.sign_data(dict_data=params)
        params['sign']=sign
        print(params)
        r = self.s.post(self.base_url,data=params)
        #self.result = r.json()
        self.result = r.status_code

        #self.assertEqual(self.result['code'],0)
        self.assertEqual(self.result,200)


    def tearDown(self):
        '''结束初始化环境'''
        print(self.result)




if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()