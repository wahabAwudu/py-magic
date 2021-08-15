import requests
from .format_msg import message

def sender(name, email=None):
	msg = message(name)
	url = "https://jsonplaceholder.typicode.com/posts"
	resp = requests.post(url, data={"none": msg})
	if resp.status_code in [200, 201]:
		print(resp.json())
	return False
