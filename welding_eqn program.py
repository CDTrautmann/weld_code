import numpy as np
import Calc_fcns

# function to take user parameters
def ParamIn():
    q = float(input('enter heat input '))
    U = float(input('enter travel speed '))
    alpha = float(input('enter thermal diffusivity '))
    k = float(input('enter thermal conductivity '))
    T_o = float(input('enter ambient temperature in C '))
    T = float(input('enter intermediate temperature '))
    d= float(input('enter plate thickness(m) '))
    Ry= q*U/(4*np.pi*k*alpha*(T-T_o))
    d_s = (U*d)/(2*alpha)
    Ro = Ry/d_s
    return(q,U,alpha,k,T_o,T,d,Ry,d_s,Ro)

# function to determine regime
def regimeSet(Ry,d_s):
    Reg=0
    intermed=0
    if Ry<10 and Ry>0.1 and d_s<10 and d_s>0.1:
        intermed = 1 

    if Ry > 1:
        if d_s > np.sqrt(np.pi*Ry/2):
            Reg = 1
        else:
            Reg = 3
    if Ry < 1:
        if d_s > -Ry*np.log(Ry):
            Reg = 2
        elif d_s > Ry:
            Reg = 4
        else:
            Reg = 3

    print(' ')
    print('Ry=',Ry)
    print('d*=',d_s)
    print(' your regime is ',Reg)
    if intermed == 1:
        print('you are in an intemediate regime')
        print('intermediate corrections not implemented')
    print(' ')
    return(Reg,intermed)

# User selects what to calculate
def FuncChoose():
    print(' please enter a number to select your calculation')
    print('[0] to end program')
    print('[1] for HAZ width')
    print('[2] for centerline cooling rate')
    print('[3] for Ymax')
    calc_pref  = 0
    calc_pref = int(input())
    return(calc_pref)

# call the function the User chose
def FuncCall(calc_pref,q,U,alpha,k,T_o,T,d,Ry,d_s,Ro,Reg,intermed):
    if calc_pref == 0:
        print('done')
    elif calc_pref == 1:
        y_haz = Calc_fcns.Yhaz(q,U,alpha,k,T_o,T,d,Ro,Reg)
        print(y_haz)
    elif calc_pref == 2:
        Tb = Calc_fcns.CoolRate(q,U,alpha,k,T,T_o,d,Ro,Reg)
        print(Tb)
    elif calc_pref == 3:
        y_max = Calc_fcns.Ymax(q,U,alpha,k,T,T_o,d,Ro,Reg)
        print(y_max)

def main():
    q,U,alpha,k,T_o,T,d,Ry,d_s,Ro = ParamIn()
    Reg,intermed = regimeSet(Ry,d_s)
    calc_pref = FuncChoose()
    FuncCall(calc_pref,q,U,alpha,k,T_o,T,d,Ry,d_s,Ro,Reg,intermed)

main()