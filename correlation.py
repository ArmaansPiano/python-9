import plotly.express as px
import csv
import numpy as np
def getDataSource(data_path):
   temperature_data=[]
   ice_cream_sales=[]
   with open(data_path)as csv_file:
      csv_reader=csv.DictReader(csv_file)
      for row in csv_reader:
         temperature_data.append(float(row["Temperature"]))
         ice_cream_sales.append(float(row["Ice-cream Sales( â‚¹ )"]))
   return{"x":temperature_data,"y":ice_cream_sales}
def findCorrelation(dataSource):
   correlation=np.corrcoef(dataSource["x"],dataSource["y"])
   print("Correlation is ->",correlation[0,1])
def setup():
   data_path="temp_data.csv"
   dataSource=getDataSource(data_path)
   findCorrelation(dataSource)
setup()