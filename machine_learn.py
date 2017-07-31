import numpy as np
import pandas as pd
from sklearn import preprocessing
import math
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('USDT_BTC.csv')
df.fillna(-99999, inplace=True)
df.dropna(inplace=True)
X = np.array(df)
print(X)
X = np.delete(X,[16], axis=1)
#np.savetxt("foo.csv", X, delimiter=",")
y = np.array(df['target'])
X = preprocessing.scale(X)




mlp = MLPClassifier(solver='adam', alpha=0.001, hidden_layer_sizes=(8,), random_state=1,
                          learning_rate='constant', learning_rate_init=0.01, max_iter=300,
                           activation='logistic', momentum=0.9, verbose=True, tol=0.0001)

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.1, random_state=1)
mlp.fit(X_treino, y_treino)
saidas = mlp.predict(X_teste)

print('-----------------------------------------------------------')


print('Saida da rede:')
print(saidas)
print('Saida desejada:')
print(y_teste)

print('-----------------------------------------------------------')
print('Score: ', (saidas == y_teste).sum() / len(X_teste))
print('Score: ', mlp.score(X_teste, y_teste))