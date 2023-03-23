import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#df = pd.read_excel(r'C:\Users\Carter\Documents\Python\welding_codes\weld_code\arc_data.xlsx')
#print(type(df))
#V_weld = df['Voltage'] #V
#I_weld = df['Current'] #A
I_weld = np.linspace(150,300,5)
V_weld = np.linspace(15,35,21)
Rho_wire = 2.87e-13 #ohm/m
V_arc = 0.8e3 #V/m
#CTWD =  df['CTWD']*0.001#m
CTWD = 14.5e-3#m
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
    pt = plt.plot(V_weld,l_arc_array[dex,1:])


plt.show()

""" P = V_weld * I_weld
P_res = (I_weld**2)*(R_lead+R_ct)
P_fix = (V_an+V_ca)*(I_weld)
P_tot = P_res+P_fix

l_arc = (P-P_tot-(I_weld**2)*Rho_wire*CTWD)/(I_weld*(((I_weld**2)*Rho_wire)+V_arc))

print(l_arc*1000)

 """#df['Arc Predicted'] = l_arc*1000

#print(df)
#ax = df.plot(kind='line', y = ['L_AC','Arc Predicted'], use_index= True)
#plt.show()