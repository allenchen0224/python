import email.message
msg =  email.message.EmailMessage()
msg['From'] = '寄件人'
msg['To'] = '收件人'
msg['Subject'] = '您好'
#寄送文件內容
msg.set_content('測試')
#寄送比較多樣的內容(html)
# msg.add_alternative('<h3>優惠券</h3>滿五百送一百喔',subtype='html')
#連線到SMTP Server驗證寄件人身份並發送
import smtplib
#到網路上搜尋 gmail smtp server
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login('帳號','密碼')
server.send_message(msg)
server.close()