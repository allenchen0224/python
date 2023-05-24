#break 的簡單範例
# n = 0
# while n<5:
#     if n ==3:
#         break
#     print(n)  #印出迴圈中的n
#     n+=1
# print('最後的n',n)  #印出迴圈結束後的n

#continue 的簡單範例
# n = 0
# for x in [0,1,2,3]:
#     if x%2==0:   #x是偶數
#         continue
#     print(x)
#     n+=1
# print('最後的n',n)

#else 的簡單範例
# sum = 0

# for n in range(11):
#     sum+=n
# else:
#     print(sum) #印出 0+1+2+...+10的結果

#綜合範例: 找出整數平方根
#輸入9 得到3
# x = eval(input('請輸入數字:'))
# for i in range(x):
#     if i*i==x:
#         print('整數平方根:',i)
#         break #用break強制結束迴圈不執行else
# else:
#     print('沒有整數平方根')


n = eval(input())
i = 0
while i<n:
    if i**2==n:
        print('整數平方根:',i)
        break
    i+=1
else:
    print('沒有整數平方根')
