import numpy as np
import Calc_fcns
import tkinter as tk
import tkinter.messagebox as messagebox


def GUiTest():

    root = tk.Tk()
    label=tk.Label(root, text='make a selection',padx=20,pady=20)
    label.pack()

    ent = tk.Entry(root)
    ent.pack()
    
    Coolbutt = tk.Button(root, text='cool rate')
    Coolbutt.pack()

    parbutt = tk.Button(root, text="Ymax", command = ParamIn)
    parbutt.pack()
    root.mainloop()


# function to take user parameters
def ParamIn():
    weldp = {}
    weldp['q'] = float(input('enter heat input '))
    weldp['U'] = float(input('enter travel speed '))
    weldp['alpha'] = float(input('enter thermal diffusivity '))
    weldp['k'] = float(input('enter thermal conductivity '))
    weldp['T_o'] = float(input('enter ambient temperature in C '))
    weldp['T']=float(input('enter intermediate temperature '))
    weldp['d']= float(input('enter plate thickness(m) '))
    weldp['Ry']= weldp['q']*weldp['U']/(4*np.pi*weldp['k']*weldp['alpha']*(weldp['T']-weldp['T_o']))
    weldp['d_s'] = (weldp['U']*weldp['d'])/(2*weldp['alpha'])
    weldp['Ro'] = weldp['Ry']/weldp['d_s']
    return(weldp)

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
def FuncCall(calc_pref,Reg,intermed,weldp):
    if calc_pref == 0:
        print('done')
    elif calc_pref == 1:
        y_haz = Calc_fcns.Yhaz(weldp,Reg)
        print(y_haz)
    elif calc_pref == 2:
        Tb = Calc_fcns.CoolRate(weldp,Reg)
        print(Tb)
    elif calc_pref == 3:
        y_max = Calc_fcns.Ymax(weldp,Reg)
        print(y_max)

def main():
    weldp = ParamIn()
    Reg,intermed= regimeSet(weldp['Ry'],weldp['d_s'])
    calc_pref = FuncChoose()
    FuncCall(calc_pref,Reg,intermed,weldp)

main()