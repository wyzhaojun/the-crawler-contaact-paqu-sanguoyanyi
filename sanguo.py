# -*- coding: utf-8 -*-
import time

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
               }
    # 爬取首页数据
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers).content.decode('utf-8')
    # 首页中解析出标题详情页
    # 实例化bs对象,加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')
    # 解析章节
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./三国演义.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        time.sleep(1)
        # 详情页
        detail_url = 'https://www.shicimingju.com/' + li.a['href']
        detail_page_text = requests.get(url=detail_url, headers=headers).content.decode('utf-8')
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        # 解析到章节内容
        content = div_tag.text
        fp.write(title + ':' + content + '\n')
        print(title, '爬取成功')
    fp.close()
