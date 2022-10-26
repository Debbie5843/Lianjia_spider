import requests
import parsel
from bs4 import BeautifulSoup
import time
import re

#租房房源
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'}

def crawl(url):
    # url = 'https://gz.lianjia.com/ershoufang/cencun/pg1/'
    response = requests.get(url=url, headers=headers)

    if not response:
        reply = False

    selector = parsel.Selector(response.text)
    lis = selector.css('.content__list div')
    i = 0
    for li in lis:
        try:
            title = li.css('.content__list--item--title a::text').get().strip()  # 题目
            area_list = li.css('.content__list--item--des a::text').getall()
            qu = area_list[0]  # 区
            bankuai = area_list[1]  # 板块
            louming = area_list[2]  # 楼名
            ex1 = '<i>/</i>.*?\n(.*?)<i>/</i>'
            src_list1 = re.findall(ex1, response.text, re.S)
            area = src_list1[0].split() # 面积
            #price = li.css('#content > div.content__article > div.content__list > div:nth-child(13) > div > span > em::text').get() # 价格

            detail_href = 'https://sz.lianjia.com' + li.css('.content__list--item--title a::attr(href)').get()
            detail_resp = requests.get(url=detail_href, headers=headers).text
            #print(detail_resp)


            ex2 = '<li class="fl oneline">(.*?)</li>'
            src_list2 = re.findall(ex2, detail_resp, re.S)
            level = src_list2[7]
            elev = src_list2[8]
            water = src_list2[11]
            electri = src_list2[13]

            ex3 = '<div class="content__aside--title">.*?<span>(.*?)</span>元/月'
            src_list3 = re.findall(ex3, detail_resp, re.S)
            price = src_list3[0]

            '''
            #house_info = li.css('.houseInfo::text').get().split('|')
            roomType = house_info[0]  # 房屋户型
            ararea = house_info[1]  # 建筑面积
            orient = house_info[2]  # 房屋朝向
            furnish = house_info[3]  # 装修情况
            floor = house_info[4]  # 所在楼层
            constructYear = house_info[5]  # 所在楼层
            # buildtype = house_info[6]  # 建筑类型

            #detail_href = li.css('.title a::attr(href)').get()
            # print(detail_href)
            #detail_resp = requests.get(url=detail_href, headers=headers).text
            # print(detail_resp.text)

            ex1 = '<li><span class="label">.*?</span>(.*?)</li>'
            src_list1 = re.findall(ex1, detail_resp, re.S)
            # roomType = src_list1[0]  # 房屋户型
            # floor = src_list1[1]  # 所在楼层
            # ararea = src_list1[2]  # 建筑面积
            structure = src_list1[3]  # 户型结构
            inarea = src_list1[4]  # 套内面积
            buildtype = src_list1[5]  # 建筑类型
            # orient = src_list1[6]  # 房屋朝向
            arcstruc = src_list1[7]  # 建筑结构
            # furnish = src_list1[8]  # 装修情况
            stair = src_list1[9]  # 梯户比
            elevator = src_list1[10]  # 有无电梯

            # 爬交易属性
            ex2 = '<li class="">\n                              <span class="label ">.*?</span>\n                              <span>(.*?)</span>\n                                                          </li>'
            src_list2 = re.findall(ex2, detail_resp, re.S)
            guapaiTime = src_list2[0]  # 挂牌时间
            propType = src_list2[1]  # 交易权属
            lastTime = src_list2[2]  # 上次交易
            buildFor = src_list2[3]  # 房屋用途
            buildYear = src_list2[4]  # 房屋年限
            propOwn = src_list2[5]  # 产权所属
            exDiya = '<li>\n                              <span class="label">抵押信息</span>\n                              <span style="display:inline-block;width:64%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;vertical-align:middle;" title=".*?">\n                                (.*?)\n                              </span>\n                            </li>'
            Diya = re.findall(exDiya, detail_resp, re.S)[0]  # 抵押信息'''

            print(detail_href, '*', title, '*', qu, '*', bankuai, '*', louming, '*', area, '*', level, '*', elev, '*', water, '*', electri, '*', price)
            # print(roomtype)
            #time.sleep(1)
        except IndexError:
            pass
    reply = True

if __name__ == "__main__":


    i = 2
    for i in range(2, 3):
        url = 'https://sz.lianjia.com/zufang/luohuqu/pg' + str(i) + 'erp4500/#contentList'
        crawl(url)
        print(i)
    '''for area in baoan_list:
        for i in range(1, 95):
            url = 'https://sz.lianjia.com/ershoufang/' + area
            '/pg' + str(i) + '/'
            reply = crawl(url)
            if reply == False:
                break
            print(i)'''

