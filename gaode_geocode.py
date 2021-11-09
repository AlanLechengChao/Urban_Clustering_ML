import requests


# 地理编码函数
def geocode(address, city):
    '''
    :param address:地址串
    :param city: 城市名
    :return: street:四级地址
             label:标签
    '''
    url = 'http://restapi.amap.com/v3/geocode/geo'

    parameters = {
        'address': address,
        'key': '56f59d1919ad56051454c201faeea14c',
        'city': city
    }
    try:
        res = requests.get(url, parameters)
        content = res.json()
        coordinate = content['geocodes'][0]['location']
        district = content['geocodes'][0]['district']
        count = content['count']
        status = content['status']
        formatted_address = content['geocodes'][0]['formatted_address']
        return [formatted_address, coordinate, district, count, status]
    except :
        return "", -1


# 处理正常地址




# print 结果
# 世纪大道