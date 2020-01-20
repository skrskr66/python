from time import time
from threading import Thread

import requests

class DownloadHandler(Thread):

    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/project1' + filename, 'wb') as f:
            f.write(resp.content)

def main():
    resp = requests.get('http://api.tianapi.com/dongman/?key=d9eb037bca54f651d630b5b6b7038b6a&num=10')
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        DownloadHandler(url).start()
if __name__ == '__main__':
    main()