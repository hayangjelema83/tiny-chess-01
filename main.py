# PST eval + check-aware QS; trial-0 Elo 989.
import json as j,os,urllib.request as u
E=os.environ['MAKEFUN_ENV_URL']
def P(p,b):
 try:return j.load(u.urlopen(u.Request(E+p,j.dumps(b).encode())))
 except:exit()
KN=(-21,-19,-12,-8,8,12,19,21);BI=(-11,-9,9,11);RO=(-10,-1,1,10);QU=BI+RO
VL=dict(zip('PNBRQKpnbrqk',(100,320,330,500,900,0)*2))
PS='0233332025777652388998834699996337899873368998632566665202333320'
ST=' '*20+' rnbqkbnr '+' pppppppp '+' ........ '*4+' PPPPPPPP '+' RNBQKBNR '+' '*20
def mm(st,m):
 b,t,c,e=st;i,j,pr=m;p=b[i];d=list(b)
 if p in 'Pp' and j==e and d[j]=='.':q=j+10 if p=='P' else j-10;d[q]='.'
 if p in 'Kk' and abs(j-i)==2:d[j+1 if j>i else j-2]='.';d[j-1 if j>i else j+1]='R' if p=='K' else 'r'
 d[j]=pr or p;d[i]='.';ne=i-10 if p=='P' and i-j==20 else i+10 if p=='p' and j-i==20 else -1
 if p in 'Kk':c=c.replace(p,'').replace('Qq'[p=='k'],'')
 c=''.join(x for x in c if (98,91,28,21)['KQkq'.find(x)] not in (i,j))
 return ''.join(d),not t,c,ne
def ev(st):
 b,t=st[0],st[1];s=0
 for i,p in enumerate(b):
  if p in VL:
   q=(9-i//10)*8+i%10-1;v=VL[p]
   if p not in 'Kk':v+=int(PS[q if p.isupper() else 63-q])*6
   if p=='P':v+=(8-i//10)*8
   elif p=='p':v+=(i//10-3)*8
   s+=v if p.isupper() else -v
 s+=30*(b.count('B')>=2)-30*(b.count('b')>=2)
 return s if t else -s
def at(b,q,w):
 if any(b[q+d]==('P' if w else 'p') for d in ((11,9) if w else (-11,-9))):return 1
 for ds,pc in ((KN,'N' if w else 'n'),(QU,'K' if w else 'k')):
  if any(b[q+d]==pc for d in ds):return 1
 for d,pc in ((BI,'BQ' if w else 'bq'),(RO,'RQ' if w else 'rq')):
  for s in d:
   z=q+s
   while b[z]=='.':z+=s
   if b[z] in pc:return 1
 return 0
def gm(st):
 b,t,c,e=st;mv=[];ow='PNBRQK' if t else 'pnbrqk';fo=ow.swapcase();dr=-10 if t else 10;sr=8 if t else 3;prr=2 if t else 9
 for i,p in enumerate(b):
  if p not in ow:continue
  if p in 'Pp':
   r=i//10;pm=('QRBN' if t else 'qrbn') if r+dr//10==prr else ('',);q=i+dr
   if b[q]=='.':
    mv+=[(i,q,z) for z in pm]
    if r==sr and b[q+dr]=='.':mv.append((i,q+dr,''))
   for o in (dr-1,dr+1):
    q=i+o
    if b[q] in fo or q==e:mv+=[(i,q,z) for z in pm]
  else:
   ds=(KN if p in 'Nn' else QU if p in 'Kk' else BI if p in 'Bb' else RO if p in 'Rr' else QU);sl=p in 'BbRrQq'
   for d in ds:
    q=i+d
    while b[q]=='.' or b[q] in fo:
     mv.append((i,q,''))
     if not sl or b[q]!='.':break
     q+=d
 ks=95 if t else 25
 for s,rr,ro in ((1,'K' if t else 'k',3),(-1,'Q' if t else 'q',-4)):
  d=ks+2*s;rf=ks+ro
  if rr in c and b[rf]==('R' if t else 'r') and all(b[ks+i*s]=='.' for i in (1,2,3) if s<0 or i<3) and not any(at(b,ks+i*s,not t) for i in (0,1,2)):mv.append((ks,d,''))
 return mv
MA=10**5;nd=0;LI=1e9
def om(st,ms):
 b=st[0]
 return sorted(ms,key=lambda m:-(VL.get(m[2],0)*10+VL.get(b[m[1]],0)))
class A(Exception):...
def se(st,d,a,be,pl):
 global nd;nd+=1
 if nd>LI:raise A
 b,t,c,e=st;ks='K' if t else 'k';ck=at(b,b.index(ks),not t)
 if d<=0:
  if ck:be2=-MA
  else:
   sn=ev(st)
   if sn>=be:return sn
   a=max(a,sn);be2=sn
 else:be2=-MA
 ms=om(st,gm(st) if d>0 or ck else [m for m in gm(st) if b[m[1]]!='.' or m[1]==e and b[m[0]] in 'Pp'])
 lg=0
 for m in ms:
  ns=mm(st,m)
  if at(ns[0],ns[0].index(ks),not t):continue
  lg+=1;v=-se(ns,d-1,-be,-a,pl+1);be2=max(be2,v);a=max(a,v)
  if a>=be:break
 if lg==0:return -MA+pl if ck else 0 if d>0 else be2
 return be2
def rs(st,lg,bd):
 global nd,LI;nd=0;LI=bd;od=om(st,lg);bm=od[0];d=1
 while nd<bd:
  try:
   a=-MA;cb=bm
   for m in od:
    v=-se(mm(st,m),d-1,-MA,-a,1)
    if v>a:a=v;cb=m
   bm=cb
  except A:break
  d+=1
 return bm
def um(u,w):
 f=lambda s:ord(s[0])-10*int(s[1])+4
 return (f(u[:2]),f(u[2:4]),(u[4].upper() if w else u[4]) if len(u)==5 else '')
def mu(m):
 return ''.join(chr(96+i%10)+str(10-i//10) for i in m[:2])+(m[2].lower() if m[2] else '')
BD=90000
while True:
 g=P('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  st=(ST,True,'KQkq',-1)
  for v in g['moves']:st=mm(st,um(v,st[1]))
  lu=g['legal_moves'];ch=lu[0] if len(lu)==1 else mu(rs(st,[um(x,st[1]) for x in lu],BD))
  g=P('/move',{'game':g['game'],'move':ch})
