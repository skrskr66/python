# def main():
#     f = None
#     try:
#         f = open('D:\书籍\\test.txt','r',encoding='utf-8')
#         print(f.read())
#     except FileExistsError:
#         print('Not Found File')
#     except LookupError:
#         print('Not Konw encoding')
#     except UnicodeDecodeError:
#         print('Read file encoding error')
#     finally:
#         if f:
#             f.close()
#
# if __name__ == '__main__':
#     main()

import json


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()