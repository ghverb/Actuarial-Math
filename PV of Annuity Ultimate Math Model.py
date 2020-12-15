import scipy.integrate as integrate
from math import *
def s_p_x(s,x,A=0.00022,B=.0000027,C=1.124):
    f_o_m_s = lambda r: (0.9**(2-r))*(A+B*(C**(x+r)))
    p = integrate.quad(f_o_m_s,0,s)
    num = p[0] 
    p = exp(-1*num)
    return p 

def t_p_x(t,x,A=0.00022,B=.0000027,C=1.124):
    f_o_m = lambda u: A+B*(C**(x+u))
    q = integrate.quad(f_o_m,0,t)
    numb = q[0] 
    q = exp(-1*numb)
    return q 

def axn(i,x,n):
    v = 1/(1+i)
    summ = 0
    for k in range(0,n):
        if k <= 2:
            summ = summ + v**(k) * s_p_x(k+1,x+1)
        else:
            summ = summ + v**(k) * t_p_x(k-1,x+1) * s_p_x(1,x+1)
    return summ 

def Axn(i,x,n):
    v = 1/(1+i)
    summ2 = 0
    for k in range(0,n):
        if k < 2:
            summ2 = summ2 + (v**(k+1) * (s_p_x(k+1,x) - s_p_x(k+2,x)))
        elif k == 2:
            summ2 = summ2 + (v**(k+1) * (s_p_x(k+1,x+1) - (s_p_x(k+1,x) * (t_p_x(k,x+2)))))
        else:
            summ2 = summ2 + (v**(k+1) * ((s_p_x(2,x)*(t_p_x(k-1,x+2)-t_p_x(k,x+2)))))
    return summ2
'''
Input i in decimal form, x from select, and n term'''
print(Axn(i,x,n)) #ultimate
print(axn(i,x,n))


