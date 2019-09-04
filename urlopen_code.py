
import urllib.request
def load_data():
	url = 'http://www.baidu.com'
	#get的请求
	#http的请求
	response = urllib.request.urlopen(url)
	print(response)
	#读取内容 byte类型
	data = response.read()
	print(data)
	#将文件获取的内容转换到字符串
	str_data = data.decode("utf-8")
	print(str_data)
	#将数据写入文件
	with open("baidu.html",'w',encoding='utf-8') as f:
		f.write(str_data)
	#将字符串类型转换到bytes类型
	str_name = 'baidu'
	bytes_name = str_name.encode('utf-8')
	print(bytes_name)
	#python爬取的类型：str bytes
	#如果爬取回来的是bytes类型：但是写入的时候哦需要字符串 deconde("utf-8")
	#如果爬取回来的是strl类型：但是写入是需要bytes类型 encode("utf-8")

load_data()
