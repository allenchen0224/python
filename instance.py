#Point 實體物件的設計:平面座標上的點
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
p = Point(6,8)
print(p.x,p.y)
p1 = Point(3,4)
print(p1.x,p1.y)
#實體物件的設計:分開紀錄姓、名資料的全名