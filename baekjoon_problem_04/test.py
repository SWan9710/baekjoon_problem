class Person:
    def __init__(self):
        self.age = 0
        
    @property 
    def age(self): # getter
        print('getter 호출')
        return self._age

    @age.setter
    def age(self, age): # setter
        print('setter 호출')
        self._age = age

    # 클래스 변수의 퍼블릭 변수
    # 게터와 세터를 만들고 property를 통해 p1.age, print(p1.age)
    # 형식으로 접근이 가능해진다
    # age = property(get_age, set_age)

p1 = Person()
p1.age = 25
print(p1.age)
# p1.set_age(25) # 프로텍트 개념을 이해하고 세터를 이용해서 age 값을 변경
# print(p1.get_age()) # 게터를 이용해서 age값 읽어오기