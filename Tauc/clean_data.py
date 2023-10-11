import pandas as pd

class CleanData:
    """Esta clase es para limpiar los datos que salen del espectrofotometro"""
    
    def __init__(self, path):
        self.path = path

    def read_data(self):
        """Esta funcion lee los datos del espectrofotometro"""

        path = self.path
        # Read the data
        data = pd.read_csv(path, skiprows = 14, sep = "\t")
        data = data.drop(data.index[-1])
        df = data.rename(columns={str(data.columns[0]): "Wavelength", str(data.columns[1]): "Intensity"})
        name = str("clean_data/" + path.split("/")[-1] + ".csv")
        df['Wavelength'] = df['Wavelength'].astype(float)
        df['Intensity'] = df['Intensity'].astype(float)
        df_filtrado = df[df['Wavelength'] <= 875]
        df_filtrado = df[df['Wavelength'] >= 380]
        df_filtrado.to_csv(name, index=False)
        print("The data was cleaned and saved in: ", name)
        return True


    



    def run(self):
        """Esta funcion corre el codigo"""
        self.read_data()
        return True