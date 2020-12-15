# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:22:56 2020

@author: gwenv
"""

import scipy.integrate as integrate
from math import *

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
     summ = summ + v**(k) * t_p_x(k,x)
    return summ 

def Axn(i,x,n):
    v = 1/(1+i)
    summ = 0
    for k in range(0,n):
      summ = summ + ((1+k)*(v**(k+1)) * ((t_p_x(k,x)*(1-t_p_x(1,x+k)))))
    return summ

print(Axn(i,x,n))
print(axn(i,x,n))
