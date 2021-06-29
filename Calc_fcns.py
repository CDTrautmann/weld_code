# calculation functions
import numpy as np
def Ymax(q,U,alpha,k,T,T_o,d,Ro,Reg):
    if Reg == 1:
        y_max = np.sqrt(2*alpha*q/np.pi/np.e/k/U/(T-T_o))
    elif Reg == 2:
        y_max = q/2/np.pi/k/(T-T_o)
    elif Reg == 3:
        y_max = np.sqrt(1/2/np.pi/np.e)*q*alpha/k/d/U/(T-T_o)
    elif Reg == 4:
        gam = float(input('enter gamma? '))
        y_max = 4*np.exp(-gam)*alpha/U*np.exp(-1/Ro)
    else:
        y_max = 'err'
        print('regime error')
    return(y_max)

def Yhaz(q,U,alpha,k,T_o,T,d,Ro,Reg,):
    T_m = float(input('enter melting temp '))
    T_haz = float(input('enter HAZ temp'))

    if Reg == 1:
        print('run Y1')
        y_haz = np.sqrt(q*alpha/2/np.e/np.pi/k/U)*(T_m-T_haz)/((T-T_o)**(3/2))
        print(alpha)
    elif  Reg == 2:
        y_haz = (q/2/np.pi/k)*(T_m-T_haz)/(T-T_o)**2
    elif  Reg == 3:
        y_haz = q*alpha/np.sqrt(2*np.e*np.pi)/k/d/U*(T_m-T_haz)/(T-T_o)**2
    elif Reg == 4:
        gam = float(input('enter gamma '))
        8*np.pi*k*alpha*d/q/U*(T_m-T_haz)/np.exp(gam+(1/Ro))
    else:
        print('regime error')
    return(y_haz)

def CoolRate(q,U,alpha,k,T,T_o,d,Ro,Reg):
    T_m = [float(input('enter melt temperature'))]
    if Reg == 1 or Reg == 2:
        T_b = -2*np.pi*k*U/q*(T-T_o)^2
    if Reg == 3:
        T_b = -2*np.pi/alpha*((k*d*U/q)**2)*(T-T_o)**3
    if Reg == 4:
        gam = float(input('enter gamma '))
        T_b = -q/8/np.pi/k/alpha/d*(U**2)*np.exp(gam+(1/Ro))
    return(T_b)

def HeatRate(q,U,alpha,k,T,T_o,d,Ro,Reg):
    do=1
