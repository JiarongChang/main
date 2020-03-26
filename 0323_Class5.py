class Student: #類別(class的範圍只到第16行(方法之後就不屬於class)，因此在類別裡的私有屬性或方法超過第16行即不能使用)
    def __init__(self,new_gender,new_major,new_id): #三個屬性(gender,major,id) self為必打格式
        self.__gender = new_gender  #__gender(前面加上兩個底線代表變數為私有變數)
        self.major = new_major
        self.id = new_id

    def join_class(self): #兩個方法(join_class, quit_class)
        pass
    def quit_class(self):
        pass

    def set_gender(self,new_gender):  #gender限制方法
        if new_gender == 'M' or new_gender == 'F':
            self.__gender = new_gender
        else:
            print('=====請傳入"M"或"F"=====')

    def get_gender(self):
        return  self.__gender  #回傳private屬性

studentA = Student('M','工管系','B10721156')
print(studentA.get_gender())  #print出studentA的gender
#print(studentA.__gender)  #因為__gender為私有(private)變數 因此有特別方法得到gender(加上第18 19行)
print(studentA.major)
studentA.__gender = 'F'  #更改gender屬性
print(studentA.get_gender())
studentA.set_gender('dog')#不合邏輯，所以在第7行加入限制  (方法要改成set_gender，而不是studentA.gender)
print(studentA.get_gender())

