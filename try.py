#例外處理
while True:
    data = input('請輸入一個數字：')
    try:
        number = int(data)
        break
    except Exception:
        print('error,請重新輸入：')

number = number *2
print(number)