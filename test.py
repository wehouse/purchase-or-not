# -*- coding: utf-8 -*-

import numpy as np
import pickle
from keras.models import model_from_json

labelencoder_X_contact = pickle.load(open('labelencoder_X_contact.p', 'rb'))
labelencoder_X_default = pickle.load(open('labelencoder_X_default.p', 'rb'))
labelencoder_X_education = pickle.load(open('labelencoder_X_education.p', 'rb'))
labelencoder_X_housing = pickle.load(open('labelencoder_X_housing.p', 'rb'))
labelencoder_X_job = pickle.load(open('labelencoder_X_job.p', 'rb'))
labelencoder_X_loan = pickle.load(open('labelencoder_X_loan.p', 'rb'))
labelencoder_X_marital = pickle.load(open('labelencoder_X_marital.p', 'rb'))
labelencoder_X_poutcome = pickle.load(open('labelencoder_X_poutcome.p', 'rb'))

onehotencoder = pickle.load(open('onehotencoder.p', 'rb'))

age=58
contact=labelencoder_X_contact.transform(['unknown'])
default=labelencoder_X_default.transform(['no'])
education=labelencoder_X_education.transform(['primary'])
housing= labelencoder_X_housing.transform(['yes'])
job = labelencoder_X_job.transform(['management'])
loan = labelencoder_X_loan.transform(['yes'])
marital = labelencoder_X_marital.transform(['married'])
poutcome = labelencoder_X_poutcome.transform(['unknown'])

# age, job, marital, education, default, balance, housing, loan, contact, campaign, pdays, previous, poutcome

data=[]
balance=2143
campaign=1
pdays=999
previous=0

data.append(age)
data.append(job[0])
data.append(marital[0])
data.append(education[0])
data.append(default[0])
data.append(balance)
data.append(housing[0])
data.append(loan[0])
data.append(contact[0])
data.append(campaign)
data.append(pdays)
data.append(previous)
data.append(poutcome[0])

input=onehotencoder.transform([data]).toarray()
input = input[:, 1:]
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

print(loaded_model.predict(input))