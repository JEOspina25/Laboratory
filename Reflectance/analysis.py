import matplotlib.pyplot as plt
import pandas as pd

class reflectance:

    def __init__(self, path):
        self.path = path
        self.df = pd.read_csv(path)

    def plot(self):
        
        name = str("plots/" + self.path.split("/")[-1] + ".png")
        plt.figure(figsize=(10, 5))
        plt.plot(self.df['Wavelength'], self.df['Intensity'])
        plt.xlabel('Wavelength [nm]]')
        plt.ylabel('Intensity')
        plt.savefig(name)
        return True