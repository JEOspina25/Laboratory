import analysis
import os

paths = os.listdir("clean_data")
if __name__ == "__main__":
    for path in paths:
        main = analysis.reflectance("clean_data/" + path)
        main.plot()
        print("The plot was saved in: plots/" + path + ".png") 

