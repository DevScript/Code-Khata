import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# TfidfVectorizer is used to convert text data into numerical value
# accuracy_score is used to define how well our model is performing and how well it is predicting

#Data Collection and preprocessing
# loading the data from csv file to a pandas Dataframe

raw_mail_data = pd.read_csv('/content/mail_data.csv')
print(raw_mail_data)

# replace the null values with null string
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)),'')

# printing the first five rows
mail_data.head()

#checking the number of rows and columns in the dataframe
mail_data.shape

# 5572 - represents the number of rows 
# 2 - represents the number of mails present either it is a ham mail or spam mail

# label spam mail as 0; ham mail as 1;
mail_data.loc[mail_data['Category']=='spam','Category',] = 0
mail_data.loc[mail_data['Category']=='ham','Category',] = 1
# first line of code will convert all the spam mails as zero.
# second line of code will convert all the ham mails as one.
# spam - 0
# ham - 1


# seperating the data as texts and label

X = mail_data['Message']

Y = mail_data['Category']
print(X)

print(Y)

# Splitting the data into training data and test data
X_train , X_test, Y_train , Y_test = train_test_split(X,Y,test_size=0.2, random_state=3) 
print(X.shape)
print(X_train.shape)
print(X_test.shape)

# Feature Extraction
# transform the text data to feature vectors that can be used as input to the logistic regression model

feature_extraction = TfidfVectorizer(min_df = 1,stop_words= 'english', lowercase = 'True')

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

#convert Y_train and Y_test values as integers

Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')
print(X_train)
print(X_train_features)

# Training the Model
model = LogisticRegression()
# training the logisticregression model

model.fit(X_train_features, Y_train)

# Evaluating the trained model
# prediction on training data
prediction_on_training_data = model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train,prediction_on_training_data)
print('Accuracy_on_training_data :', accuracy_on_training_data)

# prediction on test data
prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test,prediction_on_test_data)

print('Accuracy_on_test_data :', accuracy_on_test_data)

# Building a predictive system
input_mail = ["I've been searching for the right words to thank you for this breather. I promise i wont take your help for granted and will fulfil my promise. You have been wonderful and a blessing at all times."]

# convert text to feature vectors
input_data_features = feature_extraction.transform(input_mail)

# making prediction

prediction = model.predict(input_data_features)
print(prediction)

if (prediction[0]==1):
      print('Ham mail')

else:
  print('Spam mail')