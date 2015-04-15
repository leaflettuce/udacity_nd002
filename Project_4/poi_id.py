#!/usr/bin/python

import sys
import pickle
import numpy
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import test_classifier, dump_classifier_and_data
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from pprint import pprint
from sklearn.metrics import *

################################
# feature selection
################################
features_list = ['poi','salary', 'bonus', 'exercised_stock_options', 'to_poi_percentage',
                 'long_term_incentive', 'expenses', 'director_fees', 'total_payments']

### Load the dictionary containing the dataset
data_dict = pickle.load(open("final_project_dataset.pkl", "r") )
#n of data points
print len(data_dict)


### Store to my_dataset for easy export below.
data_dict.pop('TOTAL',0)  #first outlier..  invalid spreadsheet input
my_dataset = data_dict

################################
# New Feature
################################
#create new feature based on
#percentage of total emails that
#are sent to poi's


#reset NaN's to 0
for i in data_dict:
    if data_dict[i]['from_messages'] == 'NaN':
        data_dict[i]['from_messages'] = 0
    if data_dict[i]['from_this_person_to_poi'] == 'NaN':
        data_dict[i]['from_this_person_to_poi'] = 0
#if total messages no available.. set new feature to 0 as well
    if data_dict[i]['from_messages'] == 0:
        data_dict[i]['to_poi_percentage'] = 0
    else: #the math!
        data_dict[i]['to_poi_percentage'] = float(data_dict[i]['from_this_person_to_poi']) / float(data_dict[i]['from_messages'])
        data_dict[i]['to_poi_percentage'] = float("{0:.2f}".format(data_dict[i]['to_poi_percentage']))

 #print out to check
#for i in data_dict:
#    pprint(data_dict[i])

################################
### Extract features and labels from dataset for local testing
################################
data = featureFormat(my_dataset, features_list, sort_keys = True)

labels, features = targetFeatureSplit(data)

######################
#selectpercentile
#####################
from sklearn.feature_selection import SelectPercentile, f_classif
selector = SelectPercentile(f_classif, percentile=30)
selector.fit(features, labels)
features = selector.transform(features)
print selector._get_support_mask()
print selector.scores_

## f_classif scores -> (salary, 18.3)(bonus, 20.8)(excersied stock options, 24.8)
# (to poi percentage, 16.6)(long term incentive, 9.9)(expenses,6.1)
# (director fees, 2.12)(total payments, 8.8)
################################
# scaling
################################

#minmaxscalerr
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
#features = scaler.fit_transform(features)
#print scaler.min_
#print scaler.scale_




################################
# outlier removal
################################
from sklearn import linear_model

#outlier class (from lessons)
# def outlierCleaner(predictions, ages, net_worths):
#     cleaned_data = []
#     errors = (net_worths - predictions)**2
#     cleaned_data = zip(ages, net_worths, errors)
#     cleaned_data = sorted(cleaned_data, key = lambda x: x[2], reverse = True)
#     limit = int(len(net_worths)*0.1)
#     return cleaned_data[limit:]
#
# from sklearn import svm
# #reg = GaussianNB()
# #reg.fit(features, labels)
# reg = svm.LinearSVC()
# reg.fit(features, labels)
#
#
# cleaned_data = []
# try:
#     predictions = reg.predict(features)
#     cleaned_data = outlierCleaner(predictions, features, labels)
# except NameError:
#     print "your regression object doesn't exist, or isn't name reg"
#     print "can't make predictions to use in identifying outliers"


#try:
#    plt.plot(features, reg.predict(features), color="blue")
#except NameError:
#    pass
#plt.scatter(features, labels)
#plt.show()

#print len(features)
# features_cleaned = numpy.array([e[0] for e in cleaned_data])
# labels_cleaned = numpy.array([e[1] for e in cleaned_data])

#try:
#    plt.plot(features_cleaned, reg.predict(features_cleaned), color="blue")
#except NameError:
#    pass
#plt.scatter(features_cleaned, labels_cleaned)
#plt.show()

