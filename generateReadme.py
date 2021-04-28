# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re

blogUrl = 'https://blog.csdn.net/zwf193071'

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'} 

def addIntro(f):
	txt = ''' 
### Hi there, I'm Lucy Zhu 👋

Now I'm working at SF Express Ltd as a web frontend engineer.

9年前端开发程序猿，传说中的背锅大师 🐶，一直致力于研究并探索各种机制的底层原理

现定居于武汉，专注于前端，热衷于学习Go、web assembly、Nodejs等知识点，预期发展方向为全栈工程师

**Languages and Tools:**  

<code><img height="20" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png"></code>
<code><img height="20" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/typescript/typescript.png"></code>
<code><img height="20" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/vue/vue.png"></code>
<code><img height="20" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/nodejs/nodejs.png"></code>

[![zwf193071's github stats](https://github-readme-stats.vercel.app/api?username=zwf193071)](https://github.com/anuraghazra/github-readme-stats)


''' 
	f.write(txt)

def addProjectInfo(f):
	txt ='''
### 开源项目  
- [simple-pack](https://github.com/zwf193071/simple-pack) 简易的JS打包工具	
- [zash-cli](https://github.com/zwf193071/zash-cli) 自动化生成页面的cli工具
- [gallery-by-react](https://github.com/zwf193071/gallery-by-react) React左右切换画廊  
- [js-everywhere-learn](https://github.com/zwf193071/js-everywhere-learn) JS-Everywhere学习案例  
- [webassembly-study](https://github.com/zwf193071/webassembly-study) webassembly学习案例
   
[查看更多](https://github.com/zwf193071?tab=repositories)	 

	''' 
	f.write(txt) 


def addBlogInfo(f):  
	http = urllib3.PoolManager(num_pools=5, headers = headers)
	resp = http.request('GET', blogUrl)
	resp_tree = etree.HTML(resp.data.decode("utf-8"))
	html_data = resp_tree.xpath(".//div[@class='article-item-box csdn-tracking-statistics']/h4") 
	f.write("\n### 我的博客\n")
	cnt = 0
	for i in html_data: 
		if cnt >= 5:
			break
		title = i.xpath('./a/text()')[1].strip()
		url = i.xpath('./a/@href')[0] 
		item = '- [%s](%s)\n' % (title, url)
		f.write(item)
		cnt = cnt + 1
	f.write('\n[查看更多](https://blog.csdn.net/zwf193071)\n')


if __name__=='__main__':
	f = open('README.md', 'w+')
	addIntro(f)
	f.write('<table><tr>\n')
	f.write('<td valign="top" width="50%">\n')
	addProjectInfo(f)
	f.write('\n</td>\n')
	f.write('<td valign="top" width="50%">\n')
	addBlogInfo(f)
	f.write('\n</td>\n')
	f.write('</tr></table>\n')
	f.close 

