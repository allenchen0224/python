#定義函式
#函式內部的程式碼 若是沒有做函式呼叫 就不會執行
# def multiply(n1,n2):
#     print(n1*n2)
#     return n1*n2

# val = multiply(3,4)+multiply(10,5)
# print(val)
# multiply(10,8)

#程式的包裝
def calculate(x1,x2):
    sum = 0
    for n in range(x1,x2+1):
        sum+=n
    print(sum)

calculate(1,20)
calculate(-5,10)
