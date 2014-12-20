#Cellule d'importation des modules nécessaires à l'exécution du Notebook

import numpy as np
import pandas as pd
import sklearn as sk
from sklearn import linear_model
import urllib
import sys

#Récupération du fichier de données sur le git du projet
response = urllib.request.urlopen("https://github.com/NaasCraft/projetPython2014/raw/master/clean2.data")

data = response.read() #on obtient un fichier au format "binary literal"
data = data.decode('utf-8').splitlines() #d'où la nécessité d'utiliser la méthode .decode('utf-8')

#On procède au formatage des données en DataFrame du module pandas

data2 = []
provN = ''
indexI, indexJ = 0, 1
indexTuples = []

for l in data:
    l2 = l.split(',')
    
    molNum = l2[1].split('_')[0]
    
    #séquence de simplification des identificateurs pour les molécules
    if provN != molNum:
        indexJ = 1
        indexI += 1
    else:
        indexJ += 1
    
    provN = molNum
    indexTuples += [(indexI, indexJ)]
    newLine = [indexI, indexJ] + [l2[1]] + [int(x) for x in l2[2:-1]] + [float(l2[len(l2)-1])]
    data2.append(newLine)
    
colNames = ['indexI', 'indexJ', 'molID'] + ['f'+str(k) for k in range(1,167)] + ['class']
multiIndex = pd.MultiIndex.from_tuples(indexTuples, names=['indexI','indexJ'])
dfMusk = pd.DataFrame(data2, columns=colNames, index=multiIndex)
#on utilise trois variables comme index pour pouvoir différencier les "paquets" du problème de MIL

##Nous allons diviser la base en une base test et une base train
import random 
random_list = random.sample(range(1,103), 102) 
## On veut entre 4500 et 5500 observations car les molécules n'ont pas toutes le même nombre de conformères
num=0
while not ((4500<num) and (5500>num)):
    bag_train=random_list[0:82]
    bag_test=random_list[83:102]

    bag_train=sorted(bag_train)
    bag_test=sorted(bag_test)

    dfMusk_train=dfMusk[dfMusk["indexI"].isin(bag_train)]
    dfMusk_test=dfMusk[dfMusk["indexI"].isin(bag_test)]
    
    num=dfMusk_train.shape[0]

print("The training set has "+str(num)+" observations.")

#Multiple Instance Regression algorithm
#Source : Ray, Soumya; Page, David (2001). "Multiple instance regression", fig. 2

def MIRalg(R, df, list_Bag, dim, lossF):
    globalErr = sys.maxsize
    count = 0
    clf=linear_model.LinearRegression()
    for r in range(R):
        b0 = np.random.randn(1, dim-1)
        bestErr = sys.maxsize
        currentErr = 0
        done = False
        
        while (not done):
            bestConfs = pd.DataFrame(columns=['f'+str(k) for k in range(1,dim)]+['class'])
            
            for i in list_Bag:
                minLoss = sys.maxsize
                nInst = df.ix[i].shape[0]
                
                for j in range(1,nInst+1):
                    tempErr = lossF(df.ix[(i,j)].values.tolist()[3:],b0,count)
                    
                    if (tempErr < minLoss):
                        minLoss = tempErr
                        selectedJ = j
                        
                currentErr += minLoss
                bestConfs.loc[i] = df.ix[(i,selectedJ)].values.tolist()[3:]
                
            if currentErr >= bestErr:
                done = True
                
            else:
                bestErr = currentErr
                b1 = b0
                last_clf=clf
                
                #on procède à la régression multiple sur les "bestConfs"
                clf = linear_model.LinearRegression()
                clf.fit(bestConfs[['f'+str(k) for k in range(1,dim)]].values,bestConfs['class'].values)
                b0 = clf.coef_
                    
        if bestErr < globalErr:
            globalErr = bestErr
            b2 = b1
    
    return b2, last_clf

def leastSquaresLoss(l,b,count):
    y = l[-1]
    X = np.array(l[:-1])
    
    return (y - X.dot(b.T))**2

b, clf = MIRalg(10, dfMusk_train, bag_train, 167, leastSquaresLoss)

##Number of good predictions on the test data set:

## We are going to use the 0-1 loss function here:
dfMusk_test["Prediction"]=clf.predict(dfMusk_test[['f'+str(k) for k in range(1,167)]].values)

#here we need to change dfMusk_test["Prediction"]

print("We have "+str(number_good_pred)+" good predictions of the "+str(dfMusk_test.shape[0])+" observation of the test data set.")
print(dfMusk_test["Prediction"])

##standard output printing

# The coefficients
print('Coefficients: \n', clf.coef_)

# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((clf.predict(dfMusk_train[['f'+str(k) for k in range(1,167)]].values) - dfMusk_train['class'].values) ** 2))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % clf.score(dfMusk_train[['f'+str(k) for k in range(1,167)]].values, dfMusk_train['class'].values))
