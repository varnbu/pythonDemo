# 面向过程的写法

user1 = {
    'name': 'tom',
    'hp': 100
}
user2 = {
    'name': 'jerry',
    'hp': 120
}


def print_role_info(role):
    print('name is %s , hp is %s' % (role['name'], role['hp']))


print_role_info(user1)
print_role_info(user1)


# 面向对象的写法
class Player:
    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp

    def print_role(self):
        print('%s:%s' % (self.__name, self.__hp))


# user1 = Player('tim', 1000)
# user2 = Player('jack', 800)
# user1.print_role()
# user2.print_role()


class Monster:
    '定义怪物类'

    def __init__(self, hp=10):
        self.hp = hp

    def run(self):
        print('移动到某个位置')

    def who_am_i(self):
        print('我是怪物父类')


class Animals(Monster):
    '普通怪物'

    def __init__(self, hp=100):
        super().__init__(hp)

    def who_am_i(self):
        print('我是怪物类')


class BossAnimals(Monster):
    '大boss'
    pass


a1 = Animals(300)
print(a1.hp)
a1.run()
a1.who_am_i()
print(type(a1))
print(isinstance(a1, Animals))
