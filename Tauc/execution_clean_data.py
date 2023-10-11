import clean_data as cd
import os 
if __name__ == "__main__":

    files = os.listdir("Datos")
    sample_files= [i for i in files if i.endswith(".sample")]
    dark_files= [i for i in files if i.endswith(".dark")]
    reference_files= [i for i in files if i.endswith(".reference")]
    scope_files= [i for i in files if i.endswith(".scope")]

    for i in sample_files:
        path = "Datos/" + i
        datos = cd.CleanData(path)
        datos.run()
    
    for i in dark_files:
        path = "Datos/" + i
        datos = cd.CleanData(path)
        datos.run()
    
    for i in reference_files:
        path = "Datos/" + i
        datos = cd.CleanData(path)
        datos.run()
    
    for i in scope_files:
        path = "Datos/" + i
        datos = cd.CleanData(path)
        datos.run()
    


    print("Finished")