import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r'C:\Users\Carter\Documents\Python\welding_codes\weld_code\arc_data.xlsx')
print(type(df))
V_weld = df['Voltage'] #V
I_weld = df['Current'] #A
Rho_wire = 2.87e-13 #ohm/m
V_arc = 0.8e3 #V/m
CTWD =  df['CTWD']*0.001#m
R_lead = 8.2e-3 #ohm
R_ct = 0.2e-3 #ohm
V_an = 4.2 #V
V_ca = 11 # V

P = V_weld * I_weld
P_res = (I_weld**2)*(R_lead+R_ct)
P_fix = (V_an+V_ca)*(I_weld)
P_tot = P_res+P_fix

l_arc = (P-P_tot-(I_weld**2)*Rho_wire*CTWD)/(I_weld*(((I_weld**2)*Rho_wire)+V_arc))

print(l_arc*1000)

df['Arc Predicted'] = l_arc*1000

print(df)
ax = df.plot(kind='line', y = ['L_AC','Arc Predicted'], use_index= True)
plt.show()