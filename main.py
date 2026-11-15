import json,os,urllib.request as J
V=[0,100,320,330,500,900,0];M=9999;U=150000
KN=(-33,-31,-18,-14,14,18,31,33);KG=(-17,-16,-15,-1,1,15,16,17)
BD=(-17,-15,15,17);RD=(-16,-1,1,16);D=((),(),KN,BD,RD,BD+RD,KG)
Z=b'yyyyggo{b][jbeeV3BQQBblqBblq3BQSQ[[[VbejVejjQ][[beee[```[```]``bQ[[]X`ee[beeQ[]]B88.B88.QGGBtye`'
CT=((1,7,4,6),(2,0,4,2),(4,119,116,118),(8,112,116,114))
CR={6:(7,5),2:(0,3),118:(119,117),114:(112,115)}
b=[0]*128;s=1;k=[4,116];n=[0]
W=[15]*128
W[0]=13;W[7]=14;W[4]=12;W[112]=7;W[119]=11;W[116]=3
def F(q):return"abcdefgh"[q&7]+str((q>>4)+1)
def A(q,y):
 for d in(15,17):
  n=q-d*y
  if not n&0x88 and b[n]==y:return 1
 for d in KN+KG:
  n=q+d
  if not n&0x88 and b[n]==y*(2 if d in KN else 6):return 1
 for d in D[5]:
  n=q+d
  while not n&0x88:
   p=b[n]
   if p:
    if p in(y*5,y*3 if d in BD else y*4):return 1
    break
   n+=d
 return 0
def I(w):return A(k[0] if w>0 else k[1],-w)
def g(z=0):
 ms=[]
 for f,p in enumerate(b):
  if not p or p*s<=0:continue
  t=abs(p)
  if t==1:
   d=16*s
   for dd in(d-1,d,d+1):
    n=f+dd
    if n&0x88:continue
    if b[n] and(dd==d or b[n]*s>0)or dd!=d and not b[n] and n!=e:continue
    if n//16==(7+7*s)//2:
     for pr in(5,4,3,2):ms.append(f+n*128+pr*16384)
    elif not z or dd!=d:
     ms.append(f+n*128)
     if dd==d and f//16==(7-5*s)//2 and not b[f+2*d]:ms.append(f+(f+2*d)*128)
  else:
   for d in D[t]:
    n=f+d
    while not n&0x88:
     q=b[n]
     if q:
      if q*s<0:ms.append(f+n*128)
      break
     if not z:ms.append(f+n*128)
     if t%4==2:break
     n+=d
   if t==6 and not z:
    for c_,rk,kf,kt in CT:
     j=1 if kt>kf else-1
     if c&c_ and b[rk]==4*s and not b[kf+j]and not b[kt]and(j>0 or not b[kf+3*j])and not any(A(q,-s) for q in(kf,kf+j,kt)):ms.append(kf+kt*128)
 return ms
def u(m):
 global s,c,e
 un=(b[:],s,c,e,k[:])
 f=m&127;t=(m>>7)&127;p=(m>>14)&7;pc=b[f]
 if t==e and pc*pc==1:b[t-16*s]=0
 b[f]=0;b[t]=p*s or pc
 if pc*pc==36:
  k[0 if s>0 else 1]=t
  if abs(t-f)==2:
   rf,rt=CR[t];b[rt]=b[rf];b[rf]=0
 c&=W[f]&W[t];e=-1
 if pc*pc==1 and abs(t-f)==32:e=t-16*s
 s=-s
 return un
def v(un):
 global s,c,e
 b[:]=un[0];s,c,e=un[1],un[2],un[3];k[:]=un[4]
def L():
 sc=0
 for q,p in enumerate(b):
  if not p:continue
  t=abs(p);r,f=q>>4,q&7
  if f>3:f=7-f
  i=(3-r//2)*4+f if p>0 else(r//2)*4+f
  v=V[t]+Z[(t-1)*16+i]-96
  sc+=v if p>0 else -v
 return sc*s
def H(ms):
 def sc(m):
  f=m&127;t=(m>>7)&127;p=(m>>14)&7
  if b[t] and b[t]*s<0 or t==e and abs(b[f])==1 or p:return 100000+10*V[abs(b[t]or 1)]-V[abs(b[f])]//10
  return 0
 return sorted(ms,key=sc,reverse=True)
class C(Exception):pass
def Q(a,b,ply):
 n[0]+=1
 if n[0]>=U:raise C()
 ch=I(s)
 if not ch:
  st=L()
  if st>=b:return st
  if st>a:a=st
 ms=H(g(not ch));ln=0
 for m in ms:
  x=u(m)
  if I(-s):v(x);continue
  ln+=1
  S=-Q(-b,-a,ply+1)
  v(x)
  if S>=b:return S
  if S>a:a=S
 if ch and ln==0:return -M+ply
 return a
def d(z,a,B,ply):
 n[0]+=1
 if n[0]>=U:raise C()
 ch=I(s)
 if ch:z+=1
 if z<=0:return Q(a,B,ply)
 ms=H(g())
 ln=0
 for m in ms:
  x=u(m)
  if I(-s):v(x);continue
  ln+=1
  sc=-d(z-1,-B,-a,ply+1)
  v(x)
  if sc>a:a=sc
  if a>=B:break
 return a if ln else -M+ply if ch else 0
def r():
 ms=[]
 for m in g():
  x=u(m)
  if not I(-s):ms.append(m)
  v(x)
 ms=H(ms)
 if not ms:return None
 best=ms[0];n[0]=0
 for z in range(33):
  a=-M-1;bd=ms[0]
  try:
   for m in ms:
    x=u(m);S=-d(z,-M-1,-a,1);v(x)
    if S>a:a=S;bd=m
  except C:break
  best=bd
 return best
def o(w):
 f=(ord(w[1])-49)*16+ord(w[0])-97;t=(ord(w[3])-49)*16+ord(w[2])-97;p=0
 if len(w)==5:p=5-"qrbn".index(w[4])
 return f+t*128+p*16384
def y(mv):
 global b,s,c,e,k
 b=[0]*128
 for i,p in enumerate((4,2,3,5,6,3,2,4)):b[i]=p;b[i+112]=-p;b[i+16]=1;b[i+96]=-1
 s=1;c=15;e=-1;k=[4,116]
 for z in mv:u(o(z))
if __name__=="__main__":
 def p(a,j):return json.load(J.urlopen(os.environ["MAKEFUN_ENV_URL"]+a,json.dumps(j).encode()))
 while 1:
  a=p("/game",{})
  if a["status"]=="done":break
  while a["status"]=="your_move":
   y(a["moves"]);m=r()
   a=p("/move",{"game":a["game"],"move":F(m&127)+F((m>>7)&127)+("qrbn"[5-((m>>14)&7)] if(m>>14)&7 else"")})
