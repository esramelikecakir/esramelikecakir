import pandas as pd
import numpy as np
from pylab import *
import openpyxl


rsi_db = pd.read_excel("/Users/esra/Library/Containers/com.microsoft.Excel/Data/Downloads/rsidosyasi.xlsx")
x =rsi_db["close"]

class rsi_counter():

    def __int__(self,day_starter,total_gain,total_loss,rsi,program):
        self.total_gain = total_gain
        self.total_loss = total_loss
        self.rsi = rsi
        self.day_starter = day_starter
        self.program = True

    def day_starter_put(self,day_starter):
        day_starter = 0

    def calculator(self,day_starter,total_loss,total_gain):

        for i in range(day_starter, day_starter +14):
            total_loss=0
            total_gain = 0
            if x[i + 1] > x[i]:
                gain = x[i + 1] - x[i]
                total_gain = + gain


            elif x[i] > x[i + 1]:
                loss = x[i] - x[i + 1]
                total_loss =  + loss

    def rsi_function(self,total_loss,total_gain,rsi):
        avg_loss = total_loss / 14
        avg_gain = total_gain / 14
        rs = avg_gain/avg_loss
        rsi = 100 - 100*(1+rs)


    def show(self,rsi):
        print(rsi)

deneme = rsi_counter()
while deneme.program():
    deneme.show()
