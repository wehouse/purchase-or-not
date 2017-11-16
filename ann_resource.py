# -*- coding: utf-8 -*-

import pickle
from keras.models import model_from_json

class AnnResource:
    
    def __init__(self):
        self.labelencoder_X_contact = pickle.load(open('model_binaries/labelencoder_X_contact.p', 'rb'))
        self.labelencoder_X_default = pickle.load(open('model_binaries/labelencoder_X_default.p', 'rb'))
        self.labelencoder_X_education = pickle.load(open('model_binaries/labelencoder_X_education.p', 'rb'))
        self.labelencoder_X_housing = pickle.load(open('model_binaries/labelencoder_X_housing.p', 'rb'))
        self.labelencoder_X_job = pickle.load(open('model_binaries/labelencoder_X_job.p', 'rb'))
        self.labelencoder_X_loan = pickle.load(open('model_binaries/labelencoder_X_loan.p', 'rb'))
        self.labelencoder_X_marital = pickle.load(open('model_binaries/labelencoder_X_marital.p', 'rb'))
        self.labelencoder_X_poutcome = pickle.load(open('model_binaries/labelencoder_X_poutcome.p', 'rb'))

        self.onehotencoder = pickle.load(open('model_binaries/onehotencoder.p', 'rb'))
        
        # load json and create model
        json_file = open('model_binaries/model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        self.loaded_model.load_weights("model_binaries/model.h5")
        print("Loaded model from disk")
        
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }
        resp.media = quote

    def on_post(self, req, resp):      
        json = req.media
        contact=self.labelencoder_X_contact.transform([json.get('contact')])
        default=self.labelencoder_X_default.transform([json.get('default')])
        education=self.labelencoder_X_education.transform([json.get('education')])
        housing= self.labelencoder_X_housing.transform([json.get('housing')])
        job = self.labelencoder_X_job.transform([json.get('job')])
        loan = self.labelencoder_X_loan.transform([json.get('loan')])
        marital = self.labelencoder_X_marital.transform([json.get('marital')])
        poutcome = self.labelencoder_X_poutcome.transform([json.get('poutcome')])
        
        age = json.get('age')
        balance=json.get('balance')
        campaign=json.get('campaign')
        pdays=json.get('pdays')
        previous=json.get('previous')
        data=[]
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
        input=self.onehotencoder.transform([data]).toarray()
        input = input[:, 1:]
        resp.body = str(self.loaded_model.predict(input)[0][0])
