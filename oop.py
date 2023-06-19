#物件導向


#汽車類別
class Cars:
    #建構式
    def __init__(self,color,seat):
        self.color = color
        self.seat = seat
    #方法
    def drive(self):
        print(f"My car is {self.color} and {self.seat}.")
mazda = Cars('red',4) #mazda是Cars類別的物件
bmw = Cars('blue',4)
print(isinstance(mazda,Cars))

print(mazda.color)
print(bmw.color)