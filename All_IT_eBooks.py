import requests
import sys
from bs4 import BeautifulSoup

print('\nAll IT eBooks - 免費電腦書籍下載')
print('==============================================')
choice = input('下載整站輸入1，指定關鍵字輸入2，退出程式請輸入3:')
print('==============================================')

#建立urls為list，儲存所有主頁面連結(ex:page1~page844)
urls = []

#建立target為list，儲存所有電子書頁面連結(針對每一本書名)
target = []

#建立download_URL為list，儲存所有電子書下載的連結

links = ''


def allPAGE():

	num = int(input('請輸入電子書網站總共頁數:'))

	for i in range(1,num+1):
		main_page = "http://www.allitebooks.org/page/" + str(i)   #抓首頁
		urls.append(main_page)

	for url in urls:
		resp = requests.get(url)
		soup = BeautifulSoup(resp.text, 'lxml')
		a_tags = soup.find_all('h2', class_='entry-title')   #抓出所有電子書頁面連結的html檔案
		
		for tag in a_tags:
			links = tag.find('a')['href']  #從電子書的html檔案抓出主頁面連結
			target.append(links)

	for j in target:
		resp = requests.get(j, headers={'User-agent': 'Mozilla/5.0'})
		soup = BeautifulSoup(resp.text, 'lxml')
		download = soup.find_all(class_='download-links')	   #.pdf或.epbu下載連結
		bookName = soup.find('h1',class_='single-title').text  #書名
		for k in download:
			links = k.find('a')['href']
			#print(bookName)
			print(links)

	print('\n抓取完成')
	print('請將抓取之連結透過下載器進行下載')

def keywords():
	keywords = str(input('請輸入英文關鍵字:'))

	num = int(input('請輸入該關鍵字下總共頁數:'))

	for i in range(1,num+1):
		
		search_page = "http://www.allitebooks.org/page/" + str(i) + "/?s=" + keywords
		urls.append(search_page)


	for url in urls:
		resp = requests.get(url)
		soup = BeautifulSoup(resp.text, 'lxml')
		a_tags = soup.find_all('h2', class_='entry-title')   #抓出所有電子書頁面連結的html檔案
		
		for tag in a_tags:
			links = tag.find('a')['href']  #從電子書的html檔案抓出主頁面連結
			target.append(links)

	for j in target:
		resp = requests.get(j, headers={'User-agent': 'Mozilla/5.0'})
		soup = BeautifulSoup(resp.text, 'lxml')
		download = soup.find_all(class_='download-links')	   #.pdf或.epbu下載連結
		bookName = soup.find('h1',class_='single-title').text  #書名
		for k in download:
			links = k.find('a')['href']
			#print(bookName)
			print(links)
	print('\n抓取完成')
	print('請將抓取之連結透過下載器進行下載')


if choice == '1': #抓取整個網站的電子書
	allPAGE()

if choice == '2':    #抓取指定關鍵字的電子書
	keywords()

if choice == '3':
	sys.exit()

while choice != '1' or '2' or '0':
	print('\n請輸入1或2或3')
	print('==============================================')
	choice = input('下載整站輸入1，指定關鍵字輸入2，退出程式請輸入3:')
	if choice == '1': #抓取整個網站的電子書
		allPAGE()
	if choice == '2':    #抓取指定關鍵字的電子書
		keywords()
	if choice == '3':
		sys.exit()