import requests
import parsel
import csv

location_backup = ['beicai', 'biyun', 'caolu', 'chuansha', 'datuanzhen', 'gaodong', 'gaohang', 'geqing', 'hangtou',
                 'huamu', 'huinan', 'jinqiao', 'jinyang', 'kangqiao', 'laogangzhen', 'lianyang', 'lingangxincheng',
                 'lujiazui', 'meiyuan1', 'nanmatou', 'nichengzhen', 'sanlin', 'shibo', 'shuyuanzhen', 'tangqiao',
                 'tangzhen', 'waigaoqiao', 'wanxiangzhen', 'weifang', 'xinchang', 'xuanqiao', 'yangdong', 'yangjing',
                 'yangsiqiantan', 'yuanshen', 'yuqiao1', 'zhangjiang', 'zhoupu', 'zhuqiao',
                 'chunshen', 'gumei', 'hanghua', 'huacao', 'jinganxincheng', 'jinhongqiao', 'jinhui', 'laominhang',
                 'longbai', 'maqiao', 'meilong', 'minpu', 'pujiang1', 'qibao', 'wujing', 'xinzhuang5', 'zhuanqiao',
                 'dachangzhen', 'dahua', 'gaojing', 'gongfu', 'gongkang', 'gucun', 'luodian', 'luojing', 'shangda',
                 'songbao', 'songnan', 'tonghe', 'yanghang', 'yuepu', 'zhangmiao',
                 'caohejing', 'changqiao', 'hengshanlu', 'huadongligong', 'huajing', 'jianguoxilu', 'kangjian',
                 'longhua', 'shanghainanzhan', 'tianlin', 'wantiguan', 'xietulu', 'xuhuibinjiang', 'xujiahui',
                 'zhiwuyuan',
                 'caoyang', 'changfeng1', 'changshoulu', 'changzheng', 'ganquanyichuan', 'guangxin', 'taopu', 'wanli',
                 'wuning', 'zhenguang', 'zhenru', 'zhongyuanliangwancheng',
                 'anshan', 'dongwaitan', 'huangxinggongyuan', 'kongjianglu', 'wujiaochang', 'xinjiangwancheng',
                 'zhongyuan1', 'zhoujiazuilu',
                 'beixinjing', 'gubei', 'hongqiao1', 'tianshan', 'xianxia', 'xijiao', 'xinhualu', 'zhenninglu',
                 'zhongshangongyuan',
                 'chedun', 'jiuting', 'maogang', 'shenminbieshu', 'sheshan', 'shihudang', 'sijing', 'songjiangdaxuecheng',
                 'songjiangxincheng', 'songjianglaocheng', 'xiaokunshan', 'xinbang', 'xinqiao', 'yexie',
                 'anting', 'fengzhuang', 'huating', 'jiadinglaocheng', 'jiadingxincheng', 'jiangqiao', 'juyuanxinqu',
                 'malu', 'nanxiang', 'waigang', 'xinchenglu1', 'xuxing',
                 'dapuqiao', 'dongjiadu', 'huaihaizhonglu', 'huangpubinjiang', 'laoximen', 'nanjingdonglu', 'penglaigongyuan',
                 'renminguangchang', 'shibobinjiang', 'wuliqiao', 'xintiandi', 'yuyuan',
                 'buyecheng', 'caojiadu', 'daning', 'jiangninglu', 'jingansi', 'nanjingxilu', 'pengpu', 'xizangbeilu',
                 'yangcheng', 'yonghe', 'zhabeigongyuan',
                 'beiwaitan', 'jiangwanzhen', 'liangcheng', 'linpinglu', 'luxungongyuan', 'quyang', 'sichuanbeilu',
                 'baihe', 'chonggu', 'huaxin', 'jinze', 'liantang1', 'xianghuaqiao', 'xiayang', 'xujing', 'yingpu',
                 'zhaoxiang', 'zhujiajiao',
                 'fengcheng', 'fengxianjinhui', 'haiwan', 'nanqiao', 'qingcun', 'situan', 'xidu', 'zhelin',
                 'zhuanghang',
                 'jinshan5']
