import hashlib

# --encoding:utf-8--



def sign_data(dict_data):
    '''分销sign加密字段生成规则'''
    sit_code = 'abcd1234'
    pre_code = 'abcd1234'

    list = []
    #print(dict.keys())
    for i in dict_data.keys():
        list.append(i)

    list_sort = sorted(list)

    datalist = []
    for i in list_sort:

        a = dict_data[i]

        data = i + '=' + str(a)


        datalist.append(data)

    datastr = '&'.join(datalist)
    #print(datastr)
    F = datastr + '&'+sit_code

    #print(F)

    m = hashlib.md5()
    m.update(F.encode("utf8"))
    mdstr = m.hexdigest()
    #print(mdstr)
    return mdstr


if __name__ =='__main__':
    dict_data = {'user_id': '1111', 'trade_id': '123', 'product_no': 'c151959011', 'trade_time': '2017-07-26 19:00:00',
            'order_no': 'YB12312313', 'product_price': '100.00'}

    a = sign_data(dict_data=dict_data)
    print(a)