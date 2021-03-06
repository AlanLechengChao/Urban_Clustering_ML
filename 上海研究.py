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
location_list = ['yangjing', 'yangsiqiantan']

for l in location_list:
    print(f'\n=========??????{l}???????????????==========')
    for p in range(1, 4):
        for page in range(1, 101):

            # 1.?????????????????????url????????????(??????????????????)????????????/????????????
            print(f'\n=========???????????????{page}????????????==========')
            url = f'https://sh.lianjia.com/chengjiao/{l}/pg{page}lc{p}'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

            # 2.????????????url????????????(html/css/js)
            result = requests.get(url=url, headers=headers)
            html_data = result.text

            # 3.????????????(???????????????????????????) css?????????????????????(??????????????????html??????)
            selector = parsel.Selector(html_data)
            lissy = selector.css('.info')
            if not lissy:  # ??????????????????100?????????????????????????????????
                print(lissy)
                print('???????????????????????????')
                break

            for i in lissy:
                title = i.css('.title a::text').get()  # ???????????? (??????????????????????????????)
                title_new = title.split()
                if len(title_new) == 3:
                    location = title_new[0]  # ?????????/??????
                    rooms = title_new[1]  # ????????????
                    areas = title_new[2]  # ??????
                else:
                    print(title_new)
                    break

                address = i.css('.address')  # ????????????????????????????????????
                house_info = address.css('.houseInfo::text').get()  # ???????????? (???|??????)
                deal_date = address.css('.dealDate::text').get()  # ????????????
                if type(address.css('.totalPrice span::text').get()) == str:
                    total_price = address.css('.totalPrice span::text').get() + ',0000'  # ??????
                else:
                    total_price = '?????????'

                flood = i.css('.flood')
                position_info = flood.css('.positionInfo::text').get()  # ???????????????????????????
                position_info_new = position_info.split()
                if len(position_info_new) == 2:
                    height = position_info_new[0]  # ??????
                    years = position_info_new[1]  # ??????
                else:
                    print(position_info_new)
                    height = None
                    years = position_info_new
                unit_price = flood.css('.unitPrice span::text').get()  # ????????????

                deal_house_info = i.css('.dealHouseInfo')
                special_info = deal_house_info.css('.dealHouseTxt span::text').get()  # ??????????????????????????????

                deal_cyclee_info = i.css('.dealCycleeInfo')  # ???????????????????????????
                deal_cyclee_text = deal_cyclee_info.css('.dealCycleTxt span::text').getall()  # ???????????????????????????
                if len(deal_cyclee_text) == 2:
                    selling_price = deal_cyclee_text[0]  # ????????????
                    cycle = deal_cyclee_text[1]  # ????????????
                else:
                    print(deal_cyclee_text)
                    selling_price = None
                    cycle = deal_cyclee_text


            #4.????????????
                with open('?????????????????????4.csv', mode='a', encoding='ANSI', newline='') as f:  # encoding??????utf-8
                    csv_write = csv.writer(f)
                    csv_write.writerow([location, rooms, areas, house_info, deal_date, total_price,
                                        height, years, unit_price, special_info, selling_price, cycle, l])
