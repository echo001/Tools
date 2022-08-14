#!/usr/bin/env python3
import requests
import re
from lxml import etree
from io import BytesIO
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
## CONTENT VARIABLES ##
version = 1.1
## MAIN FUNCTION ##
def parse_args():
    import argparse
    parse = argparse.ArgumentParser()
    parse.add_argument('-d', '--domain', type=str, required=True, help='Target domain.')
    parse.add_argument('-o', '--output', type=str, help='Output file.')
    return parse.parse_args()

def banner():
    global version
    b = '''
     ______________________   ____     __        _________    __
    /  _____|___    ___|  |   |  |    /  \      /  ____|  |  /  /
   /  /         |  |   |  |___|  |   / /\ \    /  /    |  | /  /
  |  |          |  |   |  |___|  |  / /__\ \  |  |     |  |/  /
  |  |          |  |   |  |   |  | / /----\ \ |  |     |  |\  \\
   \  \_____    |  |   |  |   |  |/ /      \ \ \  \____|  | \  \\
    \_______|   |__|   |__|   |__|_/        \_\ \______|__|  \__\\
    Version {v} - There is Certificate Transparency Hack!
    Made by Echo001
    '''.format(v=version)
    print(b)

def clear_url(target):
    return re.sub('.*www\.','',target,1).split('/')[0].strip()

def url_requests(url, headers=None):
    s = requests.session()
    s.keep_alive = False
    response = requests.get(url, headers=headers)
    return response

def response_lxml_parse(url, headers=None):
    response = url_requests(url, headers)
    content = response.content
    parser = etree.HTMLParser()
    content = etree.parse(BytesIO(content), parser=parser)
    return content

def status_code_judge(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    try:
        response = url_requests(url, headers=headers)
        print(response.status_code, url)
        return response.status_code
    except:
        print('404 ' + url)


def crt_scrape(query):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    crt_url = f"https://crt.sh/?q={query}"
    response = response_lxml_parse(crt_url, headers=headers)
    result = []
    for td in response.xpath('//td[5]/text()'):
        if re.findall(query, td):
            result += td.split()
    result = {}.fromkeys(result).keys()
    return result

def exist_judge(query):
    subdomains = crt_scrape(query)
    result = []
    for subdomain in subdomains:
        http_url = f"http://{subdomain}"
        http_status_code = status_code_judge(http_url)
        if http_status_code == 200:
            result += http_url.split()
    for subdomain in subdomains:
        https_url = f"https://{subdomain}"
        https_status_code = status_code_judge(https_url)
        if https_status_code == 200:
            result += https_url.split()
    return result

def save_file(result,output_file):
	with open(output_file,'a') as f:
		f.write(result + '\n')
		f.close()

if __name__ == '__main__':
    banner()
    args = parse_args()

    url = clear_url(args.domain)
    output = args.output
    result = exist_judge(url)
    sorted(result)
    print('\n\n[!]------------TARGET:{d}-------------[!]\n'.format(d=url))
    print('[!]-----------The Subdomain Result-------------[!]\n')
    for line in result:
        print(line)
        if output is not None:
            save_file(line,output)
