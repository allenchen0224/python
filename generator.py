# #定義建立生成器的函式
# def test():
#     print('階段一')
#     yield 5
#     print('階段二')
#     yield 10
# #呼叫回傳生成器
# gen = test()

# #搭配for 迴圈使用
# for d in gen:
#     print(d) #5


def even(maxnumber):
    number = 0
    while number <= maxnumber:
        yield number
        number +=2

a = even(10)
for data in a:
    print(data)