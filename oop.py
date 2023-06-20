# #物件導向


# #汽車類別
# class Cars:
#     #建構式
#     def __init__(self,color,seat):
#         self.color = color
#         self.seat = seat
#     #方法
#     def drive(self):
#         print(f"My car is {self.color} and {self.seat}.")
# mazda = Cars('red',4) #mazda是Cars類別的物件
# bmw = Cars('blue',4)
# print(isinstance(mazda,Cars))

# print(mazda.color)
# print(bmw.color)

# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
    
#     # def get_radius(self):
#     #     return self.radius
#     # def set_radius(self,radius):
#     #     self.radius = radius
#     def get_area(self):
#         return math.pi*self.radius*self.radius
#     def get_perimeter(self):
#         return 2*math.pi*self.radius

# c1 = Circle(3)
# # print((c1.get_radius()))
# print((c1.get_area()))
# print((c1.get_perimeter()))

class Student:
    course = 'Pro'
    def __init__(self,age,sex,name):
        self.age = age
        self.sex = sex
        self.name = name
    @classmethod
    def change_course(cls,new_course):
        cls.course = new_course

    def fullname(self):
        return (stu_1.__dict__)
# Student.course = 'python'
stu_1 = Student(26,'man','Benny')
stu_2 = Student(25,'girl','Lily')
stu_1.change_course('Math')

# print(stu_1.fullname())
print(stu_1.course)
print(stu_2.course)