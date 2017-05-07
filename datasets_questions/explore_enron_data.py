#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
from math import isnan
import sys
import pprint
sys.path.append("../tools/")
from feature_format import featureFormat

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of People: ",len(enron_data.keys())
print "Number of features: ", max([len(value) for key,value in enron_data.items()])
print "Number of Persons of Interest: ", len([value["poi"] for key,value in enron_data.items() if value["poi"]==1])

print "Total stock with James Prentice: ", enron_data["PRENTICE JAMES"]["restricted_stock"] + enron_data["PRENTICE JAMES"]["exercised_stock_options"]

print "Number of emails from Wesley Colwell to POI: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "value of stock options exercised by Jeffrey K Skilling: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

poi_total_payments = 0
for person in ["LAY KENNETH L", "SKILLING JEFFREY K", "FASTOW ANDREW S"] :
    if enron_data[person]["total_payments"] > poi_total_payments:
        poi = person
        poi_total_payments = enron_data[person]["total_payments"] 
print "Person with Highest payment: ", poi, " total payments: ", poi_total_payments 

poi_email_address_count = 0
poi_salary_count = 0
for k,v in enron_data.items():
    if v["email_address"] != 'NaN':
        poi_email_address_count += 1
    if isinstance(v["salary"], int):
        poi_salary_count +=1
print "Number of people with email address: ", poi_email_address_count  
print "Number of people with known salary: ", poi_salary_count

features_list = ['poi','salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income',
'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees',
'to_messages', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi']

pprint.PrettyPrinter().pprint(featureFormat(enron_data, features_list))