location_list = ['beicai', 'biyun', 'caolu', 'chuansha', 'datuanzhen', 'gaodong', 'gaohang', 'geqing', 'hangtou',
                 'huamu', 'huinan', 'jinqiao', 'jinyang', 'kangqiao', 'laogangzhen', 'lianyang', 'lingangxincheng',
                 'lujiazui', 'meiyuan1', 'nanmatou', 'nichengzhen', 'sanlin', 'shibo', 'shuyuanzhen', 'tangqiao',
                 'tangzhen', 'waigaoqiao', 'wanxiangzhen', 'weifang', 'xinchang', 'xuanqiao', 'yangdong', 'yangjing',
                 'yangsiqiantan', 'yuanshen', 'yuqiao1', 'zhangjiang', 'zhoupu', 'zhuqiao',
                 'chunshen', 'gumei', 'hanghua', 'huacao', 'jinganxincheng', 'jinhongqiao', 'jinhui', 'laominhang',
                 'longbai', 'maqiao', 'meilong', 'minpu', 'pujiang1', 'qibao', 'wujing', 'xinzhuang5', 'zhuanqiao',
                 'dachangzhen', 'dahua', 'gaojing', 'gongfu', 'gongkang', 'gucun', 'luodian', 'luojing', 'shangda',
                 'songbao', 'songnan', 'tonghe', 'yanghang', 'yuepu', 'zhangmiao',
                 'caohejing', 'changqiao', 'hengshanlu', 'huadongligong', 'huajing', 'jianguoxilu', 'kangjian',
                 'longhua', 'shanghainanzhan', 'tianlin', 'wantiguan', 'xietulu', 'xuhuibinjiang', 'xujiahui',
                 'zhiwuyuan',
                 'caoyang', 'changfeng1', 'changshoulu', 'changzheng', 'ganquanyichuan', 'guangxin', 'taopu', 'wanli',
                 'wuning', 'zhenguang', 'zhenru', 'zhongyuanliangwancheng',
                 'anshan', 'dongwaitan', 'huangxinggongyuan', 'kongjianglu', 'wujiaochang', 'xinjiangwancheng',
                 'zhongyuan1', 'zhoujiazuilu',
                 'beixinjing', 'gubei', 'hongqiao1', 'tianshan', 'xianxia', 'xijiao', 'xinhualu', 'zhenninglu',
                 'zhongshangongyuan',
                 'chedun', 'jiuting', 'maogang', 'shenminbieshu', 'sheshan', 'shihudang', 'sijing', 'songjiangdaxuecheng',
                 'songjiangxincheng', 'songjianglaocheng', 'xiaokunshan', 'xinbang', 'xinqiao', 'yexie',
                 'anting', 'fengzhuang', 'huating', 'jiadinglaocheng', 'jiadingxincheng', 'jiangqiao', 'juyuanxinqu',
                 'malu', 'nanxiang', 'waigang', 'xinchenglu1', 'xuxing',
                 'dapuqiao', 'dongjiadu', 'huaihaizhonglu', 'huangpubinjiang', 'laoximen', 'nanjingdonglu', 'penglaigongyuan',
                 'renminguangchang', 'shibobinjiang', 'wuliqiao', 'xintiandi', 'yuyuan',
                 'buyecheng', 'caojiadu', 'daning', 'jiangninglu', 'jingansi', 'nanjingxilu', 'pengpu', 'xizangbeilu',
                 'yangcheng', 'yonghe', 'zhabeigongyuan',
                 'beiwaitan', 'jiangwanzhen', 'liangcheng', 'linpinglu', 'luxungongyuan', 'quyang', 'sichuanbeilu',
                 'baihe', 'chonggu', 'huaxin', 'jinze', 'liantang1', 'xianghuaqiao', 'xiayang', 'xujing', 'yingpu',
                 'zhaoxiang', 'zhujiajiao',
                 'fengcheng', 'fengxianjinhui', 'haiwan', 'nanqiao', 'qingcun', 'situan', 'xidu', 'zhelin',
                 'zhuanghang',
                 'jinshan5']

