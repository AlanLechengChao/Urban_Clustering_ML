import requests


# 地理编码函数
def poisearch(types, city, offset, page):
    '''
    :param offset: 每页记录数据，取<25
    :param page: 当前页数：0-99
    :param types: 查询POI类型
    :param city: 城市名
    '''
    url = 'https://restapi.amap.com/v3/place/text'
    keyJacky = '56f59d1919ad56051454c201faeea14c'
    keyElla = '3edcc1ec77a0050c2cad7fb097b2b537'
    parameters = {
        'types': types,
        'key': keyJacky,
        'city': city,
        'citylimit': 'true',
        'offset': offset,
        'extensions': 'all',
        'page': page
    }
    try:
        res = requests.get(url, parameters)
        content = res.json()
        pois = content['pois']
        # for poi in pois:
        #     print(poi)
        #     print(poi['id'])
        #     detail = poi['biz_ext']
        #     if detail:
        #         print(detail['rating'])
        return pois
        # coordinate = content['geocodes'][0]['location']
        # district = content['geocodes'][0]['district']
        # count = content['count']
        # status = content['status']
        # formatted_address = content['geocodes'][0]['formatted_address']
        # return [formatted_address, coordinate, district, count, status]
    except :
        return "", -1


# 处理正常地址
# types = '050100'
# city = '310115'
# offset = 25
# page = 0
# print(poisearch(types, city, offset, page))



# print 结果
# 世纪大道