from numpy import *
from matplotlib import pyplot as plt


##### Données #####
### Constantes ##
f = 155*10**3 #Hz, frequency of the signal
T = 1/ f #s, period of the signal
T_demi = T/2 #s, half period of the signal


tot = 3
steps = 300*tot #number of steps

end = T*tot #s, end of the simulation
t = linspace(0, end, steps) #s, time

h = 0.001 #s, step
# Bloc 1
Vcc = 5.5 #V, voltage of the power supply


R_G = 9*10**3 #Ohms, resistor in the circuit RL
C_G = 0.5*10**-9 #F, capacitor in the circuit RL
tau_G = T_demi / log(2)#s, time constant of the circuit RL









def scheme_bloc_1(f,R_G, C_G):
    V_in_moins = empty_like(t)
    V_in_plus = empty_like(t)
    V_out = empty_like(t)
    Vth1 = 1/3 * Vcc
    Vth2 = 2/3 * Vcc

    for i in range(tot):
        for j in range(int(len(t)/tot)):
            
            if t[i*int(len(t)/tot) + j] < (2*i+1)*T_demi:
                V_in_moins[i*int(len(t)/tot) + j] = Vcc - Vth2*exp(-(t[j])/tau_G)
                V_in_plus[i*int(len(t)/tot) + j] = Vth2
                V_out[i*int(len(t)/tot) + j] = Vcc

            else:
                V_in_moins[i*int(len(t)/tot) + j] = Vth2*exp(-(t[j]-T_demi)/tau_G)
                V_in_plus[i*int(len(t)/tot) + j] = Vth1
                V_out[i*int(len(t)/tot) + j] = 0

    
    plt.plot(t,V_in_moins, label = "V_in_moins")
    plt.plot(t,V_in_plus, label = "V_in_plus", color = "red")
    plt.plot(t,V_out, label = "V_out")
    plt.plot(t, array([Vth1 for i in range(len(t))]),linestyle =":", color ="black", label ="Vcc/3")
    plt.plot(t, array([Vth2 for i in range(len(t))]), linestyle =":",color ="black", label ="2Vcc/3")
    plt.xticks([])
    plt.yticks([])

    plt.legend()
    plt.show()
        

scheme_bloc_1(f,R_G, C_G)

