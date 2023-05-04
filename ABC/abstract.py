from abc import ABC, abstractmethod

class Test(ABC):

    def __init__(self, action):
        self.action = action

    @abstractmethod
    def create(self):
       return 'OK'

a = Test(1)
print(a.create())

class Test1(Test):
    pass

b = Test1(1)
print(id(b))
print(b.create())