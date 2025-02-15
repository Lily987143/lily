import requests
import csv
#创建文件对象
f=open('D:\data555.csv',mode='w',encoding='utf-8-sig',newline='')
#字典写入方法
csv_writer=csv.DictWriter(f, fieldnames=['昵称','评论'])
#写入表头
csv_writer.writeheader()

def getcontent(MaxId):
    headers={
        #cookie 用户信息，常用于检测是否有登录信息
        'cookie':'UOR=,,login.sina.com.cn; SCF=AnzjyxBEB2VqDBwg2ITosTyfOhje93Grfh8LDpNiJW9CWGH67HwpocwEW5tn7AYGUNxT-97tqxaWoLWmZkVzMwk.; XSRF-TOKEN=1RcgWkLcIqwuvAHLTgHFDat9; SUB=_2A25KgwZ3DeRhGeFL61sQ9izKyjiIHXVp4Qe_rDV8PUNbmtANLWThkW9NQp_Rtx0rshHWiJ88Ky5o-QAAJ6UDf_9-; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFuIzHhDBcT49C5pC4fN1VW5NHD95QNSK54eKqESo2XWs4Dqcj.i--RiKy2iKn4i--RiKy8iK.0i--4i-8WiK.pi--fiKnfi-zf; ALF=02_1739522855; _s_tentry=weibo.com; Apache=187073079148.39877.1736930870192; SINAGLOBAL=187073079148.39877.1736930870192; ULV=1736930870273:4:1:1:187073079148.39877.1736930870192:1712201316002; WBPSESS=_TbXldRGOGOGg7pJWWBouSl7bbJJCFmwuoJa1C7i59LYOVbpYtd6L3pbEf0H4PUWD9tQQYR18NPnLj6rCOvF159GuRuoEBVDDbMDzVCaZN2RBlciQb10XU1YF2VDc1zXdzhni8wDaSQ7pUJhzgc9kw==',
       #user-agent 用户代理，表示浏览器/设备基本信息
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
        }
    #请求网址
    url='https://weibo.com/ajax/statuses/buildComments'
    data={
          'is_reload':'1',
          'id': '5123083947738770',
          'is_show_bulletin': '2',
          'is_mix': '0',
          'max_id':MaxId,
          'count': '10',
          'uid': '1734510327',
          'fetch_level': '0',
          'locale': 'zh-CN'         
          }
    #发送请求
    response=requests.get(url=url,params=data,headers=headers)
    #获取数据
    #获取响应的json数据
    json_data=response.json()
    #print(json_data)
    #字典取值，取评论信息所在列表
    data_list=json_data['data']
    
    for index in data_list:
      
        dit={
            '昵称':index['user']['screen_name'],
            #'地区':index['source'].replace('来自',''),
            '评论':index['text']
            }
        csv_writer.writerow(dit)
    max_id=json_data['max_id']
    return max_id

max_id=''
for page in range(1,20):
    print(f'正在采集第{page}页的数据')
    max_id=getcontent(MaxId=max_id)