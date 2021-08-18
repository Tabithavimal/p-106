import plotly.express as py
import csv
import numpy as np

def getdatasource(datapath):
    marksinpercentage=[]
    dayspresent=[]
    with open(datapath)as f:
        csvreader=csv.DictReader(f)
        for g in csvreader:
            marksinpercentage.append(float(g["Marks In Percentage"]))
            dayspresent.append(float(g["Days Present"]))
    return {"x":marksinpercentage,"y":dayspresent}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print(correlation)

def setup():
    datapath="1.csv"
    datasource=getdatasource(datapath)
    findcorrelation(datasource)

setup()