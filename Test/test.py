import requests

uri = 'http://127.0.0.1:6000/_QUERIES/foo/some_get?\
	   field1=2bceef38-634a-11e8-9a2d-1b370b934e93&field2=2'

def test(url,time):
	for i in range(time):
		r = requests.get(url = uri)
		res = r.text
		if res == 'Error!':
			print('结果错误！')
		else:
			print(res)


test(url_join,10000)

