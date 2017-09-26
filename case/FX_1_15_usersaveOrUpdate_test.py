import unittest
import requests
import json
import os, sys, time
from common import urlbase,take_sign
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db import test_data


class emp_login(unittest.TestCase):
    ''' 用户数据同步 '''



    def setUp(self):
        self.emp = urlbase.list()[2]

        self.base_url = self.emp+"/user/saveOrUpdate"
        #self.base_url = 'http://120.237.128.121:814/DTBTradeSystem/api/pay/queryDetail'

        self.s = requests.Session()
        self.nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


    def test_login_success(self):
        ''' 完备的参数'''
        sdata = {"user":{"userId": "1","userName": "张三","tel": "15151876543","loginAcc": "15151876543"},
        "company":{"companyId": "2","companyName": "张三家的公司","connectUser": "张三","connectTel": "15151987654","businessLicenseNo": "sadjg1902023984","businessLicense": "http://www.baidu.com/1.jpg","organizationNo": "sadk2384798","organizationCertificate": "http://www.baidu.com/2.jpg","loginAcc": "15151876543"},
        'subChannel':{"channelId": "3","channelName": "渠道名称1",},
        'generalChannel':{"channelId": "4","channelName": "渠道名称2"},
        'sourceFrom':'1'}
        #data = ["userId","1235","bankLogo","图片base64转码字符串，用MEDIUMTEXT字段存储","cardNo","63282347923401234","cardBank","建设银行","持卡人姓名","张三"]
        #sourceFrom 平台标识 1为延保

        sdata["user"] = json.dumps(sdata["user"])
        sdata["company"]=json.dumps(sdata["company"])
        sdata["subChannel"] = json.dumps(sdata["subChannel"])
        sdata["generalChannel"] = json.dumps(sdata["generalChannel"])


        sign = take_sign.sign_data(dict_data=sdata)
        sdata['sign'] = sign
        print(sign)


        r = self.s.post(self.base_url,data=sdata)
        self.result = r.json()

        #self.assertEqual(self.result['code'],0)


    def tearDown(self):
        '''结束初始化环境'''
        print(self.result)




if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()