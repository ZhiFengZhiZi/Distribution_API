import unittest
import requests
import os, sys, time
from common import urlbase,take_sign
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db import test_data


class emp_login(unittest.TestCase):
    ''' 提现密码设置接口 '''



    def setUp(self):
        self.emp = urlbase.list()[2]

        self.base_url = self.emp+"/pay/setWithdrawPwd"
        #self.base_url = 'http://120.237.128.121:814/DTBTradeSystem/api/pay/queryDetail'

        self.s = requests.Session()
        self.nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


    def test_login_success(self):
        ''' 完备的参数'''
        sdata = {"userId": "1235","oldpwd":"123455","newpwd":"654321",'sourceFrom':'1'}
        #data = ["userId","1235","bankLogo","图片base64转码字符串，用MEDIUMTEXT字段存储","cardNo","63282347923401234","cardBank","建设银行","持卡人姓名","张三"]
        #sourceFrom 平台标识 1为延保
        list = []
        datalist = []
        for i in sdata.keys():
            list.append(i)

        for i in list:
            a = sdata[i]

            data = i + '=' + a
            datalist.append(data)

        datastr = '&'.join(datalist)

        sign = take_sign.sign_data(dict_data=sdata)
        params = '?'+datastr+'&sign='+sign
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