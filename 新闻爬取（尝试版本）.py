#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import requests
from lxml import etree


# In[9]:


url = r'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&'
print(type(url))
   # 定义搜索内容
kw = '郑州暴雨 澎湃新闻'
param = {'wd': kw}
head = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'}
response = requests.get(url=url, params=param, headers=head)
r = response.text

html = etree.HTML(r, etree.HTMLParser())
#print(r)
print('*****************')
r1 = html.xpath('//h3')
r2 = html.xpath('//*[@class="c-abstract"]')
r3 = html.xpath('//*[@class="t"]/a/@href')
for i in range(50):
   #print(r1) 
   try:
       r11 = r1[i].xpath('string(.)')
       r22 = r2[i].xpath('string(.)')
       r33 = r3[i]
   except:
       print("ERROR/n")
   else:   
       #对于单个网页的文本提取
       head1={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'}
       url1 = json.dumps(r33,ensure_ascii=False)
       url1= url1[1:-1]
       #print(url1)
       response2 = requests.get(url=url1,headers = head1)
       rt = response2.text
       html1 = etree.HTML(rt, etree.HTMLParser())
       rt1 = html1.xpath('//h1')
       print(rt1)
       #h = content.xpath('//h1')
       try:
           h1 = rt1[0].xpath('string(.)').strip()
       except:
           print("存在异常/n")

       else:
           d = html1.xpath("//div[@class='news_txt']")
           d1 = d[0].xpath('string(.)').strip()
       #print(d1)

           with open('text.txt','a',encoding='utf-8')as d:
               d.write(json.dumps(d1,ensure_ascii=False) + '\n')

       with open('result.txt', 'a', encoding='utf-8') as c:
           c.write(json.dumps(r11,ensure_ascii=False) + '\n')
           c.write(json.dumps(r22,ensure_ascii=False) + '\n')
           c.write(json.dumps(r33,ensure_ascii=False) + '\n')
       print(r11, end='\n')
       print('------------------------')
       print(r22, end='\n')
       print(r33)


# In[ ]:





# In[ ]:




