class Student(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print('%s正在学习%s。' % (self.name,course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能看熊出没哦' % self.name)
        else:
            print('%s只能看美国大片' % self.name)


# 使用上述类


# def main():
#     stu1 = Student('刘宇程',22)
#
#     stu1.study('python100天')
#
#     stu1.watch_movie()
#
# if __name__ == '__main__':
#     main()

# 在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的
# 如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头

# class Test:
#
#     def __init__(self, foo):
#         self.foo = foo
#
#     def __bar(self):
#         print(self.foo)
#         print('__bar')
#
#
# def main():
#     test = Test('hello')
#     # AttributeError: 'Test' object has no attribute '__bar'
#     test.bar()
#     # AttributeError: 'Test' object has no attribute '__foo'
#     print(test.foo)
#
#
# if __name__ == "__main__":
#     main()

class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    # 让属性名以单下划线开头来表示属性是受保护的，本类之外的代码在访问这样的属性时应该要保持慎重
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()