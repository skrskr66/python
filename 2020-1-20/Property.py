class Person(object):

    def __init__(self,name,age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self,age):
        self._age = age
    # @age.setter   如果不加name的修改器，那么名字则无法修改
    # def name(self,name):
    #     self._name = name

    def play(self):
        if self._age <= 16:
            print('%s玩飞行棋' % self._name)
        else:
            print('%s玩斗地主' % self._name)

def main():
    person = Person('刘宇程',22)
    person.play()
    person.age = 21
    person.play()
    # person.name = 'nihaoa'
    # person.play()

if __name__ == '__main__':
    main()