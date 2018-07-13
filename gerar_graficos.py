import pandas as pd
import matplotlib.pyplot as pyplot
import matplotlib.pyplot as plt 
import numpy as np

planilha = pd.read_csv('planilnaTeste.csv')

contTag = pd.value_counts(planilha['Tag'])
nPlanilha = pd.DataFrame(contTag)
indextag=[]
for index1, row in nPlanilha.iterrows():
    indextag.append(index1)
    
pyplot.pie(contTag, labels=indextag, autopct='%1.1f%%')
pyplot.title('Porcetagem TAGs')
pyplot.savefig('plot.png')
pyplot.show()

contUF= pd.value_counts(planilha['Estado'])
nPlanilha1 = pd.DataFrame(contUF)

index=[]
for index1, row in nPlanilha1.iterrows():
    index.append(index1)

pyplot.pie(contUF, labels=index, autopct='%1.1f%%')
pyplot.title('Estados conhecidos')
pyplot.savefig('plot2.png')
pyplot.show()

contTag = pd.value_counts(planilha['Tag'])
nPlanilha = pd.DataFrame(contTag)

indextag=[]
for index, row in nPlanilha.iterrows():
    indextag.append(index)

valores=[]
for valor in contTag:
    valores.append(valor)

qtdbarras = np.arange(len(indextag))
                
plt.barh(qtdbarras, valores, align='center', color='blue')
plt.yticks(qtdbarras, indextag)   
plt.ylabel('Tag')
plt.xlabel('Quatidade')
plt.title('TAG')
plt.savefig('plot3.png')
plt.show()
                
contUF= pd.value_counts(planilha['Estado'])
nPlanilha1 = pd.DataFrame(contUF)

indexuf=[]
for index1, row in nPlanilha1.iterrows():
    indexuf.append(index1)

valores=[]
for ind in contUF:
    valores.append(ind)

qtdbarras = np.arange(len(indexuf))

plt.barh(qtdbarras, valores, align='center', color='blue')
plt.yticks(qtdbarras, indexuf)   
plt.ylabel('Estados')
plt.xlabel('Quatidade')
plt.title('QDT por UF')
plt.savefig('plot4.png')
plt.show()
