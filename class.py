import unittest
class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sum(self):
        add = self.a + self.b
        print(add)
# class B(A):
#     def subt(self):

ac = A(2,3)
# ac.a = 2
# ac.b = 3
ac.sum()
ab = B(3,2)
ab.subt(2,3)
