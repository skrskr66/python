from socket import socket
from json import loads
from base64 import b64decode

def main():
    client = socket()
    client.connect(('10.198.75.60',5566))

    in_data = bytes()

    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)
    # loads()将JSON字符串转成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('/project1' + filename,'wb') as f:
        f.write(b64decode(filedata))
    print('图片已保存.')

if __name__ == '__main__':
    main()