for l in location_list:
    print(f'\n=========读取{l}地区数据中==========')
    for p in range(1, 4):
        for page in range(1, 101):

            # 1.确定数据所在的url链接地址(分析网页性质)静态网页/动态网页
            print(f'\n=========正在获取第{page}页的数据==========')
            url = f'https://sh.lianjia.com/chengjiao/{l}/pg{page}lc{p}'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

            # 2.发送指定url地址请求(html/css/js)
            result = requests.get(url=url, headers=headers)
            html_data = result.text

            # 3.数据解析(提取我们想要的数据) css选择器提取数据(专门用于提取html数据)
            selector = parsel.Selector(html_data)
            lissy = selector.css('.info')
            if not lissy:  # 如果页数不满100页就已经到底，停止循环
                print(lissy)
                print('本部分数据获取完毕')
                break

            for i in lissy:
                title = i.css('.title a::text').get()  # 房子标题 (地址、几室几厅、面积)
                sub_url = i.css('.title a::attr(href)').get()
                title_new = title.split()
                detail = requests.get(url=sub_url, headers=headers)
                detail_html_data = detail.text
                detail_selector = parsel.Selector(detail_html_data)
                # detail_price = detail_selector.css('span.dealTotalPrice ::text').get()
                detail_deal_info = detail_selector.css('div.msg ::text').getall()  # label::text getall()可以拿到所有的label下的数字，用span::text则是标签名，只用::text则是标签名和数字一起爬出来
                detail_house_attribute = detail_selector.css('.base ::text').getall() # 房屋基本属性
                detail_transaction_atrribute = detail_selector.css('.transaction ::text').getall() # 房屋成交详细信息
                # index_subscribe = detail_transaction_atrribute.index('关注（人）')
                # index_huxing = detail_house_attribute.index('房屋户型')
                # if index_huxing != -1:
                #     huxing = detail_house_attribute[index_huxing+1].strip()
                #     print(huxing)
                # else:
                #     huxing = None
                #     print(huxing)
                # index_jiegou = detail_house_attribute.index('户型结构')
                # if index_jiegou != -1:
                #     jiegou = detail_house_attribute[index_jiegou+1].strip()
                #     print(jiegou)
                # else:
                #     jiegou = None
                #     print(huxing)


                if len(title_new) == 3:
                    location = title_new[0]  # 小区名/地址
                    rooms = title_new[1]  # 几室几厅
                    areas = title_new[2]  # 面积
                else:
                    print(title_new)
                    break

                address = i.css('.address')  # 房屋信息、成交日期、总价
                house_info = address.css('.houseInfo::text').get()  # 房屋信息 (南|精装)
                deal_date = address.css('.dealDate::text').get()  # 成交日期
                if type(address.css('.totalPrice span::text').get()) == str:
                    total_price = address.css('.totalPrice span::text').get() + '0000'  # 总价
                else:
                    total_price = '无信息'

                flood = i.css('.flood')
                position_info = flood.css('.positionInfo::text').get()  # 房屋楼层信息及年代
                position_info_new = position_info.split()
                if len(position_info_new) == 2:
                    height = position_info_new[0]  # 高度
                    years = position_info_new[1]  # 年代
                else:
                    print(position_info_new)
                    height = None
                    years = position_info_new
                unit_price = flood.css('.unitPrice span::text').get()  # 单位价格

                deal_house_info = i.css('.dealHouseInfo')
                special_info = deal_house_info.css('.dealHouseTxt span::text').get()  # 是否近地铁等特殊信息

                deal_cyclee_info = i.css('.dealCycleeInfo')  # 挂牌价格、成交周期
                deal_cyclee_text = deal_cyclee_info.css('.dealCycleTxt span::text').getall()  # 挂牌价格、成交周期
                if len(deal_cyclee_text) == 2:
                    selling_price = deal_cyclee_text[0]  # 挂牌价格
                    cycle = deal_cyclee_text[1]  # 成交周期
                else:
                    print(deal_cyclee_text)
                    selling_price = None
                    cycle = deal_cyclee_text


            #4.数据保存
                with open('链家上海房价详细.csv', mode='a', encoding='ANSI', newline='') as f:  # encoding可用utf-8
                    csv_write = csv.writer(f)
                    csv_write.writerow([location, rooms, areas, house_info, deal_date, total_price,
                                        height, years, unit_price, special_info, selling_price, cycle, l,
                                        detail_house_attribute, detail_deal_info])
