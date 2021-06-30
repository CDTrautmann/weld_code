import tkinter as tk 
import tkinter.messagebox as messagebox
from typing import Text
import numpy as np


entrywindow =tk.Tk()
entrywindow.title('weld calc')
weldp = {}

y_haz =0
Reg = 0
intermed = 0
reg_var = tk.StringVar()
Yhaz_var = tk.StringVar()
labels = ['q','U','alpha','k','T_o','T','d',]
variables = []
entries = []

for i,nam in enumerate(labels):
    en = tk.Entry(entrywindow)
    en.grid(row=i+1,column=1)
    entries.append(en)

for i,nam in enumerate(labels):
    lm = tk.Label(entrywindow, text = nam)
    lm.grid(row = i+1)

def regimeset():
    
    for i,entry in enumerate(entries):
        try:
            float(entry.get())
        except:
            messagebox.showerror(title='Data type error', message = 'please enter numbers')
            break
        else:
            weldp[labels[i]]=float(entry.get())
        

    
    weldp['Ry']= weldp['q']*weldp['U']/(4*np.pi*weldp['k']*weldp['alpha']*(weldp['T']-weldp['T_o']))
    weldp['d_s'] = (weldp['U']*weldp['d'])/(2*weldp['alpha'])
    weldp['Ro'] = weldp['Ry']/weldp['d_s']

    Ry = weldp['Ry']
    d_s = weldp['d_s']
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
    messagebox.showinfo(title='Regime',message = Reg)
    reg_var.set(str(Reg))


Reg_button = tk.Button(entrywindow, text = 'regime set',command = regimeset).grid(row=9,column=0)
Reg_value = tk.Label(entrywindow, textvariable=reg_var ).grid(row = 1, column = 5 )
Reg_label = tk.Label(entrywindow, text='Regime: ').grid(row=1,column=4)

def YhazButton():
    def Ycalc():
        y_haz = 0
        try:
            print(Tm_in.get())
            float(Tm_in.get())
        except:
            messagebox.showerror(title='Type error',message='Enter numbers only')
        else:
            T_m = float(Tm_in.get())
            T_haz = float(Thaz_in.get())
        
        if Reg == 1:
            print('run Y1')
            y_haz = np.sqrt(weldp['q']*weldp['alpha']/2/np.e/np.pi/weldp['k']/weldp['U'])*(T_m-T_haz)/((weldp['T']-weldp['T_o'])**(3/2))
        elif  Reg == 2:
            y_haz = (weldp['q']/2/np.pi/weldp['k'])*(T_m-T_haz)/(weldp['T']-weldp['T_o'])**2
        elif  Reg == 3:
            y_haz = weldp['q']*weldp['alpha']/np.sqrt(2*np.e*np.pi)/weldp['k']/weldp['d']/weldp['U']*(T_m-T_haz)/(weldp['T']-weldp['T_o'])**2
        elif Reg == 4:
            messagebox.showerror(title='error',message='not implemented')
            #gam = float(input('enter gamma '))
            #8*np.pi*weldp['k']*weldp['alpha']*weldp['d']/weldp['q']/weldp['U']*(T_m-T_haz)/np.exp(gam+(1/weldp['Ro']))
        Yhaz_var.set(str(y_haz))
        y_window.destroy

    y_window = tk.Tk()
    Tm_in = tk.Entry(y_window).grid(row = 1,column=1)
    Thaz_in = tk.Entry(y_window).grid(row = 1,column = 2)
    Tm_label = tk.Label(y_window,text='Melting Temp').grid(row=2,column=1)
    Thaz_label = tk.Label(y_window,text = 'HAZ temperature').grid(row=2,column=2)
    Calc_button = tk.Button(y_window,text = 'calculate',command= Ycalc).grid(row=3,column=1)
    y_window.mainloop()
    
Yhaz_button = tk.Button(entrywindow, text='Find Y_haz',command=YhazButton).grid(row=9,column=2)
Yhaz_value = tk.Label(entrywindow,textvariable=Yhaz_var).grid(row=2,column=5)
Yhaz_label = tk.Label(entrywindow,text='HAZ width: ').grid(row=2,column=4)
entrywindow.mainloop()