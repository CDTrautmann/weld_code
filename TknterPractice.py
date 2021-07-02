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
Ymax_var = tk.StringVar()
Cool_var = tk.StringVar()

labels = ['q','U','alpha','k','T_o','T','d',]
variables = []
entries = []

for i,nam in enumerate(labels):
    en=tk.Entry(entrywindow)
    en.grid(row=i+1,column=1)
    entries.append(en)

for i,nam in enumerate(labels):
    lm=tk.Label(entrywindow,text=nam)
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
    #messagebox.showinfo(title='Regime',message = Reg)
    reg_var.set(str(Reg))


Reg_button=tk.Button(entrywindow,text='regime set',command=regimeset).grid(row=9,column=0)
Reg_value=tk.Label(entrywindow,textvariable=reg_var ).grid(row=1,column=3)
Reg_label=tk.Label(entrywindow,text='Regime: ').grid(row=1,column=2)

def YhazButton():

    y_window = tk.Tk()
    param_in = ['T_m',"T_haz"]
    Local_entry = []
    T_holder = {}
    try:
        int(reg_var.get())
    except:
        messagebox.showerror(title='Error',message='Please calculate Regime first')
        y_window.destroy()
    else:
        for i,named in enumerate(param_in):
            en=tk.Entry(y_window)
            en.grid(row=i+1,column=1)
            Local_entry.append(en)

    for i,named in enumerate(param_in):
        lm=tk.Label(y_window,text=named)
        lm.grid(row=i+1,column=2)

    def Ycalc():
        y_haz = 0
        for i,entry in enumerate(Local_entry):
            try:
                float(entry.get())
            except:
                messagebox.showerror(title='Type error',message='Enter numbers only')
                break
            else:
                T_holder[param_in[i]]=float(entry.get())
        Reg = int(reg_var.get())
        if Reg == 1:
            y_haz = np.sqrt(weldp['q']*weldp['alpha']/2/np.e/np.pi/weldp['k']/weldp['U'])*(T_holder['T_m']-T_holder['T_haz'])/((weldp['T']-weldp['T_o'])**(3/2))
            y_haz=np.round(y_haz,6)
        elif  Reg == 2:
            y_haz = (weldp['q']/2/np.pi/weldp['k'])*(T_holder['T_m']-T_holder['T_haz'])/(weldp['T']-weldp['T_o'])**2
            y_haz=np.round(y_haz,6)
        elif  Reg == 3:
            y_haz = weldp['q']*weldp['alpha']/np.sqrt(2*np.e*np.pi)/weldp['k']/weldp['d']/weldp['U']*(T_holder['T_m']-T_holder['T_haz'])/(weldp['T']-weldp['T_o'])**2
            y_haz=np.round(y_haz,6)
        elif Reg == 4:
            messagebox.showerror(title='error',message='not implemented')
            #gam = float(input('enter gamma '))
            #8*np.pi*weldp['k']*weldp['alpha']*weldp['d']/weldp['q']/weldp['U']*(T_m-T_haz)/np.exp(gam+(1/weldp['Ro']))
        else:
            messagebox.showinfo(title='Bad pass',message = 'Reg is passed incorrectly')
        Yhaz_var.set(y_haz)
        y_window.destroy()

    Calc_button = tk.Button(y_window,text='calculate',command=Ycalc).grid(row=3,column=1)
    y_window.mainloop()


Yhaz_button = tk.Button(entrywindow, text='Find Y_haz',command=YhazButton).grid(row=9,column=2)
Yhaz_value = tk.Label(entrywindow,textvariable=Yhaz_var).grid(row=2,column=3)
Yhaz_label = tk.Label(entrywindow,text='HAZ width: ').grid(row=2,column=2)

def YmaxButton():
    try:
        int(reg_var.get())
    except:
        messagebox.showerror(title='Error',message='Please calculate Regime first')
    else:
        Reg = int(reg_var.get())
        if Reg == 1:
            y_max = np.sqrt(2*weldp['alpha']*weldp['q']/np.pi/np.e/weldp['k']/weldp['U']/(weldp['T']-weldp['T_o']))
            y_max=np.round(y_max,6)
        elif Reg == 2:
            y_max = weldp['q']/2/np.pi/weldp['k']/(weldp['T']-weldp['T_o'])
            y_max=np.round(y_max,6)
        elif Reg == 3:
            y_max = np.sqrt(1/2/np.pi/np.e)*weldp['q']*weldp['alpha']/weldp['k']/weldp['d']/weldp['U']/(weldp['T']-weldp['T_o'])
            y_max=np.round(y_max,6)
        elif Reg == 4:
            messagebox.showerror(title='error',message='not implemented')
            #gam = float(input('enter gamma? '))
            #y_max = 4*np.exp(-gam)*weldp['alpha']/weldp['U']*np.exp(-1/weldp['Ro'])
            #y_max=np.round(y_max,6)    
        else:
            y_max = 'err'
            messagebox.showerror(title='Bad pass',message='Reg is passed incorrectly')
        Ymax_var.set(y_max)


Ymax_button=tk.Button(entrywindow,text='Find Ymax',command=YmaxButton).grid(row=9,column=3)
Ymax_value=tk.Label(entrywindow,textvariable=Ymax_var).grid(row=3,column=3)
Ymax_label=tk.Label(entrywindow,text='Ymax: ').grid(row=3,column=2)

def CoolButton():
    try:
        int(reg_var.get())
    except:
        messagebox.showerror(title='Error',message='Please calculate Regime first')
    else:
        Reg = int(reg_var.get())
        if Reg == 1 or Reg == 2:
            T_b = -2*np.pi*weldp['k']*weldp['U']/weldp['q']*(weldp['T']-weldp['T_o'])**2
            T_b=np.round(T_b,3)
        elif Reg == 3:
            T_b = -2*np.pi/weldp['alpha']*((weldp['k']*weldp['d']*weldp['U']/weldp['q'])**2)*(weldp['T']-weldp['T_o'])**3
            T_b=np.round(T_b,3)    
        elif Reg == 4:
            messagebox.showerror(title='error',message='not implemented')
            #gam = float(input('enter gamma '))
            #T_b = -weldp['q']/8/np.pi/weldp['k']/weldp['alpha']/weldp['d']*(weldp['U']**2)*np.exp(gam+(1/weldp['Ro']))
        else:
            T_b = 'err'
            messagebox.showerror(title='Bad pass',message='Reg is passed incorrectly')
        Cool_var.set(T_b)

Cool_button = tk.Button(entrywindow,text='Cool rate',command=CoolButton).grid(row=10,column=2)
Cool_value = tk.Label(entrywindow,textvariable=Cool_var).grid(row=4,column=3)
Cool_label =tk.Label(entrywindow,text='Cooling rate: ').grid(row=4,column=2)

entrywindow.mainloop()