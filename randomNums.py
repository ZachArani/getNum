import collections
d = collections.deque(maxlen=750)
for i in range (1000):
	if(len(d)==750):
		d.pop()
	num = get_num()
	if not num in d:
		d.append(num)

def get_num():
	return int(urllib.request.urlopen("http://localhost:8080").read())