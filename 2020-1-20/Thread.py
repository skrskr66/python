# from random import randint
# from threading import Thread
# from time import time,sleep
#
# def download_task(filename):
#     #print('启动下载%s' % filename )
#     print('开始下载%s..' % filename)
#     time_to_download = randint(5,10)
#     sleep(time_to_download)
#     print('%s下载完成！耗费了%d秒' % (filename,time_to_download))
#
# def main():
#     start = time()
#     p1 = Thread(target=download_task,args=('Python从入门到兴趣.pdf\n',))
#     p1.start()
#     p2 = Thread(target=download_task,args=('Peking Hot.avi\n',))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%.2f秒' % (end - start))
#
# if __name__ == '__main__':
#     main()

# 通过继承Thread类的方式来创建自定义的线程
from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()