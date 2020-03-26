#繼承
"""
class Member:  #父類別
    def __init__(self,new_gender,new_major,new_id):
        self.__gender = new_gender
        self.major = new_major
        self.id = new_id

    def set_gender(self,new_gender):
        if new_gender == 'M' or new_gender == 'F':
            self.__gender = new_gender
        else:
            print('=====請傳入"M"或"F"=====')

    def get_gender(self):
        return  self.__gender

    def borrow_resource(self):
        print('someone borrow')


class Student(Member): #子類別
    def __init__(self,new_gender,new_major,new_id):
        super().__init__(new_gender,new_major,new_id) #繼承

    def join_class(self): #兩個方法(join_class, quit_class)
        pass
    def quit_class(self):
        pass
    def borrow_resource(self): #覆寫
        print('student borrow')


class Professor(Member): #子類別
    def __init__(self,new_gender,new_major,new_id):
        super().__init__(new_gender,new_major,new_id)

    def borrow_resource(self):
        print('professor borrow')  #覆寫

studentA = Student('M','工管系','B10721156')
studentB = Student('B','經濟系','B10241833')
professorA = Professor('M','資工系','B75557214')
professorB = Professor('F','數媒系','B36547895')

ls = [studentA,studentB,professorA,professorB]

for item in ls:
    item.borrow_resource()
"""

#練習
class Pokemon:
    def __init__(self, new_name, new_weight, new_height,new_food,new_cp):
        self.__name = new_name  #建構子初始化
        self.__weight = new_weight
        self.__height = new_height
        self.__food = new_food
        self.__cp = new_cp

    def eat(self):
        print('The pokemon is eating{self.food}')

    def make_noice(self):
        print('The pokemon wow wow wow!')

    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        self.__name = new_name

    def get_weight(self):
        return self.__weight
    def set_weight(self, new_weight):
        self.__weight = new_weight

    def get_height(self):
        return self.__height
    def set_height(self, new_height):
        self.__height = new_height

    def get_food(self):
        return self.__food
    def set_food(self, new_food):
        self.__food = new_food

    def get_cp(self):
        return self.__cp

    def set_cp(self, new_cp):
        self.__cp = new_cp


class Pikachu(Pokemon):
    def __init__(self, new_name, new_weight, new_height, new_food, new_cp):
        super().__init__(new_name, new_weight, new_height, new_food, new_cp)

    def eat(self):
        print(f'{self.get_name()} is eating {self.get_food()}.pika')
        '''若打成f'{self.__name()} is eating {self.__food()}則會錯誤
        ，因name和food為private，所以要用get方法才能取得'''

    def make_noice(self):
        print(f'{self.get_name()} pika pika chu!')


class Squirtle(Pokemon):
    def __init__(self, new_name, new_weight, new_height, new_food, new_cp):
        super().__init__(new_name, new_weight, new_height, new_food, new_cp)

    def eat(self):
        print(f'{self.get_name()}is eating {self.get_food()}.jenny jenny')

    def make_noice(self):
        print(f'{self.get_name()} jenny jenny!')


pokemon = Pokemon('pokemonnn', 60, 120, 'banana', 50)
pikachu = Pikachu('pikachuuu', 55,64, 'apple', 90)
squirtle = Squirtle('squirtleee', 42, 46, 'guava', 80)
ls = [pokemon, pikachu, squirtle]
for item in ls:
    item.make_noice()
