#!/usr/bin/python

import requests
import json
import os
import commands
import smtplib

cookies = {
	    'G_ENABLED_IDPS': 'google',
	    'JSESSIONID': '2FC3EC6435E5FA49F65EBA43A68CDC37',
	}

def getAuthToken():
	cookies = {
	    'G_ENABLED_IDPS': 'google',
	    'JSESSIONID': '2FC3EC6435E5FA49F65EBA43A68CDC37',
	}

	headers = {
	    'Host': '35.154.251.159',
	    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
	    'Accept': 'application/json, text/plain, */*',
	    'Accept-Language': 'en-US,en;q=0.5',
	    'Referer': 'http://35.154.251.159/',
	    'content-type': 'application/json',
	    'Connection': 'keep-alive',
	}

	data = '{"email": "jatininxs11@gmail.com",  "password": "Jatin@bbc123",  "ip": "180.151.230.10",  "country": "IN",  "state": "Haryana", "city": "Gurgaon",  "time": "2017-12-27T08:02:57.252Z"}'

	response = requests.post('http://35.154.251.159/api/v1/login', headers=headers, cookies=cookies, data=data)
	#print("Response of login api : " + str(response.status_code) )
	if response.status_code == 200:
		dataValues=response.text
		dataDict = json.loads(dataValues)
		AuthToken = dataDict['data']['authToken']
		return AuthToken
	else:
		return None

def onBuildFail(cookies):
	os.chdir("/opt/build_backups/")
	listOfBuilds = filter(os.path.isfile, os.listdir('.'))
	
	lastSuccessfulBuild = sorted(listOfBuilds, key=os.path.getmtime, reverse=True)[0]
	
	buildCopyStatus = commands.getstatusoutput("cp /opt/build_backups/{0} /opt/bbcBuild/{0}.jar".format(lastSuccessfulBuild))
	if buildCopyStatus[0] == 0:
		javaProcessCode = commands.getoutput("pgrep java")
		opNotReqd = commands.getoutput("sudo su bbc -c 'kill -9 {0}' || true".format(javaProcessCode))
		opNotReqd1 = os.system("BUILD_ID='DoNotKill'")
	
		deployStatus = os.system("sudo su bbc -c 'setsid  java -jar /opt/bbcBuild/{0}.jar > /opt/bbcBuild/testfile 2>&1 &'".format(lastSuccessfulBuild))

		if deployStatus == 0:
			AuthToken = getAuthToken()
			# print(AuthToken)
			if responseCheckForWallet(AuthToken,cookies) == 200:
				if responseCheckForUserOrder(AuthToken,cookies) == 200:
					if responseCheckForTransaction(AuthToken,cookies) == 200:
						if responseCheckForTrade(AuthToken,cookies) == 200:
							if responseCheckForCurrency(AuthToken,cookies) == 200:
								if responseCheckForMarket(AuthToken,cookies) == 200:									
									sendMail("rolled back build successfully deployed and tested")	

									delFailedBuild = commands.getstatusoutput("sudo rm /opt/bbcBuild/bbc-0.0.1-SNAPSHOT.jar && sudo rm /opt/build_from_jenkins/bbc-0.0.1-SNAPSHOT.jar")
									copyOldBuild = commands.getstatusoutput("cp /opt/build_backups/{0} /opt/build_from_jenkins/bbc-0.0.1-SNAPSHOT.jar".format(lastSuccessfulBuild))
									
									if delFailedBuild[0] == 0 and copyOldBuild[0] == 0:
										print("Bad build deleted successfully")
									else:
										print("Bad build not deleted or not copied to build_from_jenkins")
								else:
									sendMail("rolled build also failed, please check!")
							else:
								sendMail("rolled build also failed, please check!")
						else:	
							sendMail("rolled build also failed, please check!")			
					else:	
						sendMail("rolled build also failed, please check!")					
				else:	
					sendMail("rolled build also failed, please check!")			
			else:	
				sendMail("rolled build also failed, please check!")			
		else:
			sendMail("rolled build also failed, please check!")
	else:
		sendMail("Build failed and no backup found to deploy, please check!")


def responseCheckForWallet(AuthToken, cookies):
	headersForWallet = {
	    'Pragma': 'no-cache',
	    'Accept-Encoding': 'gzip, deflate',
	    'Accept-Language': 'en-US,en;q=0.8',
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36',
	    'Accept': 'application/json, text/plain, */*',
	    'Referer': 'http://35.154.251.159/',
	    'Authorization': '{}'.format(AuthToken),
	    'Connection': 'keep-alive',
	    'Cache-Control': 'no-cache',
	}
	responseOfWallet = requests.get('http://35.154.251.159/api/v1/user/getUserWalletList', headers=headersForWallet, cookies=cookies)
	return responseOfWallet.status_code
	#print("Response of get user wallet list : " + str(responseOfWallet.status_code))

def responseCheckForUserOrder(AuthToken, cookies):
	headersForUserOrder = {
		    'Pragma': 'no-cache',
		    'Origin': 'http://35.154.251.159',
		    'Accept-Encoding': 'gzip, deflate',
		    'Accept-Language': 'en-US,en;q=0.8',
		    'Authorization': '{}'.format(AuthToken),
		    'content-type': 'application/json',
		    'Accept': 'application/json, text/plain, */*',
		    'Cache-Control': 'no-cache',
		    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36',
		    'Connection': 'keep-alive',
		    'Referer': 'http://35.154.251.159/',
		}

	dataForUserOrder = '{"marketName": "BTC_JPY", "orderStatus": "OPEN", "pageNumber": 1, "pageSize": 7}'
	responseOfUserOrder = requests.post('http://35.154.251.159/api/v1/trade/getUserOrder', headers=headersForUserOrder, cookies=cookies, data=dataForUserOrder)
	return responseOfUserOrder.status_code
	# print("Response of get user order : " + str(responseOfUserOrder.status_code))

