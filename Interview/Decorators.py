def notDividedByZero(f1):
    def inner(a,b):
        if b==0:
            print("Please Enter correct value of b")
            return
        return f1(a,b)
    return inner
@notDividedByZero
def division(a,b):
    print(a/b)
def addition(a,b):
    print(a+b)
division(9,0)
division(9,9)
addition(9,0)

# Decorators are the concept in which we can modify function inside function

# def denominatorIsNotZero(f1):
#     def inner(a,b):
#         if b==0:
#             print("please enter valid b value")
#             return
#         return f1(a,b)
#     return inner
#
# @denominatorIsNotZero
# def division(a,b):
#     print(a/b)
# def add(a,b):
#     print(a+b)
# division(2,0)
# division(8,4)
# add(2,0)