#set features/labels to cleaned set
# features = features_cleaned
# labels = labels_cleaned


#print len(features)
#split train/test
features_train,features_test, labels_train,labels_test = train_test_split(features,labels,
                                            test_size=0.3, random_state=42)



################################
# classifying
################################

#GaussianNB   A- 23 P-14 R-95
#from sklearn.naive_bayes import GaussianNB
#clf = GaussianNB()
#clf.fit(features_train, labels_train)

#SVM   A-  R-  P-
#from sklearn import svm, grid_search
#parameters = {'C':[1, 5, 10]}
#svr = svm.LinearSVC()
#clf = grid_search.GridSearchCV(svr, parameters)
#clf = svm.LinearSVC(multi_class='crammer_singer')
#clf.fit(features_train, labels_train)

#RandomForest   A- 87 P- 55 R- 17
#from sklearn.ensemble import RandomForestClassifier
#from sklearn import grid_search
#clf = RandomForestClassifier(n_estimators=30, min_samples_split=5)
#parameters = {'min_samples_split':[2,3,4,5,6], 'n_estimators': [10,20]}
#random = RandomForestClassifier()
#clf = grid_search.GridSearchCV(random, parameters)
#clf.fit(features_train, labels_train)

#adaboost  A- 85 P- 39 R- 32
from sklearn.ensemble import AdaBoostClassifier
from sklearn import grid_search
#ada = AdaBoostClassifier()
#parameters = {'n_estimators':[10,50,100], 'random_state': [None, 0, 42, 138]}
#clf = grid_search.GridSearchCV(ada, parameters)
clf = AdaBoostClassifier(n_estimators=50, random_state=138)
clf.fit(features_train, labels_train)


#K-Means_clustering R-.28. P-.21 f1-.24
#from sklearn.cluster import KMeans
#clf = KMeans(n_clusters = 2)
#clf.fit(features_train, labels_test)
#print clf.predict(features_test)
#print labels_test

#DecisionTree  #R- .32 P- .33 f1 - .33
from sklearn import grid_search, tree
#parameters = {'min_samples_split':[2,3,4,5,6,7,8,9], 'min_samples_leaf':[1,2,3], 'random_state':[None, 0, 42] }
#tree = tree.DecisionTreeClassifier()
#clf = grid_search.GridSearchCV(tree, parameters)
#clf = tree.DecisionTreeClassifier(min_samples_split = 5, random_state=42)
#clf = clf.fit(features_train, labels_train)
#clf.predict(features_test)
#print clf.best_estimator_
#print labels_test
#print clf.predict(features_test)


#try:
#    plt.plot(features, clf.predict(features), color="blue")
#except NameError:
#    pass
#plt.scatter(features, labels)
#plt.show()




################################
# validation
################################
predict = clf.predict(features_test)
print 'accuracy: %f' %accuracy_score(labels_test, predict)
print 'Precision: %f' %precision_score(labels_test, predict)
print 'Recall: %f' %recall_score(labels_test, predict)
print 'F1 score: %f' %f1_score(labels_test, predict)

true_pos = 0
true_neg = 0
false_pos = 0
false_neg = 0
#find counts
for num in range(0,len(predict)):
    if predict[num] == 1 and labels_test[num]== 1:
        true_pos += 1
    if predict[num] == 0 and labels_test[num]== 0:
        true_neg += 1
    if predict[num] == 1 and labels_test[num]== 0:
        false_pos += 1
    if predict[num] == 0 and labels_test[num]== 1:
        false_neg += 1
#prints
print 'True Positives: %d' %true_pos
print 'True Negatives: %d' %true_neg
print 'False Positive: %d' %false_pos
print 'False Negative: %d' %false_neg




################################
# tune classifier
################################
test_classifier(clf, my_dataset, features_list)



################################
# dump data
################################
dump_classifier_and_data(clf, my_dataset, features_list)


