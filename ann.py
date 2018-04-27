# -*- coding: utf-8 -*-

# Part 1 - Data Preprocessing

# Importing the libraries
import pandas as pd
import pickle

# Importing the dataset
dataset = pd.read_csv('data/bank-full.csv', delimiter=";")
dataset.loc[dataset['pdays'] == -1, 'pdays'] = 999

X = dataset.iloc[:, list(range(0,9))+list(range(12,16))].values
y = dataset.iloc[:, 16].values
# age, job, marital, education, default, balance, housing, loan, contact, campaign, pdays, previous, poutcome

# Encoding categorical data
# Columns are 1,2,3,4,6,7,8,12,13
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_job = LabelEncoder()
X[:, 1] = labelencoder_X_job.fit_transform(X[:, 1])
labelencoder_X_marital = LabelEncoder()
X[:, 2] = labelencoder_X_marital.fit_transform(X[:, 2])
labelencoder_X_education = LabelEncoder()
X[:, 3] = labelencoder_X_education.fit_transform(X[:, 3])
labelencoder_X_default = LabelEncoder()
X[:, 4] = labelencoder_X_default.fit_transform(X[:, 4])
labelencoder_X_housing = LabelEncoder()
X[:, 6] = labelencoder_X_housing.fit_transform(X[:, 6])
labelencoder_X_loan = LabelEncoder()
X[:, 7] = labelencoder_X_loan.fit_transform(X[:, 7])
labelencoder_X_contact = LabelEncoder()
X[:, 8] = labelencoder_X_contact.fit_transform(X[:, 8])
labelencoder_X_poutcome = LabelEncoder()
X[:, 12] = labelencoder_X_poutcome.fit_transform(X[:, 12])
onehotencoder = OneHotEncoder(categorical_features = [1,2,3,4,6,7,8,12])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = None)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim = 19, init = 'uniform', activation = 'relu', input_dim = 36))

# Adding the second hidden layer
classifier.add(Dense(output_dim = 19, init = 'uniform', activation = 'relu'))

# Adding the third hidden layer
classifier.add(Dense(output_dim = 9, init = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 10)

# Part 3 - Making the predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#Metrics to look for
from sklearn.metrics import roc_auc_score, precision_score, recall_score
print(cm)
print(roc_auc_score(y_test, y_pred))
print(precision_score(y_test,y_pred))
print(recall_score(y_test, y_pred))

# serialize model to JSON
model_json = classifier.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
classifier.save_weights("model.h5")
print("Saved model to disk")

# Pickle encoders
pickle.dump(labelencoder_X_job,open( "labelencoder_X_job.p", "wb" ) )
pickle.dump(labelencoder_X_marital,open( "labelencoder_X_marital.p", "wb" ) )
pickle.dump(labelencoder_X_education,open( "labelencoder_X_education.p", "wb" ) )
pickle.dump(labelencoder_X_default,open( "labelencoder_X_default.p", "wb" ) )
pickle.dump(labelencoder_X_housing,open( "labelencoder_X_housing.p", "wb" ) )
pickle.dump(labelencoder_X_loan,open( "labelencoder_X_loan.p", "wb" ) )
pickle.dump(labelencoder_X_contact,open( "labelencoder_X_contact.p", "wb" ) )
pickle.dump(labelencoder_X_poutcome,open( "labelencoder_X_poutcome.p", "wb" ) )
pickle.dump(onehotencoder,open( "onehotencoder.p", "wb" ) )