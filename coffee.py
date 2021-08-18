import plotly.express as py
import csv
import numpy as np

def getdatasource(datapath):
    coffeeinml=[]
    sleepinhr=[]
    with open(datapath)as f:
        csvreader=csv.DictReader(f)
        for g in csvreader:
            coffeeinml.append(float(g["Coffee in ml"]))
            sleepinhr.append(float(g["sleep in hours"]))
    return {"x":coffeeinml,"y":sleepinhr}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print(correlation)

def setup():
    datapath="2.csv"
    datasource=getdatasource(datapath)
    findcorrelation(datasource)

setup()