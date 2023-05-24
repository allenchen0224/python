#判斷式
# if False:
#     print('True 執行')
# else:
#     print('False 執行')

# x = eval(input('請輸入數字:')) #取得使用者輸入的數字

# if x >200:
#     print('x>200')
# elif x>100:
#     print('100<x<200')
# else:
#     print('x<100')

#四則運算
n1 = eval(input('請輸入數字一:'))
n2 = eval(input('請輸入數字二:'))
op = input('請輸入運算:+,-,*,/')

if op == '+':
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op =='*':
    print(n1*n2)
elif op == '/':
    print(n1/n2)
else:
    print('不支援的運算')