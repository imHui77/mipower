#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib.request
import re
from bs4 import BeautifulSoup
import sys
import smtplib
from email.mime.text import MIMEText  
from email.header import Header  

class mi_buy():
	def getHTML(self,url):
		opener = urllib.request.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		cto = opener.open(url).read().decode('utf8')
		HTML = cto.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
		self.parserHTML(HTML)

	def parserHTML(self,HTML):
		check = HTML.find("3154300003")
		if check == True:
			print("開放購買")
			self.sendMail()
		else:
			print("暫時缺貨")

	def sendMail(self):
		receiver = [	# 收件者信箱
					'******@gmail.com', 
					'******@gmail.com'
					]
		gmail_sender = '******@gmail.com'		# 寄信者帳號
		gmail_passwd = '*********'				# 寄信者密碼

		subject = '小米行動電源 10000 開放購買囉'	# 標題
		TEXT = "【商品名稱】：小米行動電源 10000\n"					# 內文
		TEXT += "【購買網址】：http://www.mi.com/tw/pb10000/"		# 內文
		  
		msg = MIMEText(TEXT,'plain','utf-8')
		msg['Subject'] = Header(subject, 'utf-8')  
		  
		server = smtplib.SMTP('smtp.gmail.com', 587)
		# server = smtplib.SMTP('smtp-mail.outlook.com', 587)
		server.ehlo()
		server.starttls()
		server.login(gmail_sender, gmail_passwd)
		try:
			server.sendmail(gmail_sender, receiver, msg.as_string())
			print ('email sent')
			pass
		except:
			print ('error sending mail')
		server.quit()  


if __name__ == '__main__':
	url = "http://buy.mi.com/tw/accessories/70-0-0-1"
	mi = mi_buy()
	mi.getHTML(url)