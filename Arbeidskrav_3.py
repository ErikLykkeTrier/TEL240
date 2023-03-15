import math
import numpy as np

class heated_tank:
    def __init__(self, P, T, T_init, T_env, T_in, T_set, Q, F, c, p, V, m, G, Tau):
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
        P_0 = (self.T_set-self.T_in)*(self.m*self.c)/self.G
        print(P_0)
    
    def temperature(self):
        pass


if __name__=="__main__":
    hei = heated_tank(0, 0, 20, 20, 20,25,0.25*10**(-3),0.25, 4200, 1000, 0.2,200,100,60)
    hei.constant_power()
