#Point 實體物件的設計:平面座標上的點
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# p = Point(6,8)
# print(p.x,p.y)
# p1 = Point(3,4)
# print(p1.x,p1.y)

#實體物件的設計:分開紀錄姓、名資料的全名
# class FullName:
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last

# name1 = FullName('W.H','Chen')
# name2 = FullName('T.Y','Lin')
# print(name1.first,name1.last)
# print(name2.first,name2.last)

# class Point:
#     def __init__ (self,x,y):
#         self.x = x
#         self.y = y
#     #定義實體方法
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetX,targetY):
#         return((self.x-targetX)**2+(self.y-targetY)**2)**0.5
# p = Point(3,4)
# p.show()
# result=p.distance(0,0)
# print(result)

#File 實體物件的設計: 包裝檔案讀取的程式
class File:
    def __init__(self,name):
        self.name = name
        self.file = None #尚未開啟檔案: 初期是None
    def open(self):
        self.file = open(self.name,mode = 'r',encoding='utf8')
    def read(self):
        return self.file.read()
    
#讀取第一個檔案
f1 = File('data1.txt')
f1.open()
data = f1.read()
print(data)
f2 = File('data2.txt')
f2.open()
data = f2.read()
print(data)