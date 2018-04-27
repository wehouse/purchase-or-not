[![Docker Repository on Quay](https://quay.io/repository/wehouse/purchase-or-not/status "Docker Repository on Quay")](https://quay.io/repository/wehouse/purchase-or-not)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Heroku](http://heroku-badge.herokuapp.com/?app=purchase-or-not&root=ann&style=flat&svg=1)](https://purchase-or-not.herokuapp.com/ann)

# Purchase Or Not

## Introduction
By using a well known public data set[1] which contains 45211 observations of a Porteguese bank's telemarketing efforts, 
outcome and demographic information about target audience.

## Dataset
We are using Moro, Cortez and Rita's banking data [1] pertaining to a marketing campaignA. The data is related with direct
marketing campaigns (phone calls) of a Portuguese banking institution. The classification goal is to predict
if the client will subscribe a term deposit (variable y).

## Data Pre-processing
Dataset contributed by Moro, Cortez and Rita [1] is quite high quality, only preprocessing we had to do was to change 
pdays (days since last marketing attempt) from -1 to 999 as documentation suggested [2]. 

## Models
In order to analyze any dataset, we first need to have a model of explanation in mind. Each model has its strengths and
weaknesses which must be carefully evaluated.

In order of implementation, we used the following models:
1. 3 Hidden layer ANN with RELU for hidden layers and sigmoid as output layer with batch size 5

## Results
In order to compare results of multiple models, we will be using the confusion matrix and tensorflow model training accuracy
comparison to evaluate test vs pred accuracy. We will introduce other techniques of comparison.

### 3 Hidden Layer ANN
Model Accurasy is 0.8937 after 10 epochs
Confusion matrix yielded

|   	| 0  	| 1  	|
|---	|---	|---	|
| 0  	| 7890  	| 91  	|
| 1  	| 896  	| 166  	|

9043 total samples
8056 Correct
987 Incorrect

Which is about 0.8908 which is very close to training accuracy indicating that overfitting is not happening with this
model.

## How to deploy and run?
### From Code
Install requirements from requirements.txt via 
```
pip install -r requirements.txt
```
Afterwards
```
gunicorn app:api
```
Port 8000 u will have it launched that will only address 127.0.0.1 requests and can be accessed using the postman collection in repo.

### From Docker
Docker image is provided via Quay, its launch instructions are here:
[Container Registry](https://quay.io/repository/wehouse/purchase-or-not)

postman collection in repo again will be the primary way to use it.

## References
1. (Moro et al., 2014) S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014
2. https://archive.ics.uci.edu/ml/datasets/bank+marketing