"""Check original homework coverage and independently integrate selected answers."""
from pathlib import Path
import re
import math

ROOT = Path(__file__).resolve().parents[1]
expected = set()
for batch, counts in [('第一次作业', (5,5,4)), ('第二次作业',(5,5,5)), ('第三次作业',(4,4,5))]:
    for kind, count in zip(('选择题','填空题','计算题'), counts):
        expected.update((batch, kind, str(n)) for n in range(1,count+1))
observed = []
for page in sorted(ROOT.glob('chapter*/homework*.md')):
    text = page.read_text()
    ids = re.findall(r'^## (第.次作业) · (选择题|填空题|计算题)(\d+)$',text,re.M)
    observed.extend(ids)
    for field in ('**原题**','**对应知识点**','**解题过程**'):
        assert text.count(field)==len(ids), (page.name,field)
assert len(observed)==len(set(observed))==42
assert set(observed)==expected, (expected-set(observed),set(observed)-expected)
print('PASS: all 42 original homework IDs appear exactly once with three required fields')

pi=math.pi
sin,cos,sqrt,exp=math.sin,math.cos,math.sqrt,math.exp

def quad(f,a,b,n=1200):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+(2*k-1)*h) for k in range(1,n//2+1))+2*sum(f(a+2*k*h) for k in range(1,n//2)))

def check(name,value,target):
    assert abs(value-target)<1e-7*max(1,abs(target)), (name,value,target)
    print('PASS:',name,round(value,9))

# Use original geometry/paths, including source inconsistencies and singular cases.
check('first work choice4 tilted great circle',quad(lambda t:3*(cos(t)/sqrt(2)+sin(t)/sqrt(6))*(-cos(t)/sqrt(2)+sin(t)/sqrt(6)),0,2*pi),-pi)
check('first work choice5 actual distance to axis',quad(lambda z:quad(lambda t:1+z*z-(cos(t)+sin(t)+z)**2/3,0,2*pi,120),0,3,120),16*pi)
check('first work calculation1 tilted circle',quad(lambda t:(sqrt(9*cos(t)**2+9*sin(t)**2)+4.5*cos(t)**2)*3,0,2*pi),63*pi/2)
check('first work calculation2 cone',2*pi*quad(lambda r:r**3*sqrt(2),0,2),8*sqrt(2)*pi)
check('first work calculation4 centroid',quad(lambda r:.5*r*r*r*sqrt(1+r*r),0,2)/quad(lambda r:r*sqrt(1+r*r),0,2),(25*sqrt(5)+1)/(5*(5*sqrt(5)-1)))
check('second work filling1 directed segments',quad(lambda t:t**4-2*t*t,1,-1)+quad(lambda t:(t+2)**2-t,-1,0),113/30)
check('second work filling2 shifted circle',quad(lambda t:((2*cos(t))*(2*cos(t))-(1+2*sin(t))*(-2*sin(t)))/4,0,2*pi),2*pi)
check('second work filling5 force along segment',quad(lambda t:t*2-(1+2*t)*3+(1+9*t)*4,0,1),17)
check('second work calculation2 actual circular arc',quad(lambda t:((1+sin(t))+exp(1+sin(t))/(1+cos(t)))*(-sin(t))+exp(1+sin(t))*math.log(1+cos(t))*cos(t),-pi/2,0),1-pi/4+math.e*math.log(2))
check('second work calculation5 shifted singular contour',quad(lambda t:((1+2*cos(t))*2*cos(t)+4*sin(t)**2)/((1+2*cos(t))**2+8*sin(t)**2),0,2*pi),sqrt(2)*pi)
check('third work calculation1 cylinder',quad(lambda t:4*sin(t)**2*(2-2*cos(t)),0,2*pi),8*pi)
# Direct flux with a nonconstant continuous f, not the divergence simplification.
def flux2(z,t):
    r=sqrt(max(0,1-z**4)); x,y=r*cos(t),r*sin(t); f=exp(x*x-y*y)
    return (x*x+y*z*f)*x+(y*y+x*z*f)*y+(z*z+x*y*f)*2*z**3
check('third work calculation2 direct flux with f=exp',quad(lambda z:quad(lambda t:flux2(z,t),0,2*pi,120),0,1,120),2*pi/3)
check('third work calculation3 removable normal factors',quad(lambda z:quad(lambda t:2/cos(sqrt(1-z*z)*cos(t))**2+(sqrt(1-z*z)*sin(t))/cos(sqrt(1-z*z)*sin(t))**2-1/cos(z)**2,0,2*pi,120),-1,1,240),4*pi*math.tan(1))
# Direct parameter flux of y=1+r² with outward downward normal.
def flux4(r,t):
    x,z=r*cos(t),r*sin(t); y=1+r*r
    return ((8*y+1)*x)*(2*r*r*cos(t))+2*(1-y*y)*(-r)+(-4*y*z)*(2*r*r*sin(t))
check('third work calculation4 direct paraboloid flux',quad(lambda r:quad(lambda t:flux4(r,t),0,2*pi,120),0,sqrt(2),120),34*pi)
# Independently integrate the spatial polygon boundary for Stokes homework.
vertices=[(1,0,1),(0,1,1),(-1,0,3),(0,-1,3),(1,0,1)]
value=0
for a,b in zip(vertices,vertices[1:]):
    delta=tuple(b[i]-a[i] for i in range(3))
    def integrand(t):
        x,y,z=(a[i]+t*delta[i] for i in range(3))
        return (y*y-z*z)*delta[0]+(2*z*z-x*x)*delta[1]+(3*x*x-y*y)*delta[2]
    value+=quad(integrand,0,1)
check('third work calculation5 actual polygon boundary',value,-24)
print('15 independent numerical checks passed')
