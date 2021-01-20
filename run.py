#!/usr/bin/python3 
# -*- coding: utf-8 -*-
#coding: UTF-8
#python3 run.py baidu.com

import requests
import re
import urllib.request
import json
import sys
import re

def get_url(url_after):
        url_before = 'http://icp.chinaz.com/'
        company = ''
        url = url_before+url_after
        r0=requests.get(url)
        findenty = re.compile(r'<a target="_blank" href="//data.chinaz.com/company/t0-p0-c0-i0-d0-s-(.*?)">')
        enty = re.findall(findenty,r0.text)
        #print r0.text
        company = enty[0]
        return company
        
def main(key):
        url = 'http://icp.chinaz.com/Home/PageData'
        data1={'pageNo':'1',
              'pageSize':'10',
              'Kw':urllib.request.unquote(key)
              }
        headers={
                'COOKIE':'Hm_lvt_aecc9715b0f5d5f7f34fba48a3c511d6=1593997639; UM_distinctid=17321a9c0170-09d8b6c563b4e28-4c302372-1fa400-17321a9c018365; qHistory=aHR0cDovL3BpbmcuY2hpbmF6LmNvbV9QaW5n5qOA5rWL; CNZZDATA433095=cnzz_eid%3D4478658-1598446294-%26ntime%3D1598446294; Hm_lvt_ca96c3507ee04e182fb6d097cb2a1a4c=1598449121,1598449587; CNZZDATA5082706=cnzz_eid%3D2071997104-1598447001-%26ntime%3D1598447001; Hm_lpvt_ca96c3507ee04e182fb6d097cb2a1a4c=1598449591',
                'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
                'Accept':'application/json, text/javascript, */*; q=0.01',
                'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding':'gzip, deflate',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With':'XMLHttpRequest',
                'Content-Length':'132',
                'Origin':'http://icp.chinaz.com',
                'Referer':'http://icp.chinaz.com/%E5%8C%97%E4%BA%AC%E7%99%BE%E5%BA%A6%E7%BD%91%E8%AE%AF%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8'
                }
        #proxies = {'http': 'http://127.0.0.1:8080'}
        #r=requests.post(url,data,headers,proxies=proxies)
        #添加代理，测试代码
        r1=requests.post(url,data=data1,headers=headers)
        #print r.text
        result1_dic = json.loads(r1.text)
        print("URL_Numbers:"+str(result1_dic['amount']))
        n = result1_dic['amount']
        #n是查询总量，大于100个实际免费也差不了，最多查前100个
        if n>100:
        	m_times = 11
        else:
                if n%10 == 0:
                        m_times = n//10 + 1
                else:
                        m_times = n//10 + 2
                #print m_times
        for m in range(1,m_times):
                data2={'pageNo':str(m),
                        'pageSize':'10',
                        'Kw':urllib.request.unquote(key)
                        }
                #print m
                #10个查一次，网站限制了每次只能查10-20个
                r2=requests.post(url,data=data2,headers=headers)
                result2_dic = json.loads(r2.text)
                url_dic = result2_dic['data']
                for y in range(len(url_dic)):
                        print (url_dic[y]['host'])
    
if __name__ == '__main__':
        url = sys.argv[1]
        #url = ''
        #输入查询的url
        domain = get_url(url).encode('utf-8')
        print (get_url(url))
        key = urllib.request.quote(domain)
        main(key)


