# coding = utf-8

import os, time, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class youtube(object):
	"""docstring for taobao"""
	def __init__(self):
		super(youtube, self).__init__()
		self.driverPath = 'D:\\pythonDemo\\driver\\chromedriver_win32\\chromedriver.exe'
		self.domain = 'https://accounts.google.com'
		self.browser = webdriver.Chrome(self.driverPath)
		# self.browser.maximize_window()
		self.browser.implicitly_wait(5)
		self.userName = 'ren_jinbo@163.com'
		self.userPassword = 'renjinbo_123'
		self.actionChain = ActionChains(self.browser)
		self.yCode = ""

	def open_youtube(self):
		self.browser.get('https://accounts.google.com/o/oauth2/v2/auth?client_id=775513731180-rc0mrf2dno2bumtf7f6chfs3uh44ur0a.apps.googleusercontent.com&scope=https://www.googleapis.com/auth/youtube&email&response_type=code&redirect_uri=http://localhost')
		self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(self.userName)
		#点击email用户下一步
		element = self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
		self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(self.userPassword)
		#点击密码用户下一步
		element = self.browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
		#选择channel
		element = self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div').click()
		# 点击信任账户 允许
		element = self.browser.find_element_by_class_name('VfPpkd-RLmnJb').click()
		element = self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]').click()
		time.sleep(2)
		print(self.browser.current_url)
		current_url = self.browser.current_url
		if current_url.startswith('http://localhost'):
			self.yCode = current_url.split("code=")[1].split('&')[0].replace('#','')
			print(self.yCode)
	
		self.browser.quit()
		# exit()

	def request_token(self):
		self.yCode = "4/0AY0e-g6iXLfL0fKhGpOePKjBpmUMMhrQU5dIyFCkILXpCrNLRjJRxFUNQDMsqQZ9m_Csvg"
		if self.yCode == "":
			print("code is empty")
			return

		import requests

		headers = {
		    'Host': 'www.googleapis.com',
		    'Accept-Language': 'zh-CN,en,*',
		    'User-Agent': 'Mozilla/5.0',
		}

		params = (
		    ('client_id', '775513731180-rc0mrf2dno2bumtf7f6chfs3uh44ur0a.apps.googleusercontent.com'),
		    ('client_secret', '2-EoB0ZlZbwrbkLR_VoW3hB0'),
		    ('code', self.yCode),
		    ('grant_type', 'authorization_code'),
		    # ('redirect_uri', 'http://127.0.0.1:64777/oauth2/callback/google'),
		    ('redirect_uri', 'http://localhost'),
		)
		print(params)
		response = requests.post('https://www.googleapis.com/oauth2/v4/token', headers=headers, params=params)
		print(response.status_code)
		print(response.text)
		if response.status_code == 200:
			json1 = eval(response.text)
			print(type(json1))
			print(json1)
		else:
			print("error with request token")
		sys.stdout.write('jimbo is good')
		
if __name__ == '__main__':
	
	yb = youtube()
	# yb.open_youtube()
	yb.request_token()
	exit()


	