def responseCheckForTransaction(AuthToken,cookies):
	headersForTransaction = {
		    'Pragma': 'no-cache',
		    'Origin': 'http://35.154.251.159',
		    'Accept-Encoding': 'gzip, deflate',
		    'Accept-Language': 'en-US,en;q=0.8',
		    'Authorization': '{}'.format(AuthToken),
		    'content-type': 'application/json',
		    'Accept': 'application/json, text/plain, */*',
		    'Cache-Control': 'no-cache',
		    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36',
		    'Connection': 'keep-alive',
		    'Referer': 'http://35.154.251.159/',
		}

	dataForTransaction = '{"walletType": "BTC", "pageSize": 10, "pageNumber": 1}'
	responseOfTransaction = requests.post('http://35.154.251.159/api/v1/user/getTransaction', headers=headersForTransaction, cookies=cookies, data=dataForTransaction)
	return responseOfTransaction.status_code
	# print("Response of get transaction : " + str(responseOfTransaction.status_code))

def responseCheckForTrade(AuthToken,cookies):
	headersForTrade = {
		    'Pragma': 'no-cache',
		    'Origin': 'http://35.154.251.159',
		    'Accept-Encoding': 'gzip, deflate',
		    'Accept-Language': 'en-US,en;q=0.8',
		    'Authorization': '{}'.format(AuthToken),
		    'content-type': 'application/json',
		    'Accept': 'application/json, text/plain, */*',
		    'Cache-Control': 'no-cache',
		    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36',
		    'Connection': 'keep-alive',
		    'Referer': 'http://35.154.251.159/',
		}

	dataForTrade = '{"marketName": "BTC_JPY", "pageNumber": 1, "pageSize": 7}'
	responseOfTrade = requests.post('http://35.154.251.159/api/v1/trade/getAllTrade', headers=headersForTrade, cookies=cookies, data=dataForTrade)
	return responseOfTrade.status_code
	# print("Response of trade : " + str(responseOfTrade.status_code))
	
def responseCheckForCurrency(AuthToken,cookies):
	headersForGetCurrency = {
		    'Pragma': 'no-cache',
		    'Accept-Encoding': 'gzip, deflate',
		    'Accept-Language': 'en-US,en;q=0.8',
		    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36',
		    'Accept': 'application/json, text/plain, */*',
		    'Referer': 'http://35.154.251.159/',
		    'Authorization': '{}'.format(AuthToken),
		    'Connection': 'keep-alive',
		    'Cache-Control': 'no-cache',
		}

	responseOfGetCurrency = requests.get('http://35.154.251.159/api/v1/admin/getAllCurrency', headers=headersForGetCurrency, cookies=cookies)
	return responseOfGetCurrency.status_code
	# print("Response of Currency : " + str(responseOfGetCurrency.status_code))

def responseCheckForMarket(AuthToken,cookies):
	headersForMarket = {
		    'Pragma': 'no-cache',
		    'Accept-Encoding': 'gzip, deflate',
		    'Accept-Language': 'en-US,en;q=0.8',
		    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36',
		    'Accept': 'application/json, text/plain, */*',
		    'Referer': 'http://35.154.251.159/',
		    'Authorization': '{}'.format(AuthToken),
		    'Connection': 'keep-alive',
		    'Cache-Control': 'no-cache',
		}

	responseOfMarket = requests.get('http://35.154.251.159/api/v1/trade/markets', headers=headersForMarket, cookies=cookies)
	return responseOfMarket.status_code
	# print("Response of market : " + str(responseOfMarket.status_code))

# def responseCheckForNewsFeed(cookies):
# 	headersForNewsFeed = {
			
# 	}

def sendMail(message):
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("bbcstage.noreply@gmail.com", "bbc@123456")
	message = message
	s.sendmail("bbcstage.noreply@gmail.com", "jatin.gupta@oodlestechnologies.com", message)
	s.quit()


if __name__ == '__main__':

	AuthToken = getAuthToken()
	if AuthToken is not None:
		if responseCheckForWallet(AuthToken,cookies) == 200:
			# print("wallet passed")
			if responseCheckForUserOrder(AuthToken,cookies) == 200:
				# print("order passed")
				if responseCheckForTransaction(AuthToken,cookies) == 200:
					# print("Transaction passed")
					if responseCheckForTrade(AuthToken,cookies) == 200:
						# print("Trade passed")
						if responseCheckForCurrency(AuthToken,cookies) == 200:
							# print("Currency passed")
							if responseCheckForMarket(AuthToken,cookies) == 200:
								# print("Market passed")
								# print("Build deployed passes basic test cases")
								sendMail("New build deployed passed basic test cases")
							else:
								sendMail("Build deployed failed, roll back function has been started")
								onBuildFail(cookies)
						else:
							sendMail("Build deployed failed, roll back function has been started")
							onBuildFail(cookies)
					else:	
						sendMail("Build deployed failed, roll back function has been started")
						onBuildFail(cookies)
				else:
					sendMail("Build deployed failed, roll back function has been started")
					onBuildFail(cookies)
			else:
				sendMail("Build deployed failed, roll back function has been started")
				onBuildFail(cookies)
		else:
			sendMail("Build deployed failed, roll back function has been started")
			onBuildFail(cookies)
	else:
		sendMail("Build deployed failed, roll back function has been started")
		onBuildFail(cookies)					