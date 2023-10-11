import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class band_gap:

    def __init__(self,dark,reference,sample,name):
        self.dark = dark
        self.reference = reference
        self.sample = sample
        self.name = name
    
    def plot(self):
        """Esta funcion lee los datos del espectrofotometro"""

        dfnum = (self.sample['Intensity'] - self.dark['Intensity'])*100/(self.reference['Intensity'] - self.dark['Intensity'])
        plt.title(self.name)
        plt.plot(self.sample['Wavelength'],dfnum, label = self.name)
        plt.legend()
        plt.savefig("band_gap" + self.name + ".png")
        return True


        