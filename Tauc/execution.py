from tauc import band_gap
import pandas as pd
if __name__ == "__main__":
    df_perovskitaD = pd.read_csv('clean_data/Perovskita.Master.dark.csv')
    df_perovskitaR = pd.read_csv('clean_data/Perovskita.Master.reference.csv')
    df_perovskitaS = pd.read_csv('clean_data/Perovskita.Master.sample.csv') 
    perovskita = band_gap(df_perovskitaD,df_perovskitaR,df_perovskitaS,"Perovskita")
    perovskita.plot()
    print("Perovskita")

    df_tio2D = pd.read_csv('clean_data/TiO2.Master.dark.csv')
    df_tio2R = pd.read_csv('clean_data/TiO2.Master.reference.csv')
    df_tio2S = pd.read_csv('clean_data/TiO2.Master.sample.csv')
    tio2 = band_gap(df_tio2D,df_tio2R,df_tio2S,"TiO2")
    tio2.plot()
    print("TiO2")

    df_znoD = pd.read_csv('clean_data/ZnO.Master.dark.csv')
    df_znoR = pd.read_csv('clean_data/ZnO.Master.reference.csv')
    df_znoS = pd.read_csv('clean_data/ZnO.Master.sample.csv')
    zno = band_gap(df_znoD,df_znoR,df_znoS,"ZnO")
    zno.plot()
    print("ZnO")