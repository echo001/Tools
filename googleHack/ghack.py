#!/usr/bin/env python3
#site:*/admin-login intitle:"Admin Login"
import requests
import urllib3
import time
import re
import os
from lxml import etree
from io import BytesIO
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)	#防InsecureRequestWarning
## CONTENT VARIABLES ##
version = 1.1
## MAIN FUNCTION ##

def parse_args():
    import argparse
    parse = argparse.ArgumentParser()
    parse.add_argument('-d', '--domain', type=str, required=True, help='Target domain.')
    parse.add_argument('-o', '--output', type=str, help='Output file')
    return parse.parse_args()

def banner():
    global version
    b = '''
      ______ _    ___ __ __        _________    __
    /  ____|  |   |  |  \  \      /  ____|  |  /  /
   /  /    |  |___|  |___\  \    /  /    |  | /  /
  |  | ____|  |___|  |___ \  \  |  |     |  |/  /
  |  | |_  |  |   |  |     \  \ |  |     |  |\  \\
   \  \__| |  |   |  |      \  \ \  \____|  | \  \\
    \______|__|   |__|       \__\ \______|__|  \__\\

    Version {v} - There is Google Hack!
    Made by Echo001
    '''.format(v=version)
    print(b)

def clear_url(target):
    return re.sub('.*www\.','',target,1).split('/')[0].strip()

def url_requests(url, headers=None):
    s = requests.session()
    s.keep_alive = False
    response = requests.get(url, headers=headers, verify=False)	#代理问题，必须加verify=False，编辑器里跑不需要
    content = response.content
    parser = etree.HTMLParser()
    content = etree.parse(BytesIO(content), parser=parser)
    return content

def google_scrape(url, query): #利用google hack语句爬取google搜索结果
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'referer':'https://www.google.com/'
    }
    query = query.replace(' ', '+')
    query = query.replace(':', '%3A')
    query = query.replace('/', '%2F')
    gl_url = f"https://google.com/search?q={query}" #google请求
    response = url_requests(gl_url, headers)
    result = result2 = []
    for cite in response.findall('//cite'): #匹配网站
        data = cite.text
        if re.findall(url, data):
            result += data.split()
    result = {}.fromkeys(result).keys() #去除列表中重复
    for href in response.xpath('//a/@href'):    #匹配具体网址
        if re.findall(url, href):
            if re.findall('^http', href):
                if re.findall('^((?!google).)*$', href):    #匹配非google搜索字符串
                    result2 += str(href).split()    #类型转换，转为list类型
    return result,result2

def site_words_scrape(url): #读取google hack字典
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path,'data','google_hack_words.txt')
    txt_reader = open(path,encoding='gbk')
    total_result = []
    website_result = []
    i = 1
    for query in txt_reader:
        query = query.replace('*',url)
        print(i, query)
        if i>= 1:
            result,result2 = google_scrape(url, query)
            time.sleep(5)  #防google bot detection
            total_result += result
            website_result += result2
            for line in result:
                print(line)
        i += 1
    return total_result,website_result

def save_file(result,output_file):
	with open(output_file,'a') as f:
		f.write(result + '\n')
		f.close()

if __name__ == '__main__':
    banner()
    args = parse_args()

    url = clear_url(args.domain)
    output = args.output
	
    total_result,website_result = site_words_scrape(url)
    website_result.sort()
    total_result = {}.fromkeys(total_result).keys() #去除列表中重复
    website_result = {}.fromkeys(website_result).keys()
    print('\n\n[!]------------TARGET:{d}-------------[!]\n'.format(d=url))
    print('[!]-----------The Subdomain Result-------------[!]\n')
    for line in total_result:
        print(line)
        if output is not None:
            save_file(line,output)
    print('\n\n[!]-----------The Website Result-------------[!]\n')
    for line in website_result:
        print(line)
        if output is not None:
            save_file(line,output)
