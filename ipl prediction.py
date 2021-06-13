Supervised learning

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("CSK vs MI.csv")
data.head()

sns.lmplot('Score','Balls',data=data,hue='Winner',palette='Set1',fit_reg=False,scatter_kws={'s':70})

scb=data[["Score",'Balls']]
label=np.where(data['Winner']=='Mumbai Indians',0,1)

from sklearn import svm

model=svm.SVC(kernel='linear')

model.fit(scb,label) #hyperplane #margin


#Get the separating hyperplane
w=model.coef_[0]
a=-w[0] / w[1]
xx=np.linspace(100,160)
yy=a*xx-(model.intercept_[0]) / w[1]

sns.lmplot('Score','Balls',data=data,hue='Winner',palette='Set1',fit_reg=False,scatter_kws={'s':70})
plt.plot(xx,yy,linewidth=2,color='black')

# Plot the parallels to the separating hyperplane that pass through the support vectors
b = model.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = model.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

sns.lmplot('Score','Balls',data=data,hue='Winner',palette='Set1',fit_reg=False,scatter_kws={'s':70})
plt.plot(xx,yy,linewidth=2,color='black')
plt.plot(xx,yy_down,'k--')
plt.plot(xx,yy_up,'k--')

def cskvsmi(score,balls):
    if model.predict([[score,balls]])==0:
        print("For this Situation MI will win the Match")
    else:
        print("For this Situation CSK will win the Match")
        
        
cskvsmi(150,120)

sns.lmplot('Score','Balls',data=data,hue='Winner',palette='Set1',fit_reg=False,scatter_kws={'s':70})
plt.plot(xx,yy,linewidth=2,color='black')
plt.plot(150,120,'yo')
