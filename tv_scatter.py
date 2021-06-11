import plotly.express as px
import csv
import numpy as np
def getDataSource(data_path):
   tv_size=[]
   watchtime_data=[]
   with open(data_path)as csv_file:
      csv_reader=csv.DictReader(csv_file)
      for row in csv_reader:
         tv_size.append(float(row["Size of TV"]))
         watchtime_data.append(float(row["Average watchtime"]))
   return{"x":tv_size,"y":watchtime_data}
def findCorrelation(dataSource):
   correlation=np.corrcoef(dataSource["x"],dataSource["y"])
   print("Correlation is ->",correlation[0,1])
def setup():
   data_path="tv_watchtime.csv"
   dataSource=getDataSource(data_path)
   findCorrelation(dataSource)
setup()