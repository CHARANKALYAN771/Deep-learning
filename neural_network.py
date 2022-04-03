import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from tensorflow.keras.layers import Dense 
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
data = load_iris()
features = data['data']
target = data['target']
targets_ = to_categorical(target, num_classes=3)
features.shape[1]
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features, targets_)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train)
model = Sequential()

model.add(Dense(100, input_shape=(features.shape[1],)))
model.add(Dense(30, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(23, activation="relu"))
model.add(Dense(3, activation="softmax"))
import tensorflow

model.compile(optimizer="sgd", 
              loss=tensorflow.keras.losses.CategoricalCrossentropy(), 
              metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))
X_train.shape
y_train.shape
y_pred = model.predict_classes(X_test)
y_pred
from sklearn.metrics import accuracy_score

y_test_ = []

for i in y_test:
    
    y_test_.append(np.argmax(i))
accuracy_score(y_test_, y_pred)

model.save("NN.h5")

from tensorflow.keras.models import load_model

model = load_model("./NN.h5")
clas = model.predict([[.2, 0.4, 0.5, 0.3]])
clas
np.argmax(clas)
classes = ['class1', 'class2', 'class3']

classes[np.argmax(clas)]

