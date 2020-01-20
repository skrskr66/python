class Person(object):
    # 限定对象只能绑定_name,_age,_gender
    # __slots__ 魔法只能对当前类有效，对子类并没有效果
    __slots__ = ('_name','_age','_gender')

    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age
    @property
    def name(self):
        return self._name

    @age.setter
    def age(self,age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s玩飞行棋' % self._name)
        else:
            print('%s玩斗地主' % self._name)

def main():
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'
    # person.name = 'fds'
    # person.play()

if __name__ == '__main__':
    main()