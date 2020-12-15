import requests
import time
from lxml import html
from lxml import etree

etree=html.etree
print(etree)

def get_book():
    # 模拟浏览器向服务器发送请求（get()或者post()）在网页服务器收到请求后返回数据
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4263.3 Safari/537.36"
    }
    data=requests.get('https://www.biquge5200.com/99_99435/',headers=headers).text
    #打印返回的数据<Response [200]>为请求成功 201为跳转 203为重定向 400网页没找到 500服务器宕机
    #print(data)
    #把HTMLA数据转换成PTHOIN可读的数据对你
    html = etree.HTML(data)
    #取出dd标签
    data =  html.xpath('//div[@id="list"]/dl/dd') #跨节点获取数据，跳过前33个标签/[posttion()>33]
    #二次筛选
    for i in data:
        #dd标签下的a标签
        name=i.xpath("./a/text()")[0]
        #a标签下的href属性
        href_url =i.xpath("./a/@href")[0]

        #具体章节信息请求内容数据
        response=requests.get(href_url,headers=headers)
        #解析HTML数据
        res=etree.HTML(response.text)
        content=res.xpath('//div[@id="content"]/p/text()')
        #print(content)
        with open("D:\\1111\\"+name+".txt","w",encoding="utf-8") as f:
            num = 0
            for i  in content:
                f.write(i+"\n")
                num+=1
                if num>20:
                    time.sleep(5)
                    num=0
                print(name)



get_book()


