import numpy as np
from matplotlib import pyplot as plt


# ---- Constants ----
Vcc = 5.5 #V, voltage of the power supply
R_L = 330 #Ohms, resistor in the circuit RL
L = 490*10**-6 #mH, inductance without metal
tau = L/R_L


f = 155*10**3 #Hz, frequency of the signal
# ---- Periods ---- 
T = 1/ f #s, period of the signal
T_demi = T/2 #s, half period of the signal
print(f"La demi période est de {T_demi:.2e} s")

# ---- Paramètre de la simulation ---- 
n = 10 #nombre d'itérations
num_values = 2000 #nombre de valeurs pour la simulation

V_max = np.empty(n)
V_min = np.empty(n)

times = np.empty((n,num_values))

Charges = np.empty((n,num_values))
Discharges = np.empty((n,num_values))





# ---- Functions ----
def V_L_Charge_func(t, Min, Vcc,i) : 
    V_L_Charge = lambda t : Vcc + (Min -Vcc)*np.e**(-(t-i*T_demi)/tau)
    return V_L_Charge(t)
def V_L_Discharge_func(t, Max, Vcc,i) : 
    V_L_Discharge = lambda t : Max*np.e**(-(t-i*T_demi)/tau)

    return V_L_Discharge(t)






# ---- Calculations ---- 

Min = 0
for i in range(0,2*n,2) : 
    j = i//2
    #Nous allons calculer à n reprises les courbes de charge et de décharge
    t = np.linspace(j*T, (j+1)*T, num_values)
    
    times[j,:] = t
    

    Charges[j,:] = V_L_Charge_func(t, Min, Vcc, i)
    Max = V_L_Charge_func((i+1)*T_demi, Min, Vcc, i)
    
    Discharges[j,:] = V_L_Discharge_func(t, Max, Vcc, i+1)
    
    Min = V_L_Discharge_func((j+1)*T, Max, Vcc, i+1)
    V_max[j] = Max
    V_min[j] = Min
    



# ---- Print ----
print(f"V_max = {V_max}")
print(f"V_min = {V_min}")

print(" ----- Diff btw the last max : ", V_max[-1]-V_max[-2]) 
print("--------------------------------------------------------------------------------")
print(" ----- Distance between the last min and the Vcc/2 : ", Vcc/2-V_min[-1])
print(" ----- Distance between the last max and the Vcc/2 : ", V_max[-1] - Vcc/2)
print(" ----- Stabilisation : ", Vcc/2-V_min[-1] - (V_max[-1] - Vcc/2))
print(f'Last max is : ¸{V_max[-1]}')

# ---- Plot ----
plt.plot(times[0,0:int(num_values/2 + 3)], Charges[0,0:int(num_values/2+ 3)], "-r", label="Discharge")
plt.plot(times[0,int(num_values/2- 3)::], Discharges[0,int(num_values/2- 3)::], "-b", label="Discharge")
plt.plot(times[1,0:int(num_values/2+ 3)], Charges[1,0:int(num_values/2+ 3)], "-r")
plt.plot(times[1,int(num_values/2- 3)::], Discharges[1,int(num_values/2- 3)::], "-b")
plt.plot(times[2,0:int(num_values/2+ 3)], Charges[2,0:int(num_values/2+ 3)], "-r")
plt.plot(times[2,int(num_values/2- 3)::], Discharges[2,int(num_values/2- 3)::], "-b")
plt.plot(times[3,0:int(num_values/2+ 3)], Charges[3,0:int(num_values/2+ 3)], "-r")
plt.plot(times[3,int(num_values/2- 3)::], Discharges[3,int(num_values/2- 3)::], "-b")
plt.plot(times[4,0:int(num_values/2+ 3)], Charges[4,0:int(num_values/2+ 3)], "-r")
plt.plot(times[4,int(num_values/2- 3)::], Discharges[4,int(num_values/2- 3)::], "-b") 
plt.plot(times[5,0:int(num_values/2+ 3)], Charges[5,0:int(num_values/2+ 3)], "-r")
plt.plot(times[5,int(num_values/2- 3)::], Discharges[5,int(num_values/2- 3)::], "-b")
plt.plot(times[6,0:int(num_values/2+ 3)], Charges[6,0:int(num_values/2+ 3)], "-r")
plt.plot(times[6,int(num_values/2- 3)::], Discharges[6,int(num_values/2- 3)::], "-b")
plt.plot(times[7,0:int(num_values/2+ 3)], Charges[7,0:int(num_values/2+ 3)], "-r")
plt.plot(times[7,int(num_values/2- 3)::], Discharges[7,int(num_values/2- 3)::], "-b")


all_times = np.concatenate(times)
plt.plot(all_times, np.array([Vcc/2 for i in range(len(all_times))]), "--k", label="Vcc")


plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.show()
