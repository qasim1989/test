from statistics import mean
from sklearn import preprocessing
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import csv 
class preprrossing:
    filepath = 'F:\python\\qasim.csv'
    #------ ------------method to read the csv file --------------------- 
    def read_csv_data(self):
        with open(self.filepath, newline='') as csvfile:
                mydata = csv.reader(csvfile, delimiter=' ', quotechar='|')
                array = list(mydata)
        for row in array:
             print(', '.join(row))
    # Normalization min_max_scaler method
    def min_max_scaler (self) :
        with open(self.filepath, newline='') as csvreader:
                csvfile = csv.reader(csvreader, delimiter=' ', quotechar='|')
                array = np.loadtxt(csvreader, delimiter=",")
        min_max = preprocessing.MinMaxScaler()
        csvflot = str(csvfile)
        # col = csvfile.columns
        result = min_max.fit_transform(array)
        print(result)
    #  Normalization z-score method 
    def z_score(self)  :
        with open(self.filepath, newline='') as csvreader:
            csvfile = csv.reader(csvreader, delimiter=' ', quotechar='|')
            array = np.loadtxt(csvreader, delimiter=",")
        zscores = stats.zscore(array)
        print(zscores) 
    #z_score_outlier method1
    def z_score1_outlier(self):
        with open(self.filepath, newline='') as csvreader:
                csvfile = csv.reader(csvreader, delimiter=' ', quotechar='|')
                array = np.loadtxt(csvreader, delimiter=",")
                a=array
                matrix=np.array(a)
                max=np.max(matrix)
                x=[]
                for row in matrix:
                    for col in row:
                        col=col/max
                        x.append(col)
                y=np.reshape(x,(len(a),len(a[0])))
                z=np.max(y)
                std=np.std(y)
                row=len(y)
                colom=len(y[0])
                countt=row*colom
                total=sum(map(sum,y))
                mean=total/countt
                for rows in y:
                    for cols in rows:
                        if ((cols > (std+mean)) | (cols<std-mean)):
                            print(cols,end=",")        

    #z_score_outlier method2
    def z_score_outlier(self):
        with open(self.filepath, newline='') as csvreader:
                csvfile = csv.reader(csvreader, delimiter=' ', quotechar='|')
                array = np.loadtxt(csvreader, delimiter=",")
                a=array
                row=len(a)
                col=len(a[0])
                countt= row*col
                total=sum(map (sum,a))
                mean =total/countt
                ss=np.std(a)
                x=1
                for row in a:
                    for co in row:
                        co=(co-mean)/ss
                        if(np.abs(co) > x):
                            print(co,end=",")
   
object  = preprrossing()
print("read")
object .read_csv_data()
print("maxmin")
object .min_max_scaler()
print("zsc")
object .z_score()
print("outlier z scor")
object .z_score_outlier()
print("out lier z scor 2 is:")
object .z_score1_outlier()