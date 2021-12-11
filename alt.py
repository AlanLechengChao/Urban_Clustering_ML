# _*_ coding: utf-8 _*_
# _author: 'sql'
# date: 2021/1/17

import re
import requests
import parsel
from fontTools.ttLib import TTFont
import time
import random
import json
import os
import pandas as pd
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 不是所有的类别都有字体反扒，例如：美容 没有
# 每页15个，实际店铺要少，缺少广告推广店铺
# 会封ip,账号，放慢采集速度


class Spider:
    def __init__(self):
        self.dir = '采集结果'
        self.t = '采集数据'
        self.datas = []
        self.s = set()
        self.n = 1
        self.nt = 1
        self.url = "http://www.dianping.com/shenzhen/ch10"  #目标URL

        # 字体映射列表
        self.wordlist = '1234567890店中美家馆小车大市公酒行国品发电金心业商司超生装园场食有新限天面工服海华水房饰城乐汽香部利子老艺花专东肉菜学福饭人百餐茶务通味所山区门药银农龙停尚安广鑫一容动南具源兴鲜记时机烤文康信果阳理锅宝达地儿衣特产西批坊州牛佳化五米修爱北养卖建材三会鸡室红站德王光名丽油院堂烧江社合星货型村自科快便日民营和活童明器烟育宾精屋经居庄石顺林尔县手厅销用好客火雅盛体旅之鞋辣作粉包楼校鱼平彩上吧保永万物教吃设医正造丰健点汤网庆技斯洗料配汇木缘加麻联卫川泰色世方寓风幼羊烫来高厂兰阿贝皮全女拉成云维贸道术运都口博河瑞宏京际路祥青镇厨培力惠连马鸿钢训影甲助窗布富牌头四多妆吉苑沙恒隆春干饼氏里二管诚制售嘉长轩杂副清计黄讯太鸭号街交与叉附近层旁对巷栋环省桥湖段乡厦府铺内侧元购前幢滨处向座下澩凤港开关景泉塘放昌线湾政步宁解白田町溪十八古双胜本单同九迎第台玉锦底后七斜期武岭松角纪朝峰六振珠局岗洲横边济井办汉代临弄团外塔杨铁浦字年岛陵原梅进荣友虹央桂沿事津凯莲丁秀柳集紫旗张谷的是不了很还个也这我就在以可到错没去过感次要比觉看得说常真们但最喜哈么别位能较境非为欢然他挺着价那意种想出员两推做排实分间甜度起满给热完格荐喝等其再几只现朋候样直而买于般豆量选奶打每评少算又因情找些份置适什蛋师气你姐棒试总定啊足级整带虾如态且尝主话强当更板知己无酸让入啦式笑赞片酱差像提队走嫩才刚午接重串回晚微周值费性桌拍跟块调糕'
        self.utf8List_shopnum = []
        self.utf8List_tagname = []
        self.utf8List_shopdesc = []
        self.utf8List_num = []
        self.utf8List_hours = []
        self.utf8List_reviewtag = []
        self.utf8List_address = []
        self.utf8List_dishname = []

        # 获取cookies
        self.cookie = self.get_cookies()

        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            #'Cookie': '_lxsdk_cuid=17cd97ed798c8-09cd12e43c8c57-57b193e-144000-17cd97ed798c8; _lxsdk=17cd97ed798c8-09cd12e43c8c57-57b193e-144000-17cd97ed798c8; _hc.v=04fc18f9-728c-e2f3-2889-5133a0ff2d43.1635736542; s_ViewType=10; switchcityflashtoast=1; cityid=1; _tr.u=WkgoW5Y3VQxOnLzg; info="{\"query_id\":\"eefc2f6f-576f-475c-923d-d59595d93741\",\"ab_id\":\"exp000095_a\"}"; default_ab=citylist%3AA%3A1%7Cshop%3AA%3A11%7Cindex%3AA%3A3%7CshopList%3AA%3A5; cy=1; cye=shanghai; ctu=ab0b17f53bfb400f278c7292e5a760ea1b2e755cdec6d7c16d34b6681d2c347f; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; dplet=d14d8625b9a1e9b148af1617a7b828e8; dper=08a3c7574643fa6b4204cdcec52f6c789359f666a8f0d90dfc3cafcc5323f09eb8ade77c56b48b2819f7b548edb19840aede0d1a5125a5f65eb60429435fa50b358d43d8ba4503dc9b3050ae62ff669d8c0f39a146c31743a47132004367d5c0; ua=dpuser_8193103949; fspop=test; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1636104702,1636467455,1636478212,1636506762; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1636511758; _lxsdk_s=17d07b29b92-e66-0d3-6f0%7C%7C21'
            'Cookie': self.cookie,
            'Host': 'www.dianping.com',
            # 'Referer': 'http://www.dianping.com/beijing/ch10/r2578',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        }

    def get_cookies(self):
        """
        从配置文件读取  cookies
        :return:
        """
        with open('cookie.txt', 'r', encoding='utf-8')as f:
            cookie = f.read().strip()
            return cookie

    def get_res(self, url):
        i = 1
        while i < 3:
            try:
                time.sleep(random.uniform(3, 5))
                response = requests.request("GET", url, headers=self.headers, timeout=(5, 10), verify=False)
                # print(response.content.decode('utf-8'))
                # 抱歉！页面无法访问
                if re.findall('页面不存在', response.content.decode('utf-8'), re.S):
                    print(url)
                    input('请滑动验证')
                    i += 1
                    continue
                elif response.status_code == 404:
                # elif re.findall('抱歉！页面无法访问', response.content.decode('utf-8'), re.S):
                    input('ip被封', url)  #  详情页访问10次左右，被封，停顿无效
                    time.sleep(random.uniform(5, 10))
                    i += 1
                    continue
                    # sys.exit()
                    # break
                elif response.status_code == 200:
                    return response
                else:
                    print('重新请求')
                    time.sleep(random.uniform(5, 10))
                    i += 1
                    continue
            except:
                print('出错了')
                i += 1
                time.sleep(random.uniform(5, 10))
                continue

    def get_ttf(self, res):
        """
        获得字体文件,保存成对应的ttf字体文件，生成对应的列表
        :return:
        """
        # html = self.get_res(url).text
        html = re.sub('\s', '', res.text)  # 去掉任意空白字符
        TTF = re.findall('<linkrel="stylesheet"type="text/css"href="(.*?)">', html, re.S)[1]  # css  url
        url = 'http:'+TTF
        print(url)
        res = requests.get(url).text                                #请求css
        res = re.sub('\s', '', res)  # 去掉任意空白字符
        TTF_dict={}                     #字体字典
        fontlist=re.findall('@font-face{(.*?)}', res, re.S)                #缩小范围
        for font in fontlist:
            TTF_name=re.findall('font-family:"PingFangSC-Regular-(.*?)"',font,re.S)[0] #TTF的类别
            TTF_link=re.findall(',url\("(.*?)"\);',font,re.S)[0]
            TTF_dict.update({TTF_name:TTF_link})
        for key, value in TTF_dict.items():
            b = requests.get('http:' + value).content
            with open('大众点评{}.ttf'.format(key), 'wb')as f:
                f.write(b)
            font1 = TTFont('大众点评{}.ttf'.format(key))  # 读取字体文件，生成对应列表
            uni_list1 = font1.getGlyphOrder()[2:]  # 获取所有编码，去除前2个
            if key == 'shopNum':
                self.utf8List_shopnum = ['&#x' + uni[3:] for uni in uni_list1]
            elif key == 'tagName':
                self.utf8List_tagname = ['&#x' + uni[3:] for uni in uni_list1]
            elif key == 'shopdesc':
                self.utf8List_shopdesc = ['&#x' + uni[3:] for uni in uni_list1]
            elif key == 'num':
                self.utf8List_num = ['&#x' + uni[3:] for uni in uni_list1]
            elif key == 'hours':
                self.utf8List_hours = ['&#x' + uni[3:] for uni in uni_list1]
            elif key == 'reviewTag':
                self.utf8List_reviewtag = ['&#x' + uni[3:] for uni in uni_list1]
            elif key == 'address':
                self.utf8List_address = ['&#x' + uni[3:] for uni in uni_list1]
            elif key == 'dishname':
                self.utf8List_dishname = ['&#x' + uni[3:] for uni in uni_list1]
            else:
                continue
        print('')

    def replace_text(self, utf8List_, str_):
        # 匹配出所有加密字符
        for i in range(len(utf8List_)):
            if utf8List_[i] in str_:
                str_ = str_.replace(utf8List_[i], self.wordlist[i])
        return str_

    def replace_num(self, utf8List_, str_):
        # 匹配出所有加密数字
        for i in range(10):
            str_ = str_.replace(utf8List_[i], self.wordlist[i])  # 数字字体映射
        return str_

    def del_char(self, str_):
        # 删掉多余字符
        str_ = re.sub('<eclass="address">|;</e>|<dclass="num">|;</d>|<cclass="dishname">|;</c>|<svgmtsiclass="tagName">|;</svgmtsi>', '',
                      str_)
        return str_

    def get_score(self, keys, html):
        # 评分 --口味，环境，服务
        taste = ''
        for key in keys:
            s = 'spanclass="item">{}:(.*?)</span>'.format(key)
            if re.findall(s, html, re.S):
                taste = re.findall(s, html, re.S)[0]  # 口味评分
        if taste:
            taste = self.replace_num(self.utf8List_num, taste)
            taste = self.del_char(taste)
        return taste

    def save_csv(self):
        # 保存为csv文件
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        n = self.t + current_time + '.csv'
        path = os.path.join(self.dir, n)
        df = pd.DataFrame(self.datas)
        df.to_csv(path, index=False, encoding='utf-8-sig')

    def parse(self, res):
        """
        解析列表页
        :param html:
        :return:
        """
        html = re.sub('\s', '', res.text)  # 去掉任意空白字符
        shop_info = re.findall('<liclass="">(.*?)<\/li>', html, re.S)  # 缩小范围，店铺信息

        for i in range(len(shop_info)):
            shop_name = ''
            if re.findall('data-name="(.*?)"', shop_info[i], re.S):
                shop_name = re.findall('data-name="(.*?)"', shop_info[i], re.S)[0]  # 店铺名称


            shopid = re.findall('data-shopid="(.*?)"', shop_info[i], re.S)[0]  # 店铺id
            url_detail = 'http://www.dianping.com/shop/{}'.format(shopid)
            print(url_detail)

            #  店铺去重
            if shopid in self.s:
                print('店铺：{}已经存在{}'.format(shop_name, url_detail))
                continue

            self.s.add(shopid)

            shop_address = ''
            if re.findall('class="tag">(.*?)</span>', shop_info[i], re.S):
                shop_address_ = re.findall('class="tag">(.*?)</span>', shop_info[i], re.S)  # 店铺地址

                shop_address = shop_address_[1]  # 店铺地址
                shop_address = self.replace_text(self.utf8List_tagname, shop_address)
                shop_address = self.del_char(shop_address)

            if re.findall('人均<b>(.*?)<\/b', shop_info[i], re.S):
                per_capita = re.findall('人均<b>(.*?)<\/b', shop_info[i], re.S)[0]  # 人均价格
            else:
                per_capita = '-'

            # 替换数字
            for i in range(10):
                per_capita = per_capita.replace(self.utf8List_shopnum[i], self.wordlist[i])  # 字体映射

            # 将对应的数字匹配出来

            per_capitas = ''
            if per_capita and per_capita!= '-':
                per_capitas = (''.join(re.findall('\d', per_capita, re.S)))  # 人均消费

            item = {}
            item.update(self.dic)
            item['店名'] = str(shop_name)
            item['店铺id'] = shopid
            item['人均'] = str(per_capitas)
            item['地址'] = str(shop_address)
            item['网址'] = url_detail

            print(item)
            self.n += 1
            self.datas.append(item)

    def get_pages(self, url):
        """
        翻页
        最多返回50页
        :param url:
        :return:
        """
        print('正在下载url:  {}'.format(url))
        res = self.get_res(url)
        if res:
            if re.findall('没有找到符合条件的商户', res.text, re.S):
                print('没有找到符合条件的商户')
                return
            else:
                # 获得对应字体文件，只获得一次即可
                if self.nt == 1:
                    self.get_ttf(res)
                    self.nt += 1

                self.parse(res)  # 解析第一页

                d = parsel.Selector(text=res.text)
                if d.xpath('.//a[contains(text(),"下一页")]/@href'):   # 解析下一页
                    next_page = d.xpath('.//a[contains(text(),"下一页")]/@href').extract_first()
                    self.get_pages(next_page)

    def get_types(self, res):
        """
        获取分类
        :param res:
        :return:
        """
        types = {}
        d = parsel.Selector(text=res.text)
        lis = d.xpath('.//div[@class="nav-category J_filter_channel"]//div[@class="nc-items"]/a')
        for li in lis[18:19]:
            name = li.xpath('.//span/text()').extract_first()
            href = li.xpath('.//@href').extract_first()
            id = re.findall(r'ch\d+', href)[0]
            types[name] = (id, href)
        print(types)
        return types

    def get_areas(self, res):
        """
        获取地点
        :param res:
        :return:
        """
        areas = {}
        d = parsel.Selector(text=res.text)
        #lis = d.xpath('.//div[@id="J_nt_items"]/div[@id="bussi-nav"]/a')  # 热门商区
        lis = d.xpath('.//div[@id="J_nt_items"]/div[@id="region-nav"]/a')  # 行政区
        # lis = d.xpath('.//div[@id="J_nt_items"]/div[@id="metro-nav"]/a')  # 地铁线
        for li in lis[4:-1]:
            name = li.xpath('.//span/text()').extract_first()
            href = li.xpath('.//@href').extract_first()
            print(re.findall(r'r\d+', href))
            id = re.findall(r'r\d+', href)[0]
            areas[name] = (id, href)
        print(areas)
        return areas

    def r(self, url=''):
        """
        遍历热门商圈
        最多返回50页
        :return:
        """
        print('正在下载url:  {}'.format(url))
        pro_code = 'shanghai'
        pro_name = '上海市'
        res = self.get_res(url)
        if res:
            base_url = 'http://www.dianping.com/{}/{}/{}'
            types = self.get_types(res)
            areas = self.get_areas(res)
            for type_name, type in types.items():

                for area_name, area in areas.items():
                    dic = {
                        '省份': pro_name,
                        '城市': pro_name,
                        '地区': area_name,
                        '分类': type_name,
                    }
                    self.dic = dic
                    url = base_url.format(pro_code, type[0], area[0])
                    print('正在下载url:  {}'.format(url))
                    self.get_pages(url)


    def run(self):
        url = "https://www.dianping.com/shanghai/ch0"  # 目标URL
        self.r(url)

        # 保存数据
        self.save_csv()

if __name__ == '__main__':
    start = time.time()
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start))  # 转化格式

    s = Spider()
    s.run()

    finish = time.time()
    finish_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(finish))  # 转化格式
    Total_time = finish - start
    m, s = divmod(Total_time, 60)
    h, m = divmod(m, 60)
    print('开始时间:', start_time)
    print('结束时间:', finish_time)
    print("Total_time", "共耗时===>%d时:%02d分:%02d秒" % (h, m, s))


