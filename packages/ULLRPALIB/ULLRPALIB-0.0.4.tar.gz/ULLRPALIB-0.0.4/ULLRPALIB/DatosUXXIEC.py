import csv
from openpyxl import load_workbook
import pandas as pd

## https://joserzapata.github.io/courses/python-ciencia-datos/pandas/

CARPETA_DATOS = "z:\\RPA\\PRE\\DATAIN\\ROBI\\"
VERBOSE = False


def carga_pd_DC(anios):
    print("Cargando datos de DC de los años: ", anios)
    pd_DC = pd.read_excel(CARPETA_DATOS + "Docuconta_" + anios[0] + ".xlsx")
    for anio in anios[1:]:
        pd_DC2 = pd.read_excel(CARPETA_DATOS + "Docuconta_" + anio + ".xlsx")
        pd_DC = pd.concat([pd_DC, pd_DC2])
    if VERBOSE:
        print("Cargados {} DC".format(len(pd_DC)))
        print(pd_DC.info())
        print(pd_DC.dtypes)
        pd_DC["Strnumerodocumento"]  = pd_DC["Strnumerodocumento"].astype("object")
        print(pd_DC.info())
        print(pd_DC.dtypes)
    pd_DC = pd_DC.drop_duplicates(["Strnumerodocumento"])
    pd_DC.set_index(["Strnumerodocumento"], inplace=True)
    print("Cargados {} DC".format(len(pd_DC)))
    if VERBOSE:
        print(pd_DC)
        print(pd_DC.info())
        print(pd_DC.dtypes)
        pd_DC.describe()
    return(pd_DC)

def carga_pd_JG(anios):
    global pd_JG

    print("Cargando datos de JG de los años: ", anios)
    pd_JG = pd.read_excel(CARPETA_DATOS + "Datos_" + anios[0] + ".xlsx" )
    for anio in anios[1:]:
        pd_JG2 = pd.read_excel(CARPETA_DATOS + "Datos_" + anio + ".xlsx" )
        pd_JG = pd.concat([pd_JG, pd_JG2])
    print("Cargados {} JG".format(len(pd_JG)))

def carga_pd_sede_docuconta():
    print("Cargando datos de los expedientes de Sede de los DC ")
    pd_sede_docuconta = pd.read_excel(CARPETA_DATOS + "Sede_Docuconta.xlsx")
    if VERBOSE:
        print(pd_sede_docuconta.info())
        print(pd_sede_docuconta.dtypes)
    pd_sede_docuconta = pd_sede_docuconta.drop_duplicates(["Codigo Expediente"])
    pd_sede_docuconta.set_index(["Codigo Expediente"], inplace=True)
    print("Cargados {} expedientes de DC de la sede".format(len(pd_sede_docuconta)))
    if VERBOSE:
        print(pd_sede_docuconta)
        print(pd_sede_docuconta.info())
        print(pd_sede_docuconta.dtypes)
        pd_sede_docuconta.describe()

