import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def Arc_sweep():
    I_weld = np.linspace(100,300,7)
    V_weld = np.linspace(15,35,21)
    Rho_wire = 2.87e-13 #ohm/m
    V_arc = 0.8e3 #V/m
    CTWD = 25.4e-3#m
    R_lead = 8.2e-3 #ohm
    R_ct = 0.2e-3 #ohm
    V_an = 4.2 #V
    V_ca = 11 # V
    l_arc_array = np.zeros((len(I_weld),len(V_weld)+1))

    for row,I in enumerate(I_weld):
        l_arc_array[row,0] = I
        for col,V in enumerate(V_weld):
            P = V*I
            P_res = (I**2)*(R_lead+R_ct)
            P_fix = (V_an+V_ca)*I
            P_tot = P_res+P_fix
            l_arc = (P-P_tot-(I**2)*Rho_wire*CTWD)/(I*(((I**2)*Rho_wire)+V_arc))
            l_arc_array[row,col+1] = l_arc*1000

    print(l_arc_array[0,:])


    for dex,cur in enumerate(l_arc_array[:,0]):
        pt = plt.plot(V_weld,l_arc_array[dex,1:],label = str(l_arc_array[dex,0]))
    pt = plt.plot(V_weld,np.zeros((len(V_weld))),label = 'short circuit')
    pt = plt.plot(V_weld,np.zeros((len(V_weld)))+(CTWD*1000), label = 'burn back limmit')
    pt = plt.plot(V_weld,np.zeros(len(V_weld))+12.7)
    plt.legend()
    plt.xlabel('voltage (V)')
    plt.ylabel('Arc length (mm)')
    plt.show()


def arc_pred_Al(V_weld,I_weld,CTWD):
    #df = pd.read_excel(r'C:\Users\Carter\Documents\Python\welding_codes\weld_code\arc_data.xlsx')
    #print(type(df))
    #V_weld = df['Voltage'] #V
    #I_weld = df['Current'] #A
    Rho_wire = 2.87e-13 #ohm/m
    V_arc = 0.8e3 #V/m
    R_lead = 8.2e-3 #ohm
    R_ct = 0.2e-3 #ohm
    V_an = 4.2 #V
    V_ca = 11 # V
    P_res = (I_weld**2)*(R_lead+R_ct)
    P_fix = (V_an+V_ca)*(I_weld)
    P_tot = P_res+P_fix
    P = V_weld * I_weld
    l_arc = (P-P_tot-(I_weld**2)*Rho_wire*CTWD)/(I_weld*(((I_weld**2)*Rho_wire)+V_arc))
    return(l_arc)


def find_CTWD(Arc_l,V_weld,I_weld):
    Rho_wire = 2.87e-13 #ohm/m
    V_arc = 0.8e3 #V/m
    R_lead = 8.2e-3 #ohm
    R_ct = 0.2e-3 #ohm
    V_an = 4.2 #V
    V_ca = 11 # V
    P_res = (I_weld**2)*(R_lead+R_ct)
    P_fix = (V_an+V_ca)*(I_weld)
    P_tot = P_res+P_fix
    P = V_weld * I_weld
    CTWD = ((I_weld*Arc_l*(((I_weld**2)*Rho_wire)+V_arc))+P_tot-P)/((I_weld**2)*Rho_wire)
    return(CTWD)


Arc_sweep()