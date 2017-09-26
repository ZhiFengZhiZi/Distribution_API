

def list():
    """配置项"""
    #url=prelist()
    url = sitlist()

    return url



def sitlist():
    """sit环境list"""
    url=['http://192.168.31.160:8004','http://192.168.31.160:8006','http://192.168.31.160:8008/DTBTradeSystemAPI/api']
    # 第一个是权限系统的端口，第二个是企业保险后台的端口, 第三个是分销api接口
    return url



def prelist():
    """pre环境list"""
    url = ['http://192.168.31.160:8005', 'http://192.168.31.160:8007']
    #第一个是权限系统的端口，第二个是企业保险后台的端口
    return url





def sit():
    url = 'http://192.168.31.160:8004'
    return url

def sit_UaUser():
    url = 'http://192.168.31.160:8006'
    return url

def sit_YbUser():
    url = 'http://eims.sit.datoubao.com/eims'
    return url

def pre():
    url='http://192.168.31.160:8005'
    return url

def pre_UaUser():
    url = 'http://192.168.31.160:8007'
    return url


def pre_admin():
    url = 'http://'
    return url



def prd():

    url='http://114.55.236.197'

    return url


if __name__ == '__main__':
    list()