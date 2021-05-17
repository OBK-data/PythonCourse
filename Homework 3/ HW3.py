import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import sklearn
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
import sklearn.model_selection as ms
import sklearn.metrics as met
import sklearn.feature_selection as fs
from sklearn.datasets import make_classification
from imblearn.over_sampling import RandomOverSampler
from sklearn import preprocessing

#[Preparing data for ML]
dat = pd.read_csv('C:/Users/Bulut/Desktop/R Course/aa/Homework 2/Homework 3/cses4_cut.csv')
#there are many NaN values that are not assigned. So I assigned them.
col1=["D2011","D2016","D2027","D2029","D2030"]
col2 = ["D2002","D2004","D2005","D2006","D2007","D2008","D2009","D2012","D2013","D2014","D2017","D2018","D2019","D2020","D2024","D2025","D2031"]
col3 = ["D2003","D2010","D2015","D2021","D2022","D2023","D2026","D2028"]
#cleaning up data
dat[col1]=dat[col1].replace(dict.fromkeys([999,998,997,996,995], np.nan))
dat[col2]=dat[col2].replace({9:np.nan})
dat[col3]=dat[col3].replace(dict.fromkeys([99,98,97], np.nan))
#onehotencode

catvar = ["D2002","D2004","D2010","D2011","D2012","D2013","D2014","D2015","D2016","D2017","D2018","D2019","D2026","D2027","D2028","D2029","D2030","D2031"]
sklearn.preprocessing.OneHotEncoder(categories='catvar')

#boolean to integer for prediction
dat["voted"] = dat["voted"].astype(int)
#fill up NaNs
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
dat = imp.fit_transform(dat)
np.set_printoptions(suppress=True) #surpresses scientific notations
#data preparation
data = dat[:,1:]#remove first column
y_data = data[:,-1].reshape(-1,1).ravel()#dependent feature
x_data0 = data[:,:-1] #independent feature
x_data =  preprocessing.normalize(x_data0) #normalization for ease of calculation

#checking the distribution of ouput first
unique, counts = np.unique(y_data, return_counts=True)
print(dict(zip(unique, counts))) #0s are overweighted by 1s with a ratio of 0.217. Therefore, models might not be able to predict 0s as much as 1s..

#general train test splits
Xtrain, Xtest, ytrain, ytest = ms.train_test_split(x_data, y_data,
random_state=1)
#feature selection to reduce unnecessary variables
selector = fs.SelectKBest(fs.f_classif, k=5)
selector.fit(Xtrain, ytrain)

#Support Vector Machine training w/o weight

from sklearn import svm
model = svm.SVC()
model.fit(Xtrain, ytrain)
y_model = model.predict(Xtest)
cv = ms.RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
# evaluate model
print("SVM normal Accuracy Score", met.accuracy_score(ytest, y_model)) #accuracy
cross_val = ms.cross_val_score(model, Xtrain, ytrain, scoring='roc_auc', cv=cv, n_jobs=-1) #cross val
print("SVM normal Cross Validation Score", np.mean(cross_val))

#confusion matrix
mat = met.confusion_matrix(ytest, y_model)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true SVM(normal)')
plt.ylabel('predicted SVM(normal)')
plt.show()

#SVM with "weights"

from sklearn import svm
weights = {0:4.60, 1:1.0} # 0.207 chosen to invert weights to equalize
model2 = svm.SVC(gamma='scale', class_weight=weights)
model2.fit(Xtrain, ytrain)
y_model2 = model2.predict(Xtest)
cv = ms.RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
# evaluate model
cross_val1 = ms.cross_val_score(model2, Xtrain, ytrain, scoring='roc_auc', cv=cv, n_jobs=-1)
print("Weighted SVM Cross Validation Score", np.mean(cross_val1))
print("Weighted SVM Accuracy Score",met.accuracy_score(ytest, y_model2))

#another confusion matrix
mata = met.confusion_matrix(ytest, y_model2)
sns.heatmap(mata.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true (SVM weight)')
plt.ylabel('predicted (SVM weight)')
plt.show()

#logistic regression training

#logistic prediction
model3 = LogisticRegression(max_iter = 2000) #more than 1000 to ensure that it iterates all of the options
model3.fit(Xtrain, ytrain)
y_model3 = model3.predict(Xtest)
print("Logistic Accuracy Score", met.accuracy_score(ytest, y_model3))#accuracy
#cross validation score
cross_val3 = ms.cross_val_score(model3, Xtrain, ytrain, scoring='roc_auc', cv=cv, n_jobs=-1)
print(" Logistic Cross Validation Score", np.mean(cross_val3))
#logistic confusion matrix
matb = met.confusion_matrix(ytest, y_model3)
sns.heatmap(matb.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('Log true')
plt.ylabel('Log predicted')
plt.show()

#LogisticRegression (weights)
model5 = LogisticRegression(max_iter = 2000, class_weight=weights) #more than 1000 to ensure that it iterates all of the options
model5.fit(Xtrain, ytrain)
y_model5 = model3.predict(Xtest)
print("Logistic (W) Accuracy Score", met.accuracy_score(ytest, y_model3))#accuracy
#cross validation score
cross_val3 = ms.cross_val_score(model3, Xtrain, ytrain, scoring='roc_auc', cv=cv, n_jobs=-1)
print(" Logistic (W) Cross Validation Score", np.mean(cross_val3))
#logistic confusion matrix
matz = met.confusion_matrix(ytest, y_model3)
sns.heatmap(matz.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('Log (w) true')
plt.ylabel('Log (w) predicted')
plt.show()

#random forest

#I will try to oversample the 0s for a better result (Without it random forest had a problem with predicting 0s (0 precision around 0.30))
oversample = RandomOverSampler(sampling_strategy=0.5)
x_data2, y_data2 = oversample.fit_resample(x_data, y_data)
Xtrain2, Xtest2, ytrain2, ytest2 = ms.train_test_split(x_data2, y_data2,
random_state=1)

#main predict
from sklearn.ensemble import RandomForestClassifier

model4 = RandomForestClassifier(n_estimators=100)
model4.fit(Xtrain2, ytrain2)
pred = model4.predict(Xtest2)

#classification report
from sklearn import metrics
print(metrics.classification_report(pred, ytest2))

#confusion matrix
matf= met.confusion_matrix(ytest2, pred)
sns.heatmap(matf.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true (forest)')
plt.ylabel('predicted (forest)')
plt.show()
#cross validation
cross_val3 = ms.cross_val_score(model3, Xtrain2, ytrain2, scoring='roc_auc', cv=cv, n_jobs=-1)
print("Forest Cross Validation Score", np.mean(cross_val3))

print("Forest Accuracy Score", met.accuracy_score(ytest2, pred))

#whole model took around 2 minutes to run because of the sample size.
