# calculation functions
import numpy as np
def Ymax(weldp,Reg):
    if Reg == 1:
        y_max = np.sqrt(2*weldp['alpha']*weldp['q']/np.pi/np.e/weldp['k']/weldp['U']/(weldp['T']-weldp['T_o']))
    elif Reg == 2:
        y_max = weldp['q']/2/np.pi/weldp['k']/(weldp['T']-weldp['T_o'])
    elif Reg == 3:
        y_max = np.sqrt(1/2/np.pi/np.e)*weldp['q']*weldp['alpha']/weldp['k']/weldp['d']/weldp['U']/(weldp['T']-weldp['T_o'])
    elif Reg == 4:
        gam = float(input('enter gamma? '))
        y_max = 4*np.exp(-gam)*weldp['alpha']/weldp['U']*np.exp(-1/weldp['Ro'])
    else:
        y_max = 'err'
        print('regime error')
    return(y_max)

def Yhaz(weldp,Reg):
    T_m = float(input('enter melting temp '))
    T_haz = float(input('enter HAZ temp'))

    if Reg == 1:
        print('run Y1')
        y_haz = np.sqrt(weldp['q']*weldp['alpha']/2/np.e/np.pi/weldp['k']/weldp['U'])*(T_m-T_haz)/((weldp['T']-weldp['T_o'])**(3/2))
    elif  Reg == 2:
        y_haz = (weldp['q']/2/np.pi/weldp['k'])*(T_m-T_haz)/(weldp['T']-weldp['T_o'])**2
    elif  Reg == 3:
        y_haz = weldp['q']*weldp['alpha']/np.sqrt(2*np.e*np.pi)/weldp['k']/weldp['d']/weldp['U']*(T_m-T_haz)/(weldp['T']-weldp['T_o'])**2
    elif Reg == 4:
        gam = float(input('enter gamma '))
        8*np.pi*weldp['k']*weldp['alpha']*weldp['d']/weldp['q']/weldp['U']*(T_m-T_haz)/np.exp(gam+(1/weldp['Ro']))
    else:
        print('regime error')
    return(y_haz)

def CoolRate(weldp,Reg):
    T_m = [float(input('enter melt temperature'))]
    if Reg == 1 or Reg == 2:
        T_b = -2*np.pi*weldp['k']*weldp['U']/weldp['q']*(weldp['T']-weldp['T_o'])^2
    if Reg == 3:
        T_b = -2*np.pi/weldp['alpha']*((weldp['k']*weldp['d']*weldp['U']/weldp['q'])**2)*(weldp['T']-weldp['T_o'])**3
    if Reg == 4:
        gam = float(input('enter gamma '))
        T_b = -weldp['q']/8/np.pi/weldp['k']/weldp['alpha']/weldp['d']*(weldp['U']**2)*np.exp(gam+(1/weldp['Ro']))
    return(T_b)

def HeatRate(q,U,alpha,k,T,T_o,d,Ro,Reg):
    do=1
