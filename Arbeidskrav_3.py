import math
import numpy as np

class heated_tank:
    def __init__(self, P, T, T_init, T_env, T_in, T_set, Q, F, c, p, V, m, G, Tau):
        self.P = P        
        self.T = T
        self.T_init = T_init
        self.T_env = T_env
        self.T_in = T_in
        self.T_set = T_set
        self.Q = Q
        self.F = F
        self.c = c
        self.p = p
        self.V = V
        self.m = m
        self.G = G
        self.Tau = Tau

    def constant_power(self):
        pass