
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

"""
создает и обучает модель машинного обучения на построенных данных из папки «train».
"""

df_train = pd.read_csv('./train/result_train.csv')


X_train = df_train.drop('target', axis=1)
y_train = df_train['target']

model = LinearRegression()
print("--- Model created")

model.fit(X_train, y_train)
print("--- Model trained")

pickle.dump(model, open('model.pkl', 'wb'))