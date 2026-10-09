import math
pi=math.pi
def quad(f,a,b,n=12000):
 h=(b-a)/n;return h/3*(f(a)+f(b)+4*sum(f(a+(2*k-1)*h) for k in range(1,n//2+1))+2*sum(f(a+2*k*h) for k in range(1,n//2)))
def check(name,value,expected):
 assert abs(value-expected)<1e-8*max(1,abs(expected)),(name,value,expected)
 print(name,'PASS',round(value,8))
check('抛物面加权积分',2*pi*quad(lambda r:r**3*math.sqrt(1+4*r*r),0,math.sqrt(2)),149*pi/30)
m=2*pi*quad(lambda r:r*math.sqrt(1+r*r),0,2)
zm=pi*quad(lambda r:r**3*math.sqrt(1+r*r),0,2)
check('抛物面壳质心',zm/m,(25*math.sqrt(5)+1)/(5*(5*math.sqrt(5)-1)))
check('分段有向积分',quad(lambda t:t**4-2*t*t,1,-1)+quad(lambda t:2+t+t*t,0,1),113/30)
check('奇点外圈积分',quad(lambda t:((1+2*math.cos(t))*2*math.cos(t)+4*math.sin(t)**2)/((1+2*math.cos(t))**2+8*math.sin(t)**2),0,2*pi),math.sqrt(2)*pi)
check('抛物面下侧通量',2*pi*quad(lambda r:(r*r+1)*r,0,1),3*pi/2)
check('半球补面通量直接计算',2*pi*quad(lambda p:(1+math.cos(p))*math.sin(p),0,pi/2),3*pi)
check('2021曲线第一型',quad(lambda t:12*t*math.sqrt(9+36*t*t+36*t**4),0,1),36)
# 侧面 r=z²，用参数 r(theta,z)，叉积=(z²cosθ,z²sinθ,-2z³)，指向外侧下方。
check('2021侧面通量直接参数化',quad(lambda z:-4*pi*z**5,0,1),-2*pi/3)
check('2023上半球下侧',-pi*quad(lambda p:math.sin(p)**3,0,pi/2),-2*pi/3)
check('圆环引力轴向',quad(lambda t:-2/(5**1.5),0,2*pi),-4*pi/(5**1.5))
print('10 independent numerical checks passed')
