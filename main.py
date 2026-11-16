import json,os,urllib.request as J
V=[0,100,320,330,500,900,0];M=9999;U=150000
KN=(-33,-31,-18,-14,14,18,31,33);KG=(-17,-16,-15,-1,1,15,16,17)
BD=(-17,-15,15,17);RD=(-16,-1,1,16)
Z=b'yyyyggo{b][jbeeV3BQQBblqBblq3BQSQ[[[VbejVejjQ][[beee[```[```]``bQ[[]X`ee[beeQ[]]B88.B88.QGGBtye`'
CT=((1,7,4,6),(2,0,4,2),(4,119,116,118),(8,112,116,114))
b=[0]*128;s=1;k=[4,116];n=[0]
W={0:13,7:14,4:12,112:7,119:11,116:3}
T={};G={}
def F(q):return"abcdefgh"[q&7]+str(q//16+1)
def A(q,y):
 for d in(15,17):
  n=q-d*y
  if not n&0x88 and b[n]==y:return 1
 for d in KN+KG:
  n=q+d
  if not n&0x88 and b[n]==y*(6-4*(d in KN)):return 1
 for d in BD+RD:
  n=q+d
  while not n&0x88:
   p=b[n]
   if p:
    if p in(y*5,y*3 if d in BD else y*4):return 1
    break
   n+=d
 return 0
def I(w):return A(k[w<0],-w)
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
    if b[n]*(dd==d or b[n]*s>0)or dd!=d and not b[n] and n!=e:continue
    if n//16==7*(s>0):
     for pr in(5,4,3,2):ms.append(f+n*128+pr*16384)
    elif not z or dd!=d:
     ms.append(f+n*128)
     if dd==d and f//16==1+5*(s<0) and not b[f+2*d]:ms.append(f*129+256*d)
  else:
   for d in((),(),KN,BD,RD,BD+RD,KG)[t]:
    n=f+d
    while not n&0x88:
     q=b[n]
     if q and q*s<0:ms.append(f+n*128)
     if q:break
     if not z:ms.append(f+n*128)
     if t%4==2:break
     n+=d
   if t==6 and not z:
    for c_,_,kf,kt in CT:
     j=(kt-kf)//2
     if c&c_ and not(b[kf+j]or b[kt]or b[kf-3]and j<0)and all(not A(q,-s)for q in(kf,kf+j,kt)):ms.append(kf+kt*128)
 return ms
def u(m):
 global s,c,e
 un=(b[:],s,c,e,k[:])
 f=m&127;t=(m>>7)&127;p=(m>>14)&7;pc=b[f]
 if t==e and pc*pc==1:b[t-16*s]=0
 b[f]=0;b[t]=p*s or pc
 if pc*pc==36:
  k[s<0]=t
  if abs(t-f)==2:
   rf=t+(t-f)//2-(t<f);rt=(f+t)//2;b[rt]=b[rf];b[rf]=0
 c&=W.get(f,15)&W.get(t,15);e=-1
 if pc*pc==1 and t-f==32*s:e=t-16*s
 s=-s
 return un
def v(un):
 global s,c,e
 b[:],s,c,e,k[:]=un
def L():
 sc=0
 for q,p in enumerate(b):
  if not p:continue
  t=abs(p);r,f=q>>4,q&7
  i=(3-r//2 if p>0 else r//2)*4+min(f,7-f)
  v=V[t]+Z[(t-1)*16+i]-96
  sc+=v*p//abs(p)
 return sc*s+10
def H(ms,j=0):
 def sc(m):
  f=m&127;t=(m>>7)&127;p=(m>>14)&7
  if m==j:return 1000000
  if b[t]*s<0 or t==e and abs(b[f])==1 or p:return 100000+10*V[abs(b[t])or 1]
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
 global s,e
 n[0]+=1
 if n[0]>=U:raise C()
 j=tuple(b)+(s,c,e)
 if G.get(j,0)>1:return 0
 ch=I(s)
 if ch:z+=1
 if z<=0:return Q(a,B,ply)
 ms=H(g(),T.get(j,0))
 bm=0;ln=0
 for m in ms:
  x=u(m)
  if I(-s):v(x);continue
  ln+=1
  sc=-d(z-1,-B,-a,ply+1)
  v(x)
  if sc>a:a=sc;bm=m
  if a>=B:break
 if ln==0:return -M+ply if ch else 0
 T[j]=bm
 return a
def r():
 ms=[]
 for m in g():
  x=u(m)
  if not I(-s):ms.append(m)
  v(x)
 ms=H(ms)
 best=ms[0];n[0]=0
 if len(T)>1e5:T.clear()
 for z in range(33):
  a=-M-1;bd=ms[0]
  try:
   for m in ms:
    x=u(m);S=-d(z,-M-1,-a,1);v(x)
    if S>a:a=S;bd=m
  except C:break
  best=bd;ms.remove(bd);ms.insert(0,bd)
  if a>=M-1000:break
 return best
def y(mv):
 global b,s,c,e,k
 b=[0]*128
 for i,p in enumerate((4,2,3,5,6,3,2,4)):b[i]=p;b[i+112]=-p;b[i+16]=1;b[i+96]=-1
 s=1;c=15;e=-1;k=[4,116];G.clear()
 for z in mv:
  f=(int(z[1])-1)*16+ord(z[0])-97;t=(int(z[3])-1)*16+ord(z[2])-97;p=0
  if len(z)==5:p=5-"qrbn".index(z[4])
  u(f+t*128+p*16384);j=tuple(b)+(s,c,e);G[j]=G.get(j,0)+1
if __name__=="__main__":
 t=lambda a,j:json.load(J.urlopen(os.getenv("MAKEFUN_ENV_URL")+a,json.dumps(j).encode()))
 while 1:
  a=t("/game",{})
  if a["status"][0]=="d":break
  while a["status"][0]=="y":
   y(a["moves"]);m=r();p=(m>>14)&7
   a=t("/move",{"game":a["game"],"move":F(m&127)+F((m>>7)&127)+(p and"qrbn"[5-p]or"")})
