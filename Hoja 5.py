#Juan Diego Solorzano 18151
#Hoja de Trabajo 5


import simpy
import random


class process(object):

    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        while True:
        
