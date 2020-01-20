from math import sqrt

class Triangle(object):

    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c

    # 返回函数的静态方法。
    # class C(object):
    #     @staticmethod
    #     def f(arg1, arg2, ...):
    #         ...
    # 以上实例声明了静态方法 f，从而可以实现实例化使用 C().f()，当然也可以不实例化调用该方法 C.f()。
    @staticmethod
    def is_valid(a,b,c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *(half - self._b) * (half - self._c))

def main():
    a,b,c = eval(input('请输入三角形边长：'))
    # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
    # print(type(a),b,c)
    # a,b,c = 3,4,5
    if Triangle.is_valid(a,b,c):
        t = Triangle(a,b,c)
        print(t.perimeter())
        print(t.area())
    else:
        print('不能构成三角形')

if __name__ == '__main__':
    main()