import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt


#df = pd.read_csv("./csv/titanic.csv")
df = pd.read_csv("titanic.csv")
df.head(100)
df.info()
age = df.loc[0:,['age']] #Define somente a coluna age das linhas 1 até o n-1
#print(age)
survived = df.loc[0:,['survived']] #Define somente a coluna age das linhas 1 até o n-1
#print(survived)
#age.dtypes #Exibe o tipo de dados 
#age = age.astype(float) #Altera o tipo de dados 
#age.dtypes #Exibe o tipo de dados 
#df.columns #Exibe as colunas do dataset
#df.values # Exibe os valores do dataset
#df.loc[24] #Exibe o conteúdo de uma determinada linha
#df.loc[[24,28]] #Exibe o conteúdo de uma determinada linha
#df.loc[24:28] #Exibe o conteúdo de uma determinada linha
#df.query('sex == "male" and survived == 0')
#plt.plot(age,survived)
#plt.bar(age,survived)
#plt.stem(age,survived)
#plt.scatter(age,survived)
#plt.step(age,survived)
#plt.hist(survived)
plt.hist(age)
plt.show()


