from keras.datasets import imdb

import warnings
warnings.filterwarnings("ignore")

vocabulary_size = 5000
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words = vocabulary_size)
print('Loaded dataset with {} training samples, {} test samples'.format(len(X_train), len(X_test)))

print('---review---')
print(X_train[6])
print('---label---')
print(y_train[6])
print(set(y_train))

word2id = imdb.get_word_index()
id2word = {i: word for word, i in word2id.items()}
print('---review with words---')
print([id2word.get(i, ' ') for i in X_train[6]])
print('---label---')
print(y_train[6])

print('tHE MOVIE WAS VERY GOOD, IT IS A FAMILY DRAMA, EVERY ONE CAN WATCH IT'.split(' '))
print('GOOD MOVIE, BUT NOT FOR EVERYONE'.split(" "))
print('YEAH IT IS GOOD'.split(" "))

print('Maximum review length: {}'.format(
len(max((X_train + X_test), key=len))))

print('Minimum review length: {}'.format(
len(min((X_test + X_test), key=len))))

from keras.preprocessing import sequence
max_words = 500
X_train = sequence.pad_sequences(X_train, maxlen=max_words)
X_test = sequence.pad_sequences(X_test, maxlen=max_words)

from keras import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout
embedding_size=32
model=Sequential()
model.add(Embedding(vocabulary_size, embedding_size, input_length=max_words))
model.add(LSTM(100))
model.add(Dense(1, activation='sigmoid'))
print(model.summary())

model.compile(loss='binary_crossentropy', 
             optimizer='adam', 
             metrics=['accuracy'])

batch_size = 64
num_epochs = 1
X_valid, y_valid = X_train[:batch_size], y_train[:batch_size]
X_train2, y_train2 = X_train[batch_size:], y_train[batch_size:]
model.fit(X_train2, y_train2, validation_data=(X_valid, y_valid), batch_size=batch_size, epochs=num_epochs)

x[:500], x[500:]

scores = model.evaluate(X_test, y_test, verbose=1)
print('Test accuracy:', scores[1])










