import math
import numpy as np
import matplotlib.pyplot as plt

class heated_tank:
    def __init__(self, P ,T, T_init, T_env, T_in, T_set, Q, F, c, p, V, m, G, Tau):
        self.P = P      # Effekten til oppvarming av vannet i tanken     
        self.T = T      # Faktiske temperaturen til vannet i tanken
        self.T_init = T_init # Initial temperature
        self.T_env = T_env   # Enviromental temperature
        self.T_in = T_in     # Temperature of liquid inflow
        self.T_set = T_set   # Set point for temp out of tank
        self.Q = Q      # Liquid Volumetric flow
        self.F = F      # Liquid mass flow
        self.c = c      # Spesific heat capacity of liquid
        self.p = p      # Density of liquid
        self.V = V      # Liquid volume in tank
        self.m = m      # Liquid mass in tank
        self.G = G      # Heat transfer coefficient of tank
        self.Tau = Tau  # Time delay

    def constant_power(self):
        P_0 = -(self.c*self.p*self.Q*(self.T_in-self.T_set)) + self.G*(self.T_env-self.T_set)

        self.P = P_0    
        print(self.P)
    def temperature(self):
        pass
    def simulation(self):
        dt = 1
        t_start = 0
        t_stop= 100
        N_sim = int((t_stop-t_start))

        t_array = np.zeros(N_sim)
        T_array = np.zeros(N_sim)
        T_in_array = np . zeros ( N_sim )
        T_env_array = np . zeros ( N_sim )
        P_array = np . zeros ( N_sim )

        T_min = 0
        T_max = 100

        T_k = self.T_init 
        for k in range (0 , N_sim):
            # State limitation :
            T_k = np.clip(T_k, T_min , T_max )
            t_k = k * dt
            P_k = self.P
            T_in_k = self.T_in
            T_env_k = self.T_env
            t_array [ k ] = t_k
            T_array [ k ] = T_k
            T_in_array [ k ] = T_in_k
            T_env_array [ k ] = T_env_k
            P_array [ k ] = P_k
            # Time derivative :
            dT_dt_k = ((1/( self.c * self.p * self.V ))*(P_k + ( self.c * self.p * self.Q )*( self.T_in - T_k ) + self.G *( self.T_env - T_k )))
            T_kp1 = T_k + dt * dT_dt_k
            # Time index shift :
            T_k = T_kp1




    def plotting(self):
        pass

        

if __name__=="__main__":
    hei = heated_tank(0, 0, 20, 20, 20,25,0.25*10**(-3),0.25, 4200, 1000, 0.2,200,100,60)
    hei.constant_power()
