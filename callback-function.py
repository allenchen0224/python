# def test(arg):
#     arg('Hello')

# # test(3)
# # test('hello')

# #定義一個回呼函式
# def handle(da):
#     print(da)

# test(handle)

def add(n1,n2,cb):
    cb(n1+n2)

def handle(result):
    print('結果是',result)

def handle1(result):
    print('Result of Add is',result)

add(3,4,handle)
add(5,6,handle)
add(4,2,handle1